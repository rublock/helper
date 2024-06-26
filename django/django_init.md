# Django

* инициализируем репозиторий на github.com
* клонируем репозиторий
```
git clone
```
* устанавливаем pip
```
sudo apt install python3-pip
```
* устанавливаем вирутальное окружение virtualenv
```
sudo pip install virtualenv && virtualenv venv && . venv/bin/activate
```
* смотрим актуальную версию Django
```
https://www.djangoproject.com/download/
```
* установка Django
```
pip install Django
```
```
pip install black
```
```
pip install isort
```
* если нет файла зависимостей
```
touch requirements.txt
```
* проверка версии Django
```
python -m django --version
```
* инициализация проекта config - папка с настройками проекта
```
django-admin startproject config .
```
* создаем Django приложение mainapp - имя приложения
```
python manage.py startapp mainapp
```
* проверяем работу Django на локальной машине
```
python manage.py runserver
```
* заливаем зависимости в файл
```
pip freeze > requirements.txt
```
---
* asgi.py и wsgi.py - файлы для взаимодействия с сервером балансировщиком, требуются во время развертывания проекта на сервере
* settings.py - настройки всего проекта
* urls.py - корневой диспетчер адресов, перенапраляем запрос пользователя
* mainapp/migrations - тут будут лежать файлы миграции для автоматической загрузки БД
* admin.py - регистрация классов которые связывают проект и БД через вэб интерфейс (админку)
* apps.py - моудль конфигурации созданного приложения
* models.py - модуль описания моделей для взаимосвязи с БД
* tests.py - модуль с тестами
* views.py - модуль с контроллерами приложения
* db.sqlite3 - модуль с базой данный sqlite
* manage.py - модуль управления проектом
---
* устанавливаем плагины для VSCode - Python, Pylance, Djaneiro
* в правом нижнем углу выбрать интерпритатор Python из виртуального окружения
* настраиваем отладчик - run and debug - выбираем Django - нажимаем шестиренку
```python
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "runserver",
                "0.0.0.0:8000",
            ],
            "django": true,
            "justMyCode": true
        }
    ]
}
```
* добавить созданое приложение mainapp в INSTALLED APPS в файле settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',
]
```
---
##### Найтсройка переменных окружения
```
touch sample.env
```
```
touch .env
```
```
pip install python-dotenv
```
* config/settings.py
```python
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = bool(int(os.environ.get('DEBUG', 0)))

ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get('ALLOWED_HOSTS', '').split(','),
    )
)
```
* sample.env
```
SECRET_KEY=""
DEBUG=1
ALLOWED_HOSTS=0.0.0.0,127.0.0.1
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
```
* чтобы создались все таблицы в том числе административные нужно провести миграции
```
python manage.py makemigrations
```
```
python manage.py migrate
```
* фиксируем имзенения на github
```
git add . && git commit -am "Initial commit" && git push
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

