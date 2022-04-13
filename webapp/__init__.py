from flask import Flask, render_template

from webapp.forms import SearchForm
from webapp.getuserlist import make_uid_users_dict
from webapp.smbstat import smb_status, parse_status, sort_records, search_records


# import webapp.config


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        search_form = SearchForm()
        uid_users_dict = make_uid_users_dict()
        smb_lines = parse_status(uid_users_dict)
        smb_lines = sort_records(smb_lines, app.config['PATH_NAME_INDEX'])
        return render_template('smbstatus/index.html', page_title=app.config['PAGE_TITLE'], smb_lines=smb_lines,
                               form=search_form)

    @app.route('/search', methods=['GET', 'POST'])
    def sort():
        sort_type = app.config['PATH_NAME_INDEX']
        search_form = SearchForm()
        user_name = ''
        file_name = ''

        if search_form.validate_on_submit():
            user_name = search_form.username.data
            file_name = search_form.filename.data
            print('UserName: ', user_name)
            print('FileName: ', file_name)

            print('Sort type: ', search_form.sort_type.data)
            sort_type_data = search_form.sort_type.data
            if sort_type_data == 'sort_filename':
                sort_type = app.config['PATH_NAME_INDEX']
            elif sort_type_data == 'sort_username':
                sort_type = app.config['LOGIN_NAME_INDEX']
            elif sort_type_data == 'sort_share':
                sort_type = app.config['SHARE_NAME_INDEX']

        uid_users_dict = make_uid_users_dict()
        smb_lines = parse_status(uid_users_dict)
        if len(user_name) > 3:
            smb_lines = search_records(smb_lines, app.config['LOGIN_NAME_INDEX'], user_name)
        if len(file_name) > 0:
            smb_lines = search_records(smb_lines, app.config['PATH_NAME_INDEX'], file_name)
        smb_lines = sort_records(smb_lines, sort_type)
        return render_template('smbstatus/index.html', page_title=app.config['PAGE_TITLE'], smb_lines=smb_lines,
                               form=search_form)

    return app

# def main():
#     uid_users_dict = make_uid_users_dict()
#
#     smb_data = smb_status()
#     smb_lines = parse_status(smb_data, uid_users_dict)
#
#
# if __name__ == '__main__':
#     # main()
#     app.run(debug=True)
