* в шаблон перед тэгом !DOCTYPE html
```
{% load static %}
```
```
mkdir static
```
* config/settings.py
```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```
```
<head>
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
</head>
```
```
<body>
    <script src="{% static 'js/app.js' %}"></script>
</body>
```
* медиа файлы для загрузки пользователем (аватраки и т.д.)
```python
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"
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
