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
