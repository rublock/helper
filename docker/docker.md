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
```docker
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
