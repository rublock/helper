# Django

* инициализируем репозиторий на github.com
* клонируем репозиторий
```
git clone
```
* устанавливаем pip
```
sudo -H pip3 install --upgrade pip
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
python manage.py runserver 0.0.0.0:8000
```
* фиксируем имзенения на github
```
git add . && git commit -am "Initial commit"
```
* переходим на dev ветку
```
git checkout -b 'dev'
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
## Создаем простейшее представление
* в config/urls.py
```python
from django.contrib import admin
from django.urls import path

from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
]
```
* в mainapp/views.py
```python
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('This is home page!')
```
* пользователь зайдет на главную страницу urls.py это зафиксирует и запустит home_page() во вьюхе, та в свою очередь отправит HttpResponse('This is home page!')
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

