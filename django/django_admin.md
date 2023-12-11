### Административный раздел

* создать суперпользователя
```
python manage.py createsuperuser
```
* или через оболочку shell
```
python manage.py shell
```
```python
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'admin@example.com', 'admin')
```
* далить суперпользователя
```python
from django.contrib.auth import get_user_model
model = get_user_model()
model.objects.get(username="admin", is_superuser=True).delete()
```
* в шаблоне
```html
{% if user.is_superuser %}
<a href="{% url 'admin:index' %}">Админ</a>
{% endif %}
```
* mainapp/admin.py краткая регистрация модели
```python
from django.contrib import admin
from mainapp import models as mainapp_models


	admin.site.register(mainapp_models.News)
```
или
```python
from django.contrib import admin
from mainapp import models as mainapp_models

	@admin.register(mainapp_models.News)
	class NewsAdmin(admin.ModelAdmin):
		pass
```
```
По умолчанию в административном разделе модель именуется как множество объектов. Имя формируется по стандартному правилу обозначения множественного числа в английском языке путём подстановки постфикса s. Однако в некоторых случаях это правило не работает, например, с моделью новостей News. Множественное и единственное представление этого объекта будет называться одинаково.
```
* чтобы это скорректировать в mainapp/models.py добавляем
```python
class Meta:
	verbose_name = _("News")
	verbose_name_plural = _("News")
	ordering = ("-created",)
```
```
python manage.py makemigrations && migrate
```
* настройка отображения списка объектов
* mainapp/admin.py код класса с настройкой отображаемых атрибутов объектов
```python
@admin.register(mainapp_models.Lesson)
	class LessonAdmin(admin.ModelAdmin):
		list_display = ["id", "num", "title", "deleted"]
```
```
Поля-связи с другими таблицами не позволяют просто вывести значение. Чтобы описать способ вывода этих данных в таблице, надо применить функцию. Для этой функции задаётся дополнительный атрибут short_description, значение которого выводится в качестве заголовка столбца. Имя функции надо занести в список list_display.
```
* mainapp/admin.py
```python
@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):

	list_display = ["id", "get_course_name", "num", "title", "deleted"]

	def get_course_name(self, obj):
		return obj.course.name

	get_course_name.short_description = _("Course")
```
* cортировка
```
В качестве значений задаются имена столбцов. Таблица объектов последовательно сортируется по заданным атрибутам. Сортировка задаётся и по связным полям, что указывается через __ (двойное подчёркивание) и атрибут модели. Инвертирование сортировки задаётся через указание — перед атрибутом.
```
```python
@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
	list_display = ["id", "get_course_name"
	ordering = ["-course__name", "-num"]

	def get_course_name(self, obj):
		return obj.course.name

	get_course_name.short_description = _("Course")
```
* количество объектов на страницу (list_per_page)
```python
class LessonAdmin(admin.ModelAdmin):
	list_display = ["id", "get_course_name", "num", "title", "deleted"]
	ordering = ["-course__name", "-num"]
	list_per_page = 5
```
* добавление фильтров (list_filter)
```python
class LessonAdmin(admin.ModelAdmin):
	list_display = ["id", "get_course_name", "num", "title", "deleted"]
	ordering = ["-course__name", "-num"]
	list_per_page = 5
	list_filter = ["course", "created", "deleted"]
```
* поиск по содержимому (search_fields)
```python
@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
	search_fields = ["title", "preambule", "body"]
```
* пользовательские действия
```
Чтобы задать собственные действия, надо:
1. Реализовать функцию действия.
2. Добавить имя функции в атрибут actions.
3. (Опционально) Добавить к функции атрибут short_description, чтобы удобнее читать названия действия.
```
```python
@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
	list_display = ["id", "get_course_name", "num", "title", "deleted"]
	ordering = ["-course__name", "-num"]
	list_per_page = 5
	list_filter = ["course", "created", "deleted"]
	actions = ["mark_deleted"]

	def get_course_name(self, obj):
		return obj.course.name

	get_course_name.short_description = _("Course")
	def mark_deleted(self, request, queryset):
		queryset.update(deleted=True)

	mark_deleted.short_description = _("Mark deleted")
```
* кастомизация внешнего вида
* изменение логотипа
```
templates/admin/base_site.html
```
```html
{% extends "admin/base.html" %}
{% load static %}

{% block title %}
	{% if subtitle %}
		{{ subtitle }} | 
	{% endif %} 
	{{ title }} | {{site_title|default:_('Django site admin') }}
{% endblock %}

{% block branding %}

<h1 id="site-name">
<a href="{% url 'admin:index' %}">
<img src="{% static 'img/logo.png' %}" alt="">
</a>
</h1>
{% endblock %}
{% block nav-global %}
{% endblock %}
```
```
Возможности административного раздела расширяются через различные дополнительные пакеты. Некоторые из них полностью модифицируют способ взаимодействия с фреймворком. Перед тем как кастомизировать административный раздел, надо понять, действительно ли это необходимо. Если стандартных функций достаточно, то лучше использовать административный раздел «из коробки»: выигрыш — по времени, проигрыш — по гибкости. А если требуется тонкая настройка — добавление дополнительных страниц, реализация отображения графиков и прочее, то придётся реализовать aдминистративный раздел самостоятельно: выигрыш — по гибкости, проигрыш — по времени.
```
* https://djangopackages.org/grids/g/admin-interface/
```

```
*
```

```
