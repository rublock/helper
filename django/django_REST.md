### Django REST Framework

##### Базовое представление

```
pip install djangorestframework
```
* core/settings.py
```python

INSTALLED_APPS = [
	'rest_framework',
	]
	

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated", #only for auth users
    ],
}
```
```
python manage.py startapp mainapp_api
```
* config/urls.py
```python
path("api/", include("mainapp_api.urls")),
path("api-auth/", include("rest_framework.urls")),
```
* mainapp_api/
```
touch serializers.py
```
```python
from rest_framework import serializers
from mainapp.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created",
        )
        model = Post

```
##### Общие представления на основе классов
* https://www.django-rest-framework.org/api-guide/generic-views/
* mainapp_api/views.py
```python
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```
##### Pagination
* mainapp_aip/views.py
```python
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination #NEW
```
##### Документация OpenAPI
```
pip install drf-spectacular
```
```python
INSTALLED_APPS = [
    'drf_spectacular',
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema', # new
}
```
* добавляем метаданные
* core/settings.py
```python
SPECTACULAR_SETTINGS = {
    "TITLE": "Blog API Project",
    "DESCRIPTION": "A sample blog to learn about DRF",
    "VERSION": "1.0.0",
}
```
```
python manage.py spectacular --file schema.yml
```
* mainapp_api/urls.py
```python
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui")
]
```
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
