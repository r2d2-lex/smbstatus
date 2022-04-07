import subprocess


def prepare_remote_command(remote_command, ssh_pass_cmd, ssh_password, ssh_cmd, ssh_options, ssh_user, src_host):
    cmd = '{SSH_PASS} -p {SSH_PASSWORD} {SSH_CMD} {SSH_OPTIONS} {SSH_USER}@{SRC_HOST} {SSH_STATUS_COMMAND}' \
          ''.format(SSH_PASS=ssh_pass_cmd,
                    SSH_PASSWORD=ssh_password,
                    SSH_CMD=ssh_cmd,
                    SSH_OPTIONS=ssh_options,
                    SSH_USER=ssh_user,
                    SRC_HOST=src_host,
                    SSH_STATUS_COMMAND=remote_command)
    return cmd


def start_shell_command(cmd):
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    return output
