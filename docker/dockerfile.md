### работа с Dokerfile
* Dockerfile для Django проекта
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
