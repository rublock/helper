### Интернационализация
```
Django «из коробки» предоставляет удобный инструмент для внедрения множества языков — систему
интернационализации. Однако он основывается на утилите gettext. Поэтому для его корректной
работы надо установить соответствующую программу.
```
```
sudo apt-get install gettext
```
```
Для создания перевода в Python-файлах надо импортировать функции для перевода как символ _
(подчёркивание; underscore), а затем в коде указать в качестве входного параметра слово для
перевода.
```
* например
```python
from django.utils.translation import gettext_lazy as _

class CourseFeedback(models.Model):
	course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name=_("Course"))
```
* Чтобы использовать локализацию в шаблонах, надо загрузить тег translate из модуля i18n.
```
{% load static i18n %}

{% translate "News" %}
```
* Чтобы сгенерировать файл, где соотносится оригинал и перевод, требуется поддержка в
операционной системе, соответствующей локали (locale).
* проверить какие локали поддерживаются ОС
```
locale -a
```
* добавить локали
```
sudo locale-gen ru_RU
sudo locale-gen ru_RU.UTF-8
```
* обновить локали
```
sudo update-locale 
```
* поиск русских локалей
```
locale -a | grep ru
```
* Добавим дополнительную настройку — указание, где сгенерируются файлы для перевода (фрагмент
файла):
* config/settings.py
```python
LOCALE_PATHS = [BASE_DIR / "locale"]
```
```
mkdir locale
```
* Генерация файлов локализации осуществляется командой:
```
django-admin makemessages -l ru
```
* locale/ru/LC_MESSAGES/django.po
```
После этого в папках приложений проекта и корневой папке внутри locale появится папка локализации
ru, куда войдёт папка LC_MESSAGES. В ней будет основной файл django.po. Все локализуемые
строки указываются в определённом формате:

●верхняя строка — указание на место, где использована локализация;
●средняя строка (параметр msgid) — локализованное слово или выражение;
●нижняя строка (параметр msgstr) — локализация (перевод).
```
* Файл с локализацией надо сделать бинарным, то есть скомпилировать. Для этого выполним команду:
```
django-admin compilemessages
```
```
Для переключения языков в Django используется специальный адрес из пакета интернационализации.
```
* config/urls.py
```python
path("i18n/", include("django.conf.urls.i18n")),
```
* в шаблоне
```html
<div class="row justify-content-end m-0">
	<div class="col p-0 border-right">
	  <form action="{% url 'set_language' %}" method="post">
	  {% csrf_token %}
	    <input name="language" type="hidden" value="ru">
	    <button type="submit" class="btn btn-link">🇷🇺</button>
	  </form>
	</div>
	<div class="col p-0 border-left">
	  <form action="{% url 'set_language' %}" method="post">
	  {% csrf_token %}
	  <input name="language" type="hidden" value="en">
	  <button type="submit" class="btn btn-link">🇬🇧</button>
	  </form>
	</div>
</div>
```
```html
<a class="nav-link" href="{% url 'mainapp:news' %}">{% translate "News" %}</a>
```
* config/settings.py
```python
MIDDLEWARE = [
	"django.middleware.locale.LocaleMiddleware",
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
