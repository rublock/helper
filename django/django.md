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
* 
```

```
* 
```

```







* устновка зависимостей
```
pip install -r requirements.txt
```
* экспорт зависимостей
```
pip freeze > requirements.txt
```

* удаление зависимости
```
python -m pip uninstall [name]
```

* установка файлов приложения
```
django-admin startproject config .
```

* создание приложения
```
python manage.py startapp mainapp
```

* настройка отладчика
```
run and debug => create a launch.json => Django => args: [ "runserver", "0.0.0.0:8000" ]
```

* добавить созданое приложение mainapp в INSTALLED APPS в файле settings.py
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'corsheaders',
    "mainapp",
    'django.contrib.humanize',
    'mathfilters',
]
```

* создаем в нашем приложении mainapp
`
urls.py
`

* пример загрузки статичного файла в `urls.py` из папки mainapp
```
from mainapp.apps import MainappConfig 

app_name = MainappConfig.nameв urls.py
```

* в `urls.py` из папки mainapp
```
path('', include('mainapp.urls')),
path("", views.MainPageView.as_view(), name="home"),
```

* во views.py
```
class MainPageView(TemplateView): 
    template_name = "mainapp/base.html"
```

* создаем папку static в корне и прописываем в файле `settings.py`
```
STATICFILES_DIRS = [BASE_DIR / 'static',] , 
src="/static/img/logo.png"
```

* создать файлы миграций
```
python manage.py makemigrations
```

* миграции базы данных
```
python manage.py migrate
```

* откат миграции
```
python manage.py migrate mainapp [last migration]
```

* создать супер пользователя
```
python manage.py createsuperuser
```

* изменить пароль супер пользователя
```
python manage.py changepassword [nick name]
```

* запуск сервера
```
python manage.py runserver
```

* сбор статики
```
python manage.py collectstatic
```

* для выполнения запросов и тестирования фрагментов кода
```
python manage.py shell
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

