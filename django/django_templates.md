# Шаблоны Django
```
cd mainapp && mkdir templates && cd templates && mkdir mainapp && cd mainapp && touch base.html
```
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
    path("", views.base_page, name="base_page"),
]
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
### блоки content
* mainapp/templates/mainapp/base.html
```
<header>
</header>
{% block content %} {% endblock content %}
```
```
cd mainapp/templates/mainapp && touch home_page.html
```
```
{% extends "base.html" %}
{% block content %}
    <h1>Главная страница</h1>
{% endblock content %}
```







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
* цикл в шаблоне
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
