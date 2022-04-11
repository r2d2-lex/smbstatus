from getuserlist import make_uid_users_dict

from flask import Flask, render_template
from smbstat import smb_status, parse_status, sort_records
import config

app = Flask(__name__)


@app.route('/')
def index():
    page_title = 'SambaStatus'
    uid_users_dict = make_uid_users_dict()

    smb_lines = parse_status(uid_users_dict)
    smb_lines = sort_records(smb_lines, config.PATH_NAME_INDEX)
    return render_template('smbstatus/index.html', page_title=page_title, smb_lines=smb_lines)


def main():
    uid_users_dict = make_uid_users_dict()

    smb_data = smb_status()
    smb_lines = parse_status(smb_data, uid_users_dict)


if __name__ == '__main__':
    # main()
    app.run(debug=True)
