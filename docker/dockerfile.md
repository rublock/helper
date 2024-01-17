### Dokerfile

#### Dockerfile на примере Django
```
FROM python:3.12.0-alpine

LABEL author=mack
LABEL type=django

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
	pip install --upgrade pip && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["echo"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```
> * FROM python:3.12.0-alpine - Устанавливает базовый образ, из которого будет создан контейнер Docker
> * LABEL - описание которое можно посмотреть через docker image inspect
> * WORKDIR /usr/src/app - Устанавливает рабочий каталог внутри контейнера, при запуске контейнера сразу туда переходим
> * ENV PYTHONDONTWRITEBYTECODE 1 - Переменная окружения не позволяет Python копировать файлы .pyc в контейнер
> * ENV PYTHONUNBUFFERED 1 - Переменная окружения гарантирует, что вывод Python регистрируется в терминале, что позволяет отслеживать журналы Django в режиме реального времени, переменные окружения можно создавать новые и переопределять при запуске контейнера
> * RUN pip install --upgrade pip - Устанавливает и обновляет версию pip, которая находится в контейнере
> * COPY ./requirements.txt . - Копирует requirements.txt файл в рабочий каталог в контейнере
> * RUN pip install -r requirements.txt - Устанавливает все необходимые модули проекта для запуска в контейнере
> * COPY . . - Копирует весь исходный код проекта в рабочий каталог в контейнере
> * EXPOSE 8000 - Предоставляет порт 8000 для доступа из других приложений
> * ENTRYPOINT - Неизменяемые комманды, выполяются в любом случае
> * CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] - Изменяемые комманды при запуске контейнера, т.е. при запуске контейнера можно переопределить данную комманду например (docker run --name [container_name] [image_name] python manage.py migrate) - выполнитеся именно migrate, а не runserver

* сборка образа
```
docker build --tag [image_name]:latest .
```
* --tag Устанавливает тег для образа. Например, мы создаем образ Docker из python:3.12.0 у него есть тег alpine.
В нашем образе Docker, latest это тег.

#### Dockerfile на примере Nginx
```
FROM ubuntu:22.04

LABEL author=mack

RUN apt-get update && \
	apt-get install nginx -y && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html/

COPY docker_files/index.html .

ENV OWNER=mack

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
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
