from webapp.utils.remote_command import prepare_remote_command, start_shell_command
import webapp.config as config
# from utils.remote_command import prepare_remote_command, start_shell_command
# import config as config


def kill_user_session(pid: str):
    try:
        kill_pid_command = f'{config.KILL_USER_COMMAND} {config.KILL_USER_PASSWORD} {str(pid)}'
        print('kill_pid_command:', kill_pid_command)
        kill_command = prepare_remote_command(kill_pid_command,
                                              config.SSH_PASS_CMD,
                                              config.SSH_PASSWORD,
                                              config.SSH_CMD,
                                              config.SSH_OPTIONS,
                                              config.SSH_USER,
                                              config.SRC_HOST,
                                              )
        result = start_shell_command(kill_command)
    except TypeError:
        result = 'Fail command'
    return result


def main():
    kill_result = kill_user_session('5555555')
    print(kill_result)


if __name__ == '__main__':
    main()
