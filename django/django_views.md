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
```
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
```
path("", views.HomePageView.as_view(), name="home_page"),
```
* в шаблоне
```
{{ datetime_obj }}
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

