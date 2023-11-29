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
запустить образ (сделать контейнер)
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
удалить контейнер
```
sudo docker rm -f [container_name]
```
зайти в контейнер и открыть терминал
```
docker exec -it [container_name] /bin/bash
```
* логи контейнера
```
docker logs [container_name]
```
* удалить все в докере
```
docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q) && docker rmi $(docker images -q)
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
