# Docker

### Установка Docker через скрипт

```
sudo apt update
```
```
curl -fsSL https://get.docker.com -o get-docker.sh
```
```
sudo sh get-docker.sh
```
* проверка
```
sudo systemctl status docker
```
* верисия
```
docker -v
```
* добавляем пользователя в группу Docker чтобы не писать sudo
```
sudo groupadd docker && sudo usermod -aG docker [user_name] && newgrp docker
```

### Работка с Docker

показать все образы
```
sudo docker images
```
скачать образ из репозитория
```
sudo docker pull [image_name]
```
удалить образ (перед этим нужно остановить контейнер этого образа)
```
sudo docker rmi [image_name]
```
запустить образ (создать контейнер) -d запустить в фоне
```
sudo docker run -p 8000:8000 --rm --name [container_name] -d [image_name]
```
показать все контейнеры
```
sudo docker ps -a
```
остановить контейнер
```
sudo docker stop [container_name]
```
перезагрузить контейнер
```
sudo docker restart [options] [container_name]
```
удалить контейнер
```
sudo docker rm -f [container_name]
```
зайти в контейнер и открыть терминал
```
docker exec -it [container_name] /bin/bash
```
* открыть интерактивную сессию в контейнере
```
docker attach [options] [container_name]
```
* логи контейнера
```
docker logs [container_name]
```
* удалить все в докере
```
docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q) && docker rmi $(docker images -q)
```
* базовая инструкция для Django проекта
```
touch Dockerfile
```
```
# pull the official base image
FROM python:3.12.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```
* FROM python:3.12.0-alpine: Устанавливает базовый образ, из которого будет создан контейнер Docker.
* WORKDIR /usr/src/app: Устанавливает рабочий каталог внутри контейнера в/usr/src/app.
* ENV PYTHONDONTWRITEBYTECODE 1: Не позволяет Python копировать файлы .pyc в контейнер.
* ENV PYTHONUNBUFFERED 1: Гарантирует, что вывод Python регистрируется в терминале, что позволяет отслеживать журналы Django в режиме реального времени.
* RUN pip install --upgrade pip: Устанавливает и обновляет версию pip, которая находится в контейнере.
* COPY ./requirements.txt /usr/src/app: Копирует requirements.txt файл в рабочий каталог в контейнере.
* RUN pip install -r requirements.txt: Устанавливает все необходимые модули проекта для запуска в контейнере.
* COPY . /usr/src/app: Копирует весь исходный код проекта в рабочий каталог в контейнере.
* EXPOSE 8000: Предоставляет порт 8000 для доступа из других приложений.
* CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]: Устанавливает исполняемые команды в контейнере.

* сборка образа
```
docker build --tag [image_name]:latest .
```
* --tag Устанавливает тег для образа. Например, мы создаем образ Docker из python:3.12.0 у него есть тег alpine.
В нашем образе Docker, latest это тег.

* создание контейнера
```
docker run --name [container_name] -d -p 8000:8000 [image_name]:latest
```
* --name: Устанавливает имя контейнера Docker.
* -d: Заставляет образ работать  в фоновом режиме.
* -p 8000:8000: Сопоставляет порт 8000 в контейнере Docker с портом 8000 на локальном хосте.
* image_name:latest Указывает, какой образ используется для сборки контейнера Docker.
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
