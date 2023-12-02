### Docker-compose

* версия
```
docker --version
```
* собрать проект
```
docker-compose build
```
* запустить проект
```
docker-compose up -d
```
* остановить проект
```
docker-compose down
```
* остановить проект и удалить контейнеры
```
docker-compose down -v
```
* посмотреть логи сервиса
```
docker-compose logs -f [service_name]
```
* вывести список контейнеров
```
docker-compose ps
```
* выполнить комманду в контейнере
```
docker-compose exec [service name] [command]
```
* вывести список образов
```
docker-compose images
```
### Подготовка глобальных переменных
* обновить список зависимостей requirements.txt
```
python-dotenv==1.0.0
```
* отредактировать файл настроек settings.py
```
from dotenv import load_dotenv
import os
load_dotenv()
```
* Далее изменим нужные переменные:
```python
SECRET_KEY = str(os.getenv('SECRET_KEY'))

DEBUG = str(os.getenv('DEBUG'))

ALLOWED_HOSTS = str(os.getenv('DJANGO_ALLOWED_HOSTS')).split(" ")

CACHES = {
    'default': {
        'BACKEND': str(os.getenv('CACHES_BACKEND')),
        'LOCATION': str(os.getenv('CACHES_LOCATION')),
    }
}

INTERNAL_IPS = str(os.getenv('INTERNAL_IPS')).split(" ")

CSRF_TRUSTED_ORIGINS = str(os.getenv('CSRF_TRUSTED_ORIGINS')).split(" ")
```
* создадим папку app в нашем проекте и перенесем туда весь проект кроме .env venv docker-compose.yml
```
mkdir app
```
* создадим файл .env в корне проекта
```
touch .env
```
* заполним файл .env
```
DEBUG = True
SECRET_KEY = 'django-insecure-xxxxxxxxxxxx'
DJANGO_ALLOWED_HOSTS = '127.0.0.1'
CSRF_TRUSTED_ORIGINS = 'http://127.0.0.1'
CACHES_BACKEND = 'django.core.cache.backends.locmem.LocMemCache'
CACHES_LOCATION = 'unique-snowflake'
INTERNAL_IPS = '127.0.0.1'
```
* создадим файл в конре проекта docker-compose.yml
```
touch docker-compose.yml
```
* заполним файл docker-compose.yml
```
version: '3.8'

services:
  web:
    # Берем Dockerfile из каталога app
    build: ./app
    # Запускаем тестовый сервер
    command: python manage.py runserver 0.0.0.0:8000
    # куда будут помещены данные из каталога app
    volumes:
      - ./app/:/usr/src/app/
    # Открываем порт 8000 внутри и снаружи
    ports:
      - 8000:8000
    # Файл содержащий переменные для контейнера
    env_file:
      - ./.env
```
* создадим файл .dockerignore в корне проекта
```
touch .dockerignore
```
* заполним файл .dockerignore
```
venv
.idea
```
* создаем образ
```
docker-compose build
```
* запускаем контейнер
```
docker-compose up -d
```
### Подключение PostgreSQL
* добавим в docker-compose.yml блок db с учетными данными
* если не описывать volume для контейнера с базой, каждое пересоздание контейнера приведет к уничтожению базы и данных. docker-том postgres_data будет хранить данные на случай пересоздания контейнера
```
  db:
      image: postgres:[version] - заменить
      volumes:
        - postgres_data:/var/lib/postgresql/data/
      environment:
        - POSTGRES_USER=book_django
        - POSTGRES_PASSWORD=pass_book_django
        - POSTGRES_DB=book_django

volumes:
  postgres_data:
```
* в файле .env добавляем
```
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=book_django
SQL_USER=book_django
SQL_PASSWORD=pass_book_django
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
* в файле setting.py меняем настройки БД
```python
DATABASES = {
    "default": {
        "ENGINE": str(os.getenv("SQL_ENGINE")),
        "NAME": str(os.getenv("SQL_DATABASE")),
        "USER": str(os.getenv("SQL_USER")),
        "PASSWORD": str(os.getenv("SQL_PASSWORD")),
        "HOST": str(os.getenv("SQL_HOST")),
        "PORT": str(os.getenv("SQL_PORT")),
    }
}
```
* устанавливаем зависимости для работы с PostgreSQL
```
psycopg==3.1.12
psycopg-binary==3.1.12
```
* запускаем контейнеры еще раз
```
docker-compose up -d --build
```
* запускаем миграции
```
docker-compose exec web python manage.py migrate --noinput
```
* можно зайти в psql и проверить БД
```
docker-compose exec db psql --username=book_django --dbname=book_django
```
### Подключение Gunicorn и NGINX
* добавим в файл requerements.txt новую зависимость
```
gunicorn==21.2.0
```
* что-бы было удобно использовать образ для локальной разработки и для продакшена, создадим второй файл с названием docker-compose.prod.yml
```
touch docker-compose.prod.yml
```
```
version: '3.8'

