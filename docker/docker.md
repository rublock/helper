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
service docker status
```
* верисия
```
docker -v
```
* добавляем пользователя в группу Docker чтобы не писать sudo
```
sudo usermod -aG docker [user_name] && reboot
```

### Работка с Docker

* показать все образы
```
docker images
```
* скачать образ из репозитория
```
docker pull [image_name]
```
* создать контейнер из образа (если нет локально, то скачает с dockerhub версию latest)
```
docker run [image_name]
```
* создать контейнер из образа и поставить в спящий режим, чтобы он не закрылся
```
docker run [image_name] sleep [sec]
```
* удалить образ (перед этим нужно остановить контейнер этого образа)
```
docker rmi [image_name]
```
* показать все контейнеры
```
docker ps -a
```
* остановить контейнер
```
docker stop [container_name]
```
* перезагрузить контейнер
```
docker restart [options] [container_name]
```
* удалить контейнер
```
docker rm -f [container_name]
```
* удалить все в докере
```
docker stop $(docker ps -a -q) && docker system prune -a --volumes
```
* зайти в контейнер и открыть терминал
```
docker exec -it [container_name] /bin/bash
```
* открыть интерактивную сессию в контейнере
```
docker attach [options] [container_name]
```
* логи контейнера
```
docker logs -f [container_name]
```
* -f: логи в режиме реального времени

* посмотреть информацию по контейнеру
```
docker inspect [container_name or id]
```
* узнать сколько ресурсов требует контейнер
```
docker stats [container_name or id]
```

### Порты
* создание контейнера с пробросом портов
```
docker run --name [container_name] -d -p 80:8080 [image_name]:[image_version]
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
