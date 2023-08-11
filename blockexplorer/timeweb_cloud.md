##Деплой проекта на VPS серевер timeweb


установка общих зависимостей
```
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
```

```
sudo -H pip3 install --upgrade pip
```

```
sudo -H pip3 install virtualenv
```

```
virtualenv venv
```

```
. venv/bin/activate
```
установка зависимостей
```
pip install -r requirements.txt
```
установить расширение для VSCode
```
Remote-SSH
```

```
Host my_remote_server
    HostName your_server_ip_or_hostname
    User sammy
    IdentityFile /location/of/your/private/key
```
добавить IP и домен в 
```
ALLOWED_HOSTS
```
подготавливаем conf_prod.py
```
cd config && touch conf_prod.py
```
```
import os

from .settings import *

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = False

del STATICFILES_DIRS
STATIC_ROOT = BASE_DIR / "static"
```
```
export DJANGO_SECRET_KEY="[key]"
```
```
export DJANGO_SETTINGS_MODULE="config.conf_prod"
```
проверка

```
grep DJANGO
```
```
python manage.py collectstatic
```

##в связи с тем что Django не работает с Nginx напряую, нужно настроить Gunicorn

тест Gunicorn

```
gunicorn --bind 0.0.0.0:8000 myproject.wsgi
```

```
deactivate
```

##cоздание файлов сокета и служебных файлов systemd для Gunicorn

```
sudo nano /etc/systemd/system/gunicorn.socket
```

```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

```
sudo nano /etc/systemd/system/gunicorn.service
```

```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=admin
Group=admin
WorkingDirectory=/home/admin/Git/Django_blockexplorer
ExecStart=/home/admin/Git/Django_blockexplorer/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          config.wsgi:application

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl start gunicorn.socket
```

```
sudo systemctl enable gunicorn.socket
```

```
sudo systemctl status gunicorn.socket
```
проверка, должно быть /run/gunicorn.sock: socket
```
file /run/gunicorn.sock
```
журналы ошибок
```
sudo journalctl -u gunicorn.socket
```
если статус Active: inactive (dead)
```
curl --unix-socket /run/gunicorn.sock localhost
```

```
sudo systemctl status gunicorn
```
журнал
```
sudo journalctl -u gunicorn
```
перезагрузка
```
sudo systemctl daemon-reload
```

```
sudo systemctl restart gunicorn
```
##Настройка Nginx как прокси для Gunicorn
```
sudo nano /etc/nginx/sites-available/Django_blockexplorer
```

```
server {
    listen 80;
    server_name easyexplorer.io;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static {
        root /home/admin/Git/Django_blockexplorer;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

```
sudo ln -s /etc/nginx/sites-available/Django_blockexplorer /etc/nginx/sites-enabled
```
тест Nginx
```
sudo nginx -t
```

```
sudo systemctl restart nginx
```
устанавливаем права для пользователя
```
sudo usermod -a -G [user name] www-data
```

```
sudo chown -R :www-data /path/to/your/static/folder
```
##Настройка берндмауэра UWF
```
sudo apt install ufw
```

```
sudo ufw default deny incoming
```
### тест
```
sudo ufw default allow outgoing
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