services:
  web:
    # Берем Dockerfile из каталога app
    build: app
    # Запускаем сервер gunicorn
    command: gunicorn core.wsgi:application --bind 0.0.0.0:8000
    # Открываем порт 8000 внутри и снаружи
    ports:
      - 8000:8000
    # Файл содержащий переменные для контейнера
    env_file:
      - .env.prod
    # Дожидаемся запуска контейнера db и memcached
    depends_on:
      - db
      - memcached
  db:
      image: postgres:15
      volumes:
        - postgres_data:/var/lib/postgresql/data/
      environment:
        - POSTGRES_USER=book_django
        - POSTGRES_PASSWORD=pass_book_django
        - POSTGRES_DB=book_django
  memcached:
      image: memcached:1.6.21
      ports:
        - 11211:11211
volumes:
  postgres_data:
```
* также в корне проекта создадим файл .env.prod
```
touch .env.prod
```
```
DEBUG = True
SECRET_KEY = 'django-insecure-xxxxxxxxxxxx'
DJANGO_ALLOWED_HOSTS = '127.0.0.1'
CSRF_TRUSTED_ORIGINS = 'http://127.0.0.1'
CACHES_BACKEND = 'django.core.cache.backends.memcached.PyMemcacheCache'
CACHES_LOCATION = 'memcached:11211'
INTERNAL_IPS = '127.0.0.1'

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=book_django
SQL_USER=book_django
SQL_PASSWORD=pass_book_django
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
* создаем контейнер для деплоя
```
docker-compose -f docker-compose.prod.yml up -d --build
```
* выполняем миграции
```
docker-compose exec web python manage.py migrate --noinput
```
### настройка Dockerfile.prod для Django проекта
* в данном примере будет использоваться мульти-образ для экономии места. builder - это временный образ с помощью которого будут созданы бинарные файлы библиотек Python. После создания образа builder с него будут скопированы файлы в наш основной образ.
* в образе мы создаем пользователя app и его группу app. Это делается для того, что бы не использовать пользователя root, который используется по умолчанию в контейнерах Docker.
* Создадим файл в папке app
```
touch Dockerfile.prod
```
```
###########
# BUILDER #
###########

FROM python:3.12.0-alpine as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# установка зависимостей
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip

# установка зависимостей
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

FROM python:3.12.0-alpine

# создаем директорию для пользователя
RUN mkdir -p /home/app

# создаем отдельного пользователя и его группы
RUN addgroup -S app && adduser -S app -G app

# создание директории для проекта Django
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# установка зависимостей
RUN apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# копирование entrypoint-prod.sh
COPY ./entrypoint.prod.sh $APP_HOME

# копирование проекта Django
COPY . $APP_HOME

# смена владельца файлов и директорий проекта Django, на пользователя app
RUN chown -R app:app $APP_HOME

# изменение рабочего пользователя
USER app
```
* создадим файл в папке app, данный файл необходим чтобы проверить работоспособность PostgreSQL перед применением миграции и запуском сервера разработки Django.
```
touch entrypoint.prod.sh
```
```
#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Postgres еще не запущен..."

    # Проверяем доступность хоста и порта
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL запущен"
fi

exec "$@"
```
* изменим файл docker-compose.prod.yml, что бы он использовал новый файл - Dockerfile.prod
```
version: '3.8'

services:
  web:
    # Берем Dockerfile из каталога app
    build:
      context: ./app
      dockerfile: Dockerfile.prod
    # Запускаем сервер gunicorn
    command: gunicorn core.wsgi:application --bind 0.0.0.0:8000
    # Открываем порт 8000 внутри и снаружи
    ports:
      - 8000:8000
    # Файл содержащий переменные для контейнера
    env_file:
      - .env.prod
    # Дожидаемся запуска контейнера db и memcached
    depends_on:
      - db
      - memcached
  db:
      image: postgres:15
      volumes:
        - postgres_data:/var/lib/postgresql/data/
      environment:
        - POSTGRES_USER=book_django
        - POSTGRES_PASSWORD=pass_book_django
        - POSTGRES_DB=book_django
  memcached:
      image: memcached:1.6.21
      ports:
        - 11211:11211
volumes:
  postgres_data:
```
* удаляем контейнеры и запускаем заново
```
docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```
### Подключаем NGINX
* открываем стандартный 80й порт для посетителей сайта, который будет перенаправлять пакеты на 80й порт контейнера nginx. Вы можете изменить 80й порт на любой другой в файле docker-compose.prod.yml
```
version: '3.8'

services:
  web:
    # Берем Dockerfile из каталога app
    build:
      context: ./app
      dockerfile: Dockerfile.prod
    # Запускаем сервер gunicorn
    command: gunicorn core.wsgi:application --bind 0.0.0.0:8000
    # Открываем порт 8000 внутри и снаружи
    ports:
      - 8000:8000
    # Файл содержащий переменные для контейнера
    env_file:
      - .env.prod
    # Дожидаемся запуска контейнера db и memcached
    depends_on:
      - db
      - memcached
  db:
      image: postgres:15
      volumes:
        - postgres_data:/var/lib/postgresql/data/
      environment:
        - POSTGRES_USER=book_django
        - POSTGRES_PASSWORD=pass_book_django
        - POSTGRES_DB=book_django
  memcached:
      image: memcached:1.6.21
      ports:
        - 11211:11211
  nginx:
    build: ./nginx
    ports:
      - 80:80
    depends_on:
      - web
volumes:
  postgres_data:
```
* в корне проекта создадим папку nginx, в которой будут хранится конфигурационный файл htmx_book.conf и файл Dockerfile.
```
mkdir nginx
```
```
touch htmx_book.conf
```
```
upstream htmx_book {
    # Список бэкэнд серверов для проксирования
    server web:8000;
}

server {
    listen 80;
    # Ваш домен
    server_name 127.0.0.1;
    # Параметры проксирования
    location / {
        # Если будет открыта корневая страница
        # все запросу пойдут к одному из серверов
        # в upstream htmx_book
        proxy_pass http://htmx_book;
        # Устанавливаем заголовки
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        # Отключаем перенаправление
        proxy_redirect off;
    }

}
```
```
touch Dockerfile
```
```
FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf
COPY htmx_book.conf /etc/nginx/conf.d/
```
* заменим port на expose, в файле docker-compose.prod.yml
```
version: '3.8'

services:
  web:
    # Берем Dockerfile из каталога app
    build:
      context: ./app
      dockerfile: Dockerfile.prod
    # Запускаем сервер gunicorn
    command: gunicorn core.wsgi:application --bind 0.0.0.0:8000
    # Слушаем порт 8000
    expose:
      - 8000
    # Файл содержащий переменные для контейнера
    env_file:
      - .env.prod
    # Дожидаемся запуска контейнера db и memcached
    depends_on:
      - db
      - memcached
  db:
      image: postgres:15
      volumes:
        - postgres_data:/var/lib/postgresql/data/
      environment:
        - POSTGRES_USER=book_django
        - POSTGRES_PASSWORD=pass_book_django
        - POSTGRES_DB=book_django
  memcached:
      image: memcached:1.6.21
      ports:
        - 11211:11211
  nginx:
    build: ./nginx
    ports:
      - 80:80
    depends_on:
      - web
volumes:
  postgres_data:
```
* пересоздадим контейнер
```
docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```
* теперь проект доступен по адерсу без порта
```
http://127.0.0.1
```
### Настройки для статических и медиа файлов
* в файле settings.py
```
# url директории статических файлов
STATIC_URL = "/static/"
# Путь до директории статических файлов
STATIC_ROOT = BASE_DIR / "static"

# url директории медиа файлов
MEDIA_URL = "/media/"
# Путь до директории медиа файлов
MEDIA_ROOT = BASE_DIR / "media"
```
* статические файлы могут быть использованы как Nginx, так и Django мы создадим 2 тома в Docker и подключим их к обоим контейнерам
* для этого изменим файл docker-compose.prod
```
version: '3.8'

services:
  web:
    # Берем Dockerfile из каталога app
    build:
      context: ./app
      dockerfile: Dockerfile.prod
    # Запускаем сервер gunicorn
    command: gunicorn core.wsgi:application --bind 0.0.0.0:8000
    # Слушаем порт 8000
    expose:
      - 8000
    # Подключаем статические и медиа файлы
    volumes:
      - static_volume:/home/app/web/static
      - media_volume:/home/app/web/media
    # Файл содержащий переменные для контейнера
    env_file:
      - .env.prod
    # Дожидаемся запуска контейнера db и memcached
    depends_on:
      - db
      - memcached
  db:
      image: postgres:15
      volumes:
        - postgres_data:/var/lib/postgresql/data/
      environment:
        - POSTGRES_USER=book_django
        - POSTGRES_PASSWORD=pass_book_django
        - POSTGRES_DB=book_django
  memcached:
      image: memcached:1.6.21
      ports:
        - 11211:11211
  nginx:
    build: ./nginx
    # Подключаем статические и медиа файлы
    volumes:
      - static_volume:/home/app/web/static
      - media_volume:/home/app/web/media
    ports:
      - 80:80
    depends_on:
      - web
volumes:
  postgres_data:
  static_volume:
  media_volume:
```
* чтобы у нас не было проблем с правами (эти папки будут проброшены с правами для root) мы должны создать аналогичные папки в контейнере
* для этого добавим в Dockerfile.prod в папке app в месте где происходит создание каталога для приложения
```
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
```
* нужно изменить файл конфигурации Nginx что он тоже мог обращаться к этим папкам
```
upstream htmx_book {
    # Список бэкэнд серверов для проксирования
    server web:8000;
}

server {
    listen 80;
    # Ваш домен
    server_name 127.0.0.1;
    # Параметры проксирования
    location / {
        # Если будет открыта корневая страница
        # все запросу пойдут к одному из серверов
        # в upstream htmx_book
        proxy_pass http://htmx_book;
        # Устанавливаем заголовки
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        # Отключаем перенаправление
        proxy_redirect off;
    }
        # подключаем статические файлы
    location /static/ {
        alias /home/app/web/static/;
    }
    # подключаем медиа файлы
    location /media/ {
        alias /home/app/web/media/;
   }

}
```
* пересоздадим контейнер
```
docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
```
* выполним миграции и соберем статические файлы
```
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --no-input
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input
```
