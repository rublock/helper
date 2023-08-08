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
размещение статики для Nginx
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```

```
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

```
python manage.py collectstatic
```

```
python manage.py runserver 0.0.0.0:8000
```

```
cd config/ && touch conf_prod.py
```
conf_prod.py
```
import os

from .settings import *


SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = False
```
установка переменной окружения
```
export DJANGO_SETTINGS_MODULE="config.conf_prod" && env | grep DJANGO
```
проверка
```
env | grep DJANGO
```

```
export DJANGO_SECRET_KEY='[key]'
```
в связи с тем что Django не работает с Nginx напряую нужно настровить Gunicorn
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
