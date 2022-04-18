from flask import Flask, render_template, request

from webapp.forms import SearchForm
from webapp.getuserlist import make_uid_users_dict
from webapp.smbstatus import smb_status, parse_status, sort_records, search_records


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    def check_get_args(req):
        user_name = req.args.get("username")
        file_name = req.args.get("filename")
        if not isinstance(user_name, str):
            user_name = ''
        if not isinstance(file_name, str):
            file_name = ''
        return user_name, file_name

    @app.route('/', methods=['GET', 'POST'])
    def index():
        user_name = ''
        file_name = ''
        sort_type = app.config['PATH_NAME_INDEX']

        if request.method == "GET":
            user_name, file_name = check_get_args(request)

        search_form = SearchForm()
        if search_form.validate_on_submit():
            user_name = search_form.username.data
            file_name = search_form.filename.data
            sort_type_data = search_form.sort_type.data
            if sort_type_data == 'sort_filename':
                sort_type = app.config['PATH_NAME_INDEX']
            elif sort_type_data == 'sort_username':
                sort_type = app.config['LOGIN_NAME_INDEX']
            elif sort_type_data == 'sort_share':
                sort_type = app.config['SHARE_NAME_INDEX']

        uid_users_dict = make_uid_users_dict()
        smb_lines, list_of_user_names = parse_status(uid_users_dict)
        if len(user_name) > 0:
            smb_lines = search_records(smb_lines, app.config['LOGIN_NAME_INDEX'], user_name)
        if len(file_name) > 0:
            smb_lines = search_records(smb_lines, app.config['PATH_NAME_INDEX'], file_name)
        smb_lines = sort_records(smb_lines, sort_type)
        return render_template('smbstatus/index.html', page_title=app.config['PAGE_TITLE'], smb_lines=smb_lines,
                               form=search_form, records_count=len(smb_lines), user_names=list_of_user_names)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
