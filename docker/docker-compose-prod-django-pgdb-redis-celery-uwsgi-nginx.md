### Deployment Django with docker-compose, postgres, redis, celery, uwsgi, nginx
* mk dir app/ - создать в корне проекта и переместить туда все файлы Django приложения кроме requirements.txt
* touch Dockerfile
```
# Взять официальный базовый образ Python с платформы Docker
FROM python:alpine3.19
LABEL maintainer="rublock"

# Задать переменные среды
ENV PYTHONUNBUFFERED 1

# Скопировать код в работчий каталог в образ
COPY ./requirements.txt ./requirements.txt
COPY .app/ .app/

# Задать рабочий каталог
WORKDIR /app
EXPOSE 8000

# Установка python, venv, зависимостей, регистарция пользователя
RUN python -m venv /python && \
    /python/bin/pip install --upgrade pip && \
    /python/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home admin

# Путь к локальному виртуальному окружению
ENV PATH="/python/bin:$PATH"

# Переключаемся на локального пользователя
USER admin
```
* touch .dockerignore
```
# Git
.git
.gitignore

# Docker
.docker

# Python
app/__pycache__/
app/*/__pycache__/
app/*/*/__pycache__/
app/*/*/*/__pycache__/
.env/
.venv/
venv/

# Local PostgreSQL data
data/
```
* cd app/config/ && mkdir settings
* touch base.py
> * настройки общие для local и prod
* touch local.py
> * настройки для разработки
* touch prod.py
> * настройки для продакшн
* app/config/settings/local.py
```
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0']

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
* app/config/settings/prod.py
```
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['82.97.241.112', '127.0.0.1']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.environ.get('POSTGRES_DB'),
       'USER': os.environ.get('POSTGRES_USER'),
       'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
       'HOST': 'postgres',
       'PORT': 5432,
   }
}
```
* все остальное в base.py
* touch docker-compose.yml
```yml
version: "3.8"

services:
  django:
    container_name: django
    build:
      context: .
    ports:
      - 8000:8000
    volumes:
      - ./app:/app
    env_file:
      - .env
    depends_on:
      - postgres

  postgres:
    image: postgres:alpine3.19
    container_name: postgres
    restart: always
    volumes:
      - postgres-data:/var/lib/postgresql/data/
    env_file:
      - .env
```
* touch .env && touch env.sample
```
SECRET_KEY='jw!v45^#vy3h&)5ll5-3q1a=y^3_p*3%kk7@g3uy=)j+q9gw!5'
DJANGO_SETTINGS_MODULE=config.settings.local
CELERY_BROKER=redis://redis:6379/0
CELERY_BACKEND=redis://redis:6379/0
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```
* app/config/settings/base.py
```python
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')
```
* скрипт для ожидания готовности базы postgres
* touch app/mainapp/management/commands/wait_for_db.py
```python
"""
Django command to wait for the database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
