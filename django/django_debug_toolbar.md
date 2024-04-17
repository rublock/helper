### Django Debug Toolbar
```
Так как Django Debug Toolbar считается вспомогательным инструментом, надо указать внутренние
сетевые адреса, с которых открывается доступ к его возможностям.
```
* config/settings.py
```python
if DEBUG:
    INTERNAL_IPS = [
        "192.168.1.4",
        "127.0.0.1",
    ]

    def show_toolbar(request):
        return True


    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    }
```
```python
INSTALLED_APPS = [
	"debug_toolbar",
]
```
```python
MIDDLEWARE = [
	"debug_toolbar.middleware.DebugToolbarMiddleware",
]
```
* config/urls.py
```python
if settings.DEBUG:
	urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
