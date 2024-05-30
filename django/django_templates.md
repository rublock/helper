# Шаблоны Django
```
mkdir templates
```
* проверяем пусть к шаблонам
* config/settings.py
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # указываем путь к каталогу с шаблонами
        # ...
    },
]
```
* templates/mainapp/base.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>hello world</p>
</body>
</html>
```
* во views.py
```python
from django.shortcuts import render

def base_page(request):
    return render(request, "mainapp/base.html")
```
```
cd mainapp && touch urls.py
```
```python
from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.base_page),
]

other_urlpatterns = [
    path("", views.base_page2),
]

urlpatterns += other_urlpatterns
```
* или через функцию include
```python
from django.urls import path, include
from blog import views

product_patterns = [
    path("", views.products),
    path("top/", views.top),
]

urlpatterns = [
    path("", views.index),
    path("products/", include(product_patterns)),
]

#http://127.0.0.1:8000/products/top/
```
* в config/urls.py
```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainapp.urls")),
]
```
### Маршрутизация в шаблонах
* задаем имена адресов в urls.py
```python
from django.urls import path, include
from blog import views

product_patterns = [
    path("", views.products, name='products'),
    path("top/", views.top, name='top'),
]
```
* в шаблонах вместо ссылки прописываем
```python
{% url 'mainapp:products' %}
{% url 'mainapp:top' %}
```
### Расширение шаблонов (блок content)
* создаем базовый шаблон mainapp/templates/mainapp/base.html
```
cd templates/mainapp && touch base.html
```
```
<header>
</header>
{% block content %} {% endblock content %}
```
```
cd templates/mainapp && touch home_page.html
```
```
{% extends "base.html" %}
{% block content %}
{% load static %}
    <h1>Главная страница</h1>
{% endblock content %}
```
```python
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates/mainapp'),],
    }
```
### Работа с данными в шаблоне через Function Based View
* забираем данные от клиента через параметр
```
http://localhost:8000/?data=some_data
```
```python
from django.shortcuts import render

def home_page(request):
    data = request.GET.get("data")
    print(data) #some_data
    return render(request, "mainapp/base_page.html")
```
* забирем числовое значение через http адрес
```
http://localhost:8000/123
```
* mainapp/views.py
```python
def get_int(request, pk):
    print(pk) #123
    return render(request, "mainapp/home_page.html")
```
* mainapp/urls.py
```python
urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("<int:pk>", views.get_int, name="get_int"),
]
```
* передаем контекст в шаблон
```python
def home_page(request):
    data = request.GET.get("data")
    print(data) #some_data
    context = {
        "data": data,
    }
    return render(request, "mainapp/base_page.html", context)
```
* в шаблоне
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>hello world</p>
    {{ data }}
</body>
</html>
```
* запускаем
```
http://localhost:8000/?data=some_data
```
* вывод
```
hello world

some_data
```
### Контекстные процессоры (данные для всех шаблонов сразу)
- mainapp/context_processors/context.py
```python
def title(request):
return {"foo": "bar"}
```
- config/settings.py
```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "mainapp.context_processors.context.title", #new
            ],
        },
    },
]
```
### Циклы в шаблонах
```html
<ul>
    {% for i in data %}
        <li>{{ i }}</li>
    {% endfor %}
</ul>
```
* цикл с уловием
```html
<ul>
    {% for i in data %}
        {% if i > 5 %}
            <li>{{ i }}</li>
        {% endif %}
    {% endfor %}
</ul>
```
### Пагинация в шаблонах
* mainapp/views.py
```python
from django.core.paginator import Paginator

content = [str(i) for i in range(1000)]

def pagination(request):
    page_num = int(request.GET.get('page', 1))
    pag = Paginator(content, 10)
    page = pag.get_page(page_num)
    context = {
        "page": page,
    }
    return render(request, 'mainapp/base_page.html', context)
```
* mainapp/urls.py
```python
urlpatterns = [
    path("", views.pagination, name="pagination"),
]
```
* в шаблоне
```html
{% for i in page %}
    {{ i }}
{% endfor %}
<br>
{% if page.has_previous %}
    <a href='?page={{ page.previous_page_number }}'> << </a>
{% endif %}

{% for i in page.paginator.page_range %}
    {% if page.number == i %}
        <a href='?page={{ i }}'> {{ i }} </a>
    {% elif i > page.number|add:'-3' and i < page.number|add:'3' %}
        <a href='?page={{ i }}'> {{ i }} </a>
    {% endif %}
{% endfor %}

{% if page.has_next %}
    <a href='?page={{ page.next_page_number }}'> >> </a>
{% endif %}
```
### Шаблонные фильтры
* создадим шаблонный фильтр для вставки e-mail адреса
```
mkdir mainapp/templatetags/ && cd mainapp/templatetags/ && touch email_to_link.py
```
```python
from django import template
from django.utils.safestring import mark_safe


register = template.Library()
@register.filter
def email_to_link(value):
	return mark_safe(f"<a href='mailto:{value}'>{value}</a>")
```
```
register = template.Library() создает объект реестра тегов и фильтров, через который они будут
проходить регистрацию для их применения в шаблоне
●
@register.filter — декоратор регистрации шаблонного тега\фильтра. У него есть опциональный
именованный параметр name, который позволяет задать другое имя. По умолчанию
тег\фильтр берёт имя функции, к которой применен декоратор
●
def email_to_link(value) — определение функции. Имеет обязательный позиционный параметр,
в который помещается значение объекта, к которому применен фильтр.
●
return mark_safe(f"<a href='mailto:{value}'>{value}</a>") - функция mark_safe помечает
содержимое строки как безопасное для использования в верстке. В ином случае вместо
многих символов будет использована их версия в виде символов-мнемоник.
```
* в шаблоне
```
{% load email_to_link %}

<li><strong>{{ 'example@mail.ru'|email_to_link }}</strong></li>
```
### Контекстные процессоры
* нужны для того чтобы получать данные во всех шаблонах сразу
```
mkdir -p mainapp/context_processors/ && touch mainapp/context_processors/__init__.py && touch mainapp/context_processors/example.py
```
```python
def simple_context_processor(request):
    return {"foo": "bar"}
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
