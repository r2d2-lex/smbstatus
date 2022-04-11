USERNAME = 'username@work.org'
PASSWORD = 'password'
HOSTNAME = 'dc.work.org'
BASE_DN_GRP = 'CN=Users,DC=work,DC=org'
BASE_DN_OU = 'OU={},DC=work,DC=org'
GROUP_FILTER = '(objectCategory=group)'
GROUP_MEMBERS_FILTER = '(&(objectCategory=group)(cn={}))'
USER_FILTER_TEMPLATE = '(&(objectCategory=person)(name={}))'
USER_FILTER = '(&(objectCategory=person)(sAMAccountName={}))'


SSH_CMD = '/usr/bin/ssh'
SSH_OPTIONS = '-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
SSH_PASS = '/usr/bin/sshpass'
SSH_STATUS_COMMAND = 'sudo /root/supercommand.sh'
SSH_USER = 'user'
SSH_PASSWORD = 'password'
SRC_HOST = '127.0.0.1'

LOGIN_NAME_INDEX = 9
PATH_NAME_INDEX = 7
