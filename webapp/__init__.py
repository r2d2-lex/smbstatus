from flask import Flask, render_template

from webapp.forms import SearchForm
from webapp.getuserlist import make_uid_users_dict
from webapp.smbstat import smb_status, parse_status, sort_records


# import webapp.config


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        sort_form = SearchForm()
        uid_users_dict = make_uid_users_dict()
        smb_lines = parse_status(uid_users_dict)
        smb_lines = sort_records(smb_lines, app.config['PATH_NAME_INDEX'])
        return render_template('smbstatus/index.html', page_title=app.config['PAGE_TITLE'], smb_lines=smb_lines, form=sort_form)

    @app.route('/sort', methods=['GET', 'POST'])
    def sort():
        sort_form = SearchForm()
        for item1 in sort_form:
            print('Item: ', item1)
        print('Sort FORM: ', sort_form)
        uid_users_dict = make_uid_users_dict()
        smb_lines = parse_status(uid_users_dict)
        smb_lines = sort_records(smb_lines, app.config['PATH_NAME_INDEX'])
        return render_template('smbstatus/index.html', page_title=app.config['PAGE_TITLE'], smb_lines=smb_lines, form=sort_form)

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
