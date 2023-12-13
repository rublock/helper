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
* получаем данные из адресной строки
```python
from mainapp import models as mainapp_models

class HomePageDetailView(TemplateView):
    template_name = "mainapp/home_page_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["data"] = get_object_or_404(mainapp_models.HomeDetail, pk=pk)
        return context

```
* в mainapp/urls.py
```python
path("news/<int:pk>/", views.HomePageDetailView.as_view(), name="home_page_detail"),
```
* в шаблоне 
```
{% for i in data %}
    <a href="{% url 'mainapp:home_page_detail' pk=i.pk %}" class="card-link">Подробнее</a>
{% endfor %}
```
### Контроллеры CBV CRUD
* создаем контроллер добавления новости
```python
class NewsCreateView(PermissionRequiredMixin, CreateView):
    template_name = "mainapp/news_form.html"

    model = mainapp_models.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.add_news",)
```
* прописываем пути
```python
path("news/create/", views.NewsCreateView.as_view(), name="news_create"),
```
* шаблон формы с использованием crispy
```html
{% extends 'base.html' %}
{% load crispy_forms_tags %}

{% block content %}
<div class="row justify-content-center pt-3">
  <div class="col-md-12 col-lg-8">
    <form method="post">
      {% csrf_token %}
      {{ form|crispy }}
      <button type="submit"
        class="btn btn-primary btn-block">Опубликовать</button>
    </form>
  </div>
</div>
{% endblock content %}
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

