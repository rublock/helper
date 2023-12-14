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
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
