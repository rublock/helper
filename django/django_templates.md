# Шаблоны Django
```
cd mainapp && mkdir templates && cd templates && mkdir mainapp && cd mainapp && touch home_page.html
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

def home_page(request):
    return render(request, "mainapp/home_page.html")
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
    path("", views.home_page, name="home_page"),
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
* забираем данные от клиента через параметр
```
http://localhost:8000/?data=some_data
```
```python
from django.shortcuts import render

def home_page(request):
    data = request.GET.get("data")
    print(data) #some_data
    return render(request, "mainapp/home_page.html")
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
    return render(request, "mainapp/home_page.html", context)
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
