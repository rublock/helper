### Логирование в Django
```
Логгер в Python настраивается путём описания конфигурационной структуры в виде словаря. Важные
части этой структуры:

1. Форматтеры (formatters). Эта настройка позволяет определить, как будет выводиться лог.
Можно определить сколько угодно различных правил, выводящих данные в требуемом
формате. Формат составляется с применением атрибутов. Задаётся время, номер строки
вывода, сообщение, уровень лог-сообщения и т. д.
2. Обработчики (handlers). Они определяют способ вывода сообщений. Так настраивается вывод
сообщений в файл, консоль, системный журнал (syslog) и прочее. В обработчиках задаются
форматтеры.
3. Фильтры (filters). Предоставляют возможность более тонкой настройки для пересылки
сообщений лога. Например, если общий поток сообщений идёт в консоль, сообщения о
критических ошибках отправляются по электронной почте.
4. Логгеры. Позволяют настроить способ взаимодейтствия обработчиков и форматтеров для
различных частей системы. Например, для сообщений лога конкретного приложения в Django
задаётся вывод лог-сообщений в файл определённого формата.
```
```
логгеры, которые поставляются в пакете фреймворка Django:

1. django — логгер для всех сообщений Django.
2. django.request — логгер сообщений, связанных с запросами.
3. django.server — логгер сообщений, связанных с обработкой запросов при запуске команды
runserver. Без дополнительной настройки в консоли при запросе какой-либо страницы
отображаются сообщения, которые обрабатываются именно этим логгером.
4. django.template — логгер сообщений, относящихся к отрисовке шаблонов.
5. django.db.backends — логгер сообщений от подсистемы ORM.
6. django.security — логгер сообщений, связанный с подсистемой безопасности.
Дополнительно в Django предоставляется обработчик AdminEmailHandler. Он позволяет отправлять
лог-сообщения администраторам сайта по электронной почте. Это удобно в критических ситуациях,
когда требуется срочное вмешательство обслуживающего персонала.
```
* Уровни сообщений
```
1. CRITICAL. Цифровой эквивалент — 50.
2. ERROR. Цифровой эквивалент — 40.
3. WARNING. Цифровой эквивалент — 30.
4. INFO. Цифровой эквивалент — 20.
5. DEBUG. Цифровой эквивалент — 10.
6. NOTSET. Цифровой эквивалент — 0.
```
* config/settings.py
```python
LOG_FILE = BASE_DIR / "var" / "log" / "main_log.log"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "[%(asctime)s] %(levelname)s %(name)s (%(lineno)d) %(message)s"
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
            "formatter": "console",
        },
        "console": {"class": "logging.StreamHandler", "formatter": "console"},
    },
    "loggers": {
        "django": {"level": "INFO", "handlers": ["console"]},
        "mainapp": {
            "level": "DEBUG",
            "handlers": ["file"],
        },
    },
}
```
```
Как читается эта конфигурация:
1. Конфигурация задаётся в виде словаря, значит, при логировании используется конфигуратор
версии 1.
2. Отключения существующих логгеров не произойдёт (disable_existing_loggers).
3. Добавляется новый форматтер с именем console.
4. Для форматтера console задаётся новый формат сообщений: время в стандартном виде
(asctime), уровень приоритета сообщения (levelname), имя модуля, откуда поступило
сообщение (name), номер строки в модуле (lineno), само сообщение (message).
5. В обработчиках (handlers) задаётся новый (обработчик) с именем console.
6. Для обработчика с именем
console задаётся класс вывода потока лог-сообщений
(logging.StreamHandler) и формат потока сообщений (console).
7. Изменяется настройка стандартного логгера django — все лог-сообщения фреймворка.
8. В новом логгере django для всех сообщений начиная с приоритета уровня INFO используется
обработчик console.
Лог-сообщения выводятся не только в стандартный поток вывода, но и, например, в файл.
```
* Логгер не создаёт папки автоматически, поэтому перед запуском проекта надо создать
папки, указанные в переменной LOG_FILE.
```
mkdir -p ./var/log
```
```python
"loggers": {
	"django": {"level": "INFO", "handlers": ["file", "console"]},
},
```
* mainapp/views.py
```python
import logging
logger = logging.getLogger(__name__)

class NewsListView(ListView):
    model = mainapp_models.News
    paginate_by = 5

    def get_queryset(self):
        logger.debug("class NewsListView, def get_queryset log message") #сообщение лога
        return super().get_queryset().filter(deleted=False)
```
* вывод логов на сайт
* mainapp/views.py
```python
class LogView(TemplateView):
    template_name = "mainapp/log_view.html"

    def get_context_data(self, **kwargs):
        context = super(LogView, self).get_context_data(**kwargs)
        log_slice = []
        with open(settings.LOG_FILE, "r") as log_file:
            lines = log_file.readlines()
            for line in reversed(lines[-1000:]): #последние 1000 строк
                log_slice.insert(0, line)
            context["log"] = "".join(log_slice)
        return context


class LogDownloadView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, *args, **kwargs):
        return FileResponse(open(settings.LOG_FILE, "rb"))
```
* mainapp/urls.py
```python
path("log_view/", views.LogView.as_view(), name="log_view"),
path("log_download/", views.LogDownloadView.as_view(), name="log_download"),
```
```
touch mainapp/templates/mainapp/log_view.html
```
```html
{% extends 'base.html' %}

{% block content %}
<div class="row justify-content-end my-2">
  <div class="col-sm-4 col-lg-2">
    <a href="{% url 'mainapp:log_download' %}" class="btn btn-primary btn-block"
      role="button">Скачать</a>
  </div>
</div>
<p>
<div class="text-center text-muted"><small>Last 1000 lines of log file</small></div>
<pre>{{ log }}</pre>
</p>
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
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
