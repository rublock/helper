### Function based view
```python
from django.shortcuts import render

def base_page(request):
    return render(request, "mainapp/base.html")
```
### Class based view
```python
class MainPageView(TemplateView):
    template_name = "mainapp/index.html"
```
* передаем данные в шаблон
```python
class HomePageView(TemplateView):
    template_name = "mainapp/home_page.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["datetime_obj"] = datetime.now()
        return context
```
* в mainapp/urls.py
```python
path("", views.HomePageView.as_view(), name="home_page"),
```
* в шаблоне
```
{{ datetime_obj }}
```
* получаем данные из адресной строки
```python
class HomePageView(TemplateView):
    template_name = "mainapp/home_page.html"

    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context
```
* в mainapp/urls.py
```python
path("<int:page>/", views.HomePageView.as_view(), name="home_page")
```
* в шаблоне можно передать данные ввиде ссылки
```
href="{% url 'mainapp:home_page' page=1 %}"
```
* получаем данные из БД и передаем в шаблон
```python
from mainapp import models as mainapp_models

class HomePageView(TemplateView):
    template_name = "mainapp/home_page.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = mainapp_models.Home.objects.all()
        return context
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

