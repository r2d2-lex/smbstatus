from getuserlist import get_user_list, make_uid_users_dict, check_uid
from remote_command import prepare_remote_command, start_shell_command
import config


def smb_status():
    smb_status_command = prepare_remote_command(config.SAMBA_STATUS_COMMAND,
                                                config.SSH_PASS_CMD,
                                                config.SSH_PASSWORD,
                                                config.SSH_CMD,
                                                config.SSH_OPTIONS,
                                                config.SSH_USER,
                                                config.SRC_HOST,
                                                )
    return start_shell_command(smb_status_command)


def main():
    # Получаем результат smbstatus -L
    smb_status_result = smb_status()
    print(smb_status_result)

    # Получаем список пользователей
    # uid_users_dict = make_uid_users_dict()
    # print(uid_users_dict)


if __name__ == '__main__':
    main()
