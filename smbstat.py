from getuserlist import get_user_list, make_uid_users_dict, check_uid
from remote_command import smb_status


def main():
    # Получаем результат smbstatus -L
    smb_status_result = smb_status()
    print(smb_status_result)

    # Получаем список пользователей
    uid_users_dict = make_uid_users_dict(get_user_list())
    print(uid_users_dict)


if __name__ == '__main__':
    main()
