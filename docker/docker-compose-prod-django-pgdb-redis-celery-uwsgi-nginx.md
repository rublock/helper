### Deployment Django with docker-compose, postgres, redis, celery, uwsgi, nginx
* mk dir app/ - создать в корне проекта и переместить туда все файлы Django приложения кроме requirements.txt
* touch Dockerfile
```
# Взять официальный базовый образ Python с платформы Docker
FROM python:alpine3.19
LABEL maintainer="rublock"

# Задать переменные среды
ENV PYTHONUNBUFFERED 1

# Скопировать код в работчий каталог в образ
COPY ./requirements.txt ./requirements.txt
COPY .app/ .app/

# Задать рабочий каталог
WORKDIR /app
EXPOSE 8000

# Установка python, venv, зависимостей, регистарция пользователя
RUN python -m venv /python && \
    /python/bin/pip install --upgrade pip && \
    /python/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home admin

# Путь к локальному виртуальному окружению
ENV PATH="/python/bin:$PATH"

# Переключаемся на локального пользователя
USER admin
```
* touch .dockerignore
```
# Git
.git
.gitignore

# Docker
.docker

# Python
app/__pycache__/
app/*/__pycache__/
app/*/*/__pycache__/
app/*/*/*/__pycache__/
.env/
.venv/
venv/

# Local PostgreSQL data
data/
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
