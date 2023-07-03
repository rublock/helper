# VScode
построить код
`
ctrl + Shift + I
`

закрыть все вкладки
`
ctrl + k w
`

терминал 
`
ctrl + ` 
`

в правом нижнем углу, выбрать интерпретатор проекта из виртуального окружения 
```
/venv/bin/python
```

# venv linux
установка программы
```
sudo pip install virtualenv
```
создание окружения
```
virtualenv venv
```
запуск виртуального окружения
```
. venv/bin/activate
```
установка питона в окружение
```
virtualenv -p /usr/bin/python3.10 venv
```
отключить виртуальное окружение
```
deactivate
```

# Git
проверить есть ли ssh ключи на компьютере
```
cd ~/.ssh | ls -lah
```
сгенерировать ssh ключ
```
ssh-keygen -t ed25519 -C "your_email@example.com"”
```
переходим в каталог с ssh ключами
```
cd .ssh/
```
копируем ключ и вставляем на GitHub
```
cat ./id_ed25519.pub
```
добавляем почту
```
git config --global user.email "hypermail@yandex.ru"
```
добавляем пользователя
```
git config --global user.name "rublock"
```
скопировать репозиторий с Git через ssh
```
git clone [git link]
```
создать ветку и переключиться
```
git checkout -b [yourbranchname]
```
удаляет все локальные изменения
```
git stash -u
```
добавить все файлы и закомитить
```
git add . && git commit -am [commit_text]
```
создать такую же ветку на удаленном репозитории и отправить
```
git push -u origin master
```
удалить локальную ветку
```
git branch -d [local_branch_name]
```
удалить последний коммит в локальной ветке
```
git reset HEAD~1
```
пуш если нет такой ветки на удаленном репозитории
```
git push --set-upstream origin [local_branch_name]
```
вернуться в состояние удаленной ветки
```
git reset --hard origin/[branch_name]
``` 
вывести все коммиты
```
git log --oneline
```


# Django
установка Django
```
pip install --no-cache-dir 'Django<[version]'
```
устновка зависимостей
```
pip install -r requirements.txt
```
экспорт зависимостей
```
pip freeze > requirements.txt
```
удаление зависимости
```
python -m pip uninstall [name]
```
установка файлов приложения
```
django-admin startproject config .
```
создание приложения
```
python manage.py startapp mainapp
```
настройка отладчика
```
run and debug => create a launch.json => Django => args: [ "runserver", "0.0.0.0:8000" ]
```
добавить созданое приложение mainapp
```
INSTALLED APPS в settings.py
```
создаем в нашем приложении mainapp
`
urls.py
`

пример загрузки статичного файла в корневом urls.py
```
from mainapp.apps import MainappConfig 

app_name = MainappConfig.nameв urls.py
```
в mainapp
```
path('', include('mainapp.urls')),
path("", views.MainPageView.as_view(), name="home"),
```
во views.py
```
class MainPageView(TemplateView): 
    template_name = "mainapp/base.html"
```
создаем папку static в корне и прописываем в файле settings.py
```
STATICFILES_DIRS = [BASE_DIR / 'static',] , 
src="/static/img/logo.png"
``` 

```python manage.py makemigrations```создать файлы миграций
```python manage.py migrate```миграции базы данных
```python manage.py migrate mainapp [last migration]```откат миграции
```python manage.py createsuperuser```создать супер пользователя
```python manage.py changepassword [nick name]```изменить пароль супер пользователя
```python manage.py runserver```- запуск сервера
```python manage.py collectstatic```сбор статики
```python manage.py shell```для выполнения запросов и тестирования фрагментов кода

# RAR linux
```unrar x [file_name]```распаковать архив в одноименную папку
```unrar l [file_name]```просмотреть содержимое архива
```rar [file_name] [dir_name]```заархивировать папку 



# Docker
```sudo docker images```показать все образы
```sudo docker ps -a```показать все запущенные образы
```sudo docker pull [imagename:version]```скачать образ
```sudo docker rmi [imagename:version]```удалить образ
```sudo docker run [imagename:version]```запустить образ
```sudo docker run -it [imagename:version]```запустить образ + открыть терминал
```sudo docker stop [NAME]```остановить образ
```sudo docker rm [NAME]```удалить существующий образ образ, но не удалять сам файл образа
```sudo docker start [NAME]```запустить существующий образ
```sudo docker exec -it [NAME] bash```зайти в контейнер используя bash
