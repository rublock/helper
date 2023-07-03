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
 ```source venv/bin/activate```запуск виртуального окружения
 ```virtualenv -p /usr/bin/python3.10 venv```установка питона в окружение
 ```deactivate```отключить виртуальное окружение

# Django
 ```pip install --no-cache-dir 'Django<[version]'```установка Django
 ```pip install -r requirements.txt```устновка зависимостей
 ```pip freeze > requirements.txt```экспорт зависимостей
 ```python -m pip uninstall [name]```удаление зависимости
 ```django-admin startproject config .```установка файлов приложения
 ```python manage.py startapp mainapp```создание приложения
 ```run and debug``` => ```create a launch.json``` => ```Django``` => ```args: [ "runserver", "0.0.0.0:8000" ]```настройка отладчика
 ```INSTALLED APPS``` в ```settings.py```добавить созданое приложение ```mainapp```
 ```urls.py``` – создаем в нашем приложении ```mainapp```
 ```from mainapp.apps import MainappConfig app_name = MainappConfig.name```в ```urls.py``` в ```mainapp```
 ```path('', include('mainapp.urls')),```в корневом ```urls.py```
 ```path("", views.MainPageView.as_view(), name="home"),```в ```urls.py``` приложения
 ```class MainPageView(TemplateView): template_name = "mainapp/base.html"```во ```views.py```
 ```STATICFILES_DIRS = [BASE_DIR / 'static',]```в файле ```settings.py``` , создаем папку ```static``` в корне
 ```src="/static/img/logo.png"```пример загрузки статичного файла 

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

# Git
 ```cd ~/.ssh | ls -lah``` – проверить есть ли ssh ключи на компьютере
 ```ssh-keygen -t ed25519 -C "your_email@example.com"”``` – сгенерировать ssh ключ 
 ```cd .ssh/```переходим в каталог с ssh ключами
 ```cat ./id_ed25519.pub``` – копируем ключ и вставляем на GitHub
 ```git config --global user.email "hypermail@yandex.ru"```добавляем почту
 ```git config --global user.name "rublock"```добавляем пользователя
 ```git clone [git link]``` – скопировать репозиторий с Git через ssh
 ```git checkout -b [yourbranchname]```создать ветку и переключиться
 ```git stash -u``` – удаляет все локальные изменения
 ```git add . && git commit -am [commit_text]``` – добавить все файлы и закомитить
 ```git push -u origin master``` – создать такую же ветку на уд. реп. и отправить
 ```git branch -d [local_branch_name]``` – удалить локальную ветку
 ```git reset HEAD~1``` – удалить последний коммит в локальной ветке
 ```git push --set-upstream origin [local_branch_name]```пуш если нет такой ветки на удаленном репозитории
 ```git reset --hard origin/[branch_name]``` – вернуться в состояние удаленной ветки 
 ```git log --oneline```вывести все коммиты

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
