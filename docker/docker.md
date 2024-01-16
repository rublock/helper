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
* логи контейнера
```
docker logs -f [container_name]
```
> * -f - логи в режиме реального времени

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
docker run --name [container_name] -d -p 8080:80 [image_name]:[image_version]
```
> * --name - устанавливает имя контейнера Docker
> * -d - заставляет образ работать  в фоновом режиме
> * -p 8080:80 - сопоставляет порт 80 в контейнере Docker с портом 8080 на локальном хосте,
> можно пробрасывать большее количество портов
> * image_name:latest - указывает, какой образ используется для сборки контейнера Docker

### Переменные окружения
```
docker run --name [container_name] -e MYSQL_ROOT_PASSWORD=[password] -d mysql
```
> * -e - переменная окружения которая будет лежать в контейнере

* посмотреть все переменные окружения на машине или в контейнере
```
env
```

### Docker Volumes (сохраняющиеся данные)
* посмотреть все volumes
```
docker volume ls
```
* удалить volume
```
docker volume rm [volume_name]
```
* Host Volumes
```
docker run -v /opt/mysql_data:/var/lib/mysql:ro mysql
```
> * /opt/mysql_data - данные на сервере
> *	/var/lib/mysql - данные в docker контейнере
> * :ro - права только на чтение (read only)

* пример с nginx
* создаем папку на сервере
```
sudo mkdir /opt/nginx/data
```
```
docker run --name nginx_container -p 80:80 -v /opt/nginx/data:/usr/share/nginx/html -d nginx
```
```
cd /opt/nginx/data && sudo nano index.html
```
> * index html будет транслироваться nginx-ом в барузер по ip

* Named Volumes
```
docker run -v mysql_data:var/lib/mysql mysql
```
> * mysql_data - создается папка на сервере var/lib/docker/volumes/mysql_data/_data
> *	/var/lib/mysql - данные в docker контейнере

* пример с nginx
```
docker run --name nginx_container -p 80:80 -v web_data:/usr/share/nginx/html -d nginx
```
```
cd /var/lib/docker/volumes/web_data/_data && sudo nano index.html
```
> * возможно потребуется дать права для папки docker
```
sudo chmod -R 777 docker/
```

### Docker Networks (сетевые настройки)
* посмотреть список сетей
```
docker network ls
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
* тип сети bridge
> * такой тип сети создается поумолчанию когда мы вводим docker run
> * ip - 172.17.0.0/16
> * /16 - указывает на то, что первые 16 битов адреса составляют сетевую часть, а оставшиеся 16 битов - хостовую часть. Это означает, что данная подсеть имеет маску подсети 255.255.0.0 и включает в себя диапазон IP-адресов от 172.17.0.0 до 172.17.255.255
> * контейнеры в сети bridge могут общаться по DNS именам, т.е. по именам самих контейнеров
> * если создать еще одну сесть, то разные сети не смогут общаться между собой (изоляция)
* создать новую сеть типа bridge
```
docker network create --drive bridge [network_name]
```
* запустить контейнер в созданной сети
```
docker run --net [network_name] [image_name]:[image_version]
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
* тип сети host
> * используется ip адрес сервера (хоста)
```

```
* тип сети none
> * нельзя никак подключиться извне, однако, можно выполнять комманды docker
```

```
* тип сети macvlan
> * каждый контейнер получает свой собственный mac адрес
```

```
* тип сети ipvlan
> * каждый контейнер получает тот же mac адрес что и у сервера
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