0. sudo apt install build-essential python3-dev libsasl2-dev slapd ldap-utils valgrind \
python-dev libldap2-dev libssl-dev libpcre3 libpcre3-dev

1. sudo apt install virtualenv python3-venv

2. cd /%root%/
example root dir: cd /var/www
git clone git clone https://github.com/r2d2-lex/smbstatus.git

3. cd /%root%/smbstatus
python3 -m venv venv

4. source ./venv/bin/activate

5. pip install -r requirements.txt

6. Make config:
cd /%root%/smbstatus/webapp/
cp config-example.py config.py

7. Create start uwsgi service:
cd /%root%/smbstatus/systemd
cp smbstatus.service /etc/systemd/system/

8. Test uwsgi:
cd %root%
uwsgi --socket 127.0.0.1:5000 --protocol=http -w webapp.uwsgi:app

9.
cd %root%
chown -R www-data. smbstatus/

10. Make nginx resource:
cp /%root%/smbstatus/nginx/smbstatus /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/smbstatus /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx


EXAMPLE RUN from command prompt:
uwsgi --socket 127.0.0.1:5000 --protocol=http -w webapp.uwsgi:app_run

11. Make on target host:
set SAMBA_STATUS_COMMAND and KILL_USER_COMMAND in config.py like:
SAMBA_STATUS_COMMAND = 'sudo /usr/local/bin/smbstat.sh'
KILL_USER_COMMAND = 'sudo /usr/local/bin/killuser.sh'

Copy scripts on target host:
scp server-script/_killuser.sh remoteuser@targethost:/usr/local/bin/killuser.sh
scp server-script/_smbstat.sh remoteuser@targethost:/usr/local/bin/smbstat.sh

Make visudo records:
remoteuser ALL= NOPASSWD: /usr/local/bin/smbstat.sh
remoteuser ALL= NOPASSWD: /usr/local/bin/killuser.sh
