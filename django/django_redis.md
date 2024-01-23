### Кэширование через Redis
* чтобы отследить результат кэшированием подключаем django-debug-toolbar см. django_debug_toolbar.md
```
sudo apt install redis-server
```
```
pip install django-redis
```
```
pip install django-debug-toolbar
```
```python
if DEBUG:
    INTERNAL_IPS = [
        "192.168.1.4",
        "127.0.0.1",
    ]
```
* проверка статуса redis на машине
```
sudo systemctl status redis
```
* остановить redis на машине
```
sudo systemctl stop redis
```

* указываем для Django тот backend, который используется в качестве кеш-системы
```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
```
* Типы кеширования в Django
```
1. Кеширование всего сайта.
2. Кеширование результата, относящегося к обработке запроса контроллером.
3. Кеширование внутри шаблона.
4. Низкоуровневое API для кеширования значений.
Кеширование всего сайта хоть и возможно, но не несёт практической пользы, поскольку в таком случае сайт становится полностью статичным. Если требуется использовать кеш всего сайта, стоит рассмотреть вариант перехода на генераторы статических сайтов.
```
* Кэшируем работу CBV контроллера на 300 секунд
```python
from django.views.decorators.cache import cache_page

path("courses/", cache_page(60 * 5)(views.CoursesListView.as_view()), name="courses",)
```
* Кэшируем шаблон на 300 секунд
```
{% load static cache %}
{% cache 300 lessons %}
	{% for item in lessons %}
		{{ item }}
	{% endfor %}
{% endcache %}
```
* Кэшируем данные внутри контроллера
* Кеширование, независимо от используемого бэкенда (будь до Redis или Memcashed), выполняется через объект cache из пакета django.core.cache. Основные методы взаимодействия с кешем:
```python
cache.get(“<key>”) — для получения значения;
cache.set(“<key>”, “<value>”) — для установки значения.
```
```
Дополнительно в метод set для установки времени хранения значения передаётся именованный
параметр timeout. По умолчанию это значение устанавливается из конфигурации проекта
DEFAULT_TIMEOUT и если оно не задано вручную, то равно 30 секундам.
```
```python
class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):

		cached_feedback = cache.get(f"feedback_list_{pk}") #проверяем есть ли кэш
			if not cached_feedback:
			    context["feedback_list"] = (
			        mainapp_models.CourseFeedback.objects.filter(course=context["course_object"])
			        .order_by("-created", "-rating")
			        .select_related()
			    )
			    cache.set(f"feedback_list_{pk}", context["feedback_list"], timeout=300)  # кэшируем на 300 сек.
			else:
			    context["feedback_list"] = cached_feedback

			return context
```
* открыть консоль
```
redis-cli
```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
