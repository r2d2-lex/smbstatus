import subprocess
from getuserlist import get_user_list, make_uid_users_dict, check_uid
import config


def prepare_remote_command(remote_command):
    cmd = '{SSH_PASS} -p {SSH_PASSWORD} {SSH_CMD} {SSH_OPTIONS} {SSH_USER}@{SRC_HOST} {SSH_STATUS_COMMAND}' \
          ''.format(SSH_PASS=config.SSH_PASS,
                    SSH_PASSWORD=config.SSH_PASSWORD,
                    SSH_CMD=config.SSH_CMD,
                    SSH_OPTIONS=config.SSH_OPTIONS,
                    SSH_USER=config.SSH_USER,
                    SRC_HOST=config.SRC_HOST,
                    SSH_STATUS_COMMAND=remote_command)
    return cmd


def smb_stat_command():
    return prepare_remote_command(config.SSH_STATUS_COMMAND)


def start_shell_command(cmd):
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    return output


def smb_status():
    smb_status_command = smb_stat_command()
    return start_shell_command(smb_status_command)


def main():
    # Получаем результат smbstatus -L
    smb_status_result = smb_status()
    print(smb_status_result)

    # Получаем список пользователей
    uid_users_dict = make_uid_users_dict(get_user_list())
    print(uid_users_dict)


if __name__ == '__main__':
    main()
