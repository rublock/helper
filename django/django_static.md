* в шаблон перед тэгом !DOCTYPE html
```
{% load static %}
```
```
cd mainapp && mkdir static
```
* config/settings.py
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = ('static',)
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
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```
