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
* создаем .gitignore
```
wget -O .gitignore https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore
```
* добавляем лицензию
```
echo "MIT" > LICENSE
```
* создаем README.md
```
touch README.md
```
* смотрим актуальную версию Django
```
https://www.djangoproject.com/download/
```
* установка Django
```
pip install Django==4.2.4
```
* если нет файла зависимостей
```
touch requirements.txt && pip freeze -> requirements.txt
```
* если уже есть файл с зависимостями
```
pip install -r requirements.txt
```
* указываем интерпритатор Python в IDE из нашей папки
```
venv/bin/python
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
* добавляем разрешаем доступ с любого хоста
```python
ALLOWED_HOSTS = ['127.0.0.1']
```
* проверяем работу Django на локальной машине
```
python manage.py runserver 127.0.0.1:8000
```
* заливаем зависимости в файл
```
pip freeze -> requirements.txt
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
* чтобы создались все таблицы в том числе административные нужно провести миграции
```
python manage.py makemigrations
```
```
python manage.py migrate
```
* создаем суперпользователя
```
python manage.py shell
```
```
from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='adin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')
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

