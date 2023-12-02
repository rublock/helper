### Деплой проекта на VDS севере через docker-compose
* обновим список пакетов
```
sudo apt update
```
* обновим и сами установленные пакеты
```
sudo apt upgrade -y
```
```
sudo reboot
```
* установим несколько дополнительных пакетов, которые позволят менеджеру пакетов APT использовать HTTPS
```
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
```
* docker и docker-compose должны быть уже установленны
* клонируем репозиторий и переходим в папку проекта
```
nano .env.prod
```
```python
DJANGO_ALLOWED_HOSTS = 'имя_вашего_домена'
CSRF_TRUSTED_ORIGINS = 'http://имя_вашего_домена https://имя_вашего_домена'
```
```
cd nginx && nano htmx_book.conf
```
* server_name имя_вашего_домена;
```
cd ..
```
* запустим процесс создания образов
```
docker compose -f docker-compose.prod.yml build
```
* создадим и запустим контейнеры
```
docker compose -f docker-compose.prod.yml up -d
```
* выполним миграции
```
docker compose -f docker-compose.prod.yml exec web python manage.py migrate --no-input
```
* соберем статические файлы
```
docker compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input
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
