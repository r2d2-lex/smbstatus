0. apt install build-essential python3-dev libsasl2-dev slapd ldap-utils valgrind \
python-dev libldap2-dev libssl-dev libpcre3 libpcre3-dev

1. sudo apt install virtualenv

2. sudo apt-get install python3-venv

3. python3 -m venv venv

4. pip install -r requirements.txt

5. Make config:
cd /%root%/smbstatus/webapp/
cp config-example.py config.py

6. Create start uwsgi service:
cd /%root%/smbstatus/systemd
cp smbstatus.service /etc/systemd/system/

7. Test uwsgi:
cd %root%
uwsgi --socket 127.0.0.1:5000 --protocol=http -w webapp.uwsgi:app

8.
cd %root%
chown -R www-data. smbstatus/

9. Make nginx resource:
cp /%root%/smbstatus/nginx/smbstatus /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/smbstatus /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
