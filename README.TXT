0. apt install build-essential python3-dev libsasl2-dev slapd ldap-utils valgrind \
python-dev libldap2-dev libssl-dev
1. sudo apt install virtualenv
2. sudo apt-get install python3-venv
3. python3 -m venv venv
4. pip install -r requirements.txt
5. test uwsgi
uwsgi --socket 127.0.0.1:5000 --protocol=http -w webapp.uwsgi:app
