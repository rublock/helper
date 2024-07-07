# Django ORM

* базовая структура модели
```python
class Modelname(models.Model):
    #Fields
    field_name = models.CharField(max_length=20, help_text='some text')

    #Metadata
    class Meta:
        ordering = ['field_name']

    #Methods
    def __str__(self):
        return '<readable_name>'
```
* все поля обязательны к заполнению по умолчанию
* django автоматически добавляет поле primary_key
```python
id = models.AutoField(primary_key=True)
```
#### Манипуляция с данными в Django на основе CRUD 

* открываем консоль
```
python manage.py shell
``` 
```
from my_app.models import My_model
```
* Добавление данных
```
data = My_model.objects.create(text='some text')
data.save()
```
* Обращение к полям
```
data.id
data.text
```
* Чтение данных
```
data = My_model.objects.get(id=1)
data = My_model.objects.all()[5:10]
data = My_model.objects.filter(id=1)
data = My_model.objects.exclude(id=1)
```
* Методы all(), filter() и exclude() возвращают объект QuerySet. Это, по сути, некое промежуточное хранилище, в котором содержится информация, полученная из БД.

* Обновление объектов
```
data = My_model.objects.get(id=1)
data.text = 'some new text'
data.save()
```
* Когда нужно обновить только определенные поля, следует использовать параметр update_fields. Такой подход позволяет повысить скорость работы приложения, особенно в тех случаях, когда требуется обновить большой массив информации.
```
data = My_model.objects.get(id=1)
data.text = 'some new text'
data.save(update_fields=["text"])
```
* Другой способ обновления объектов в БД предоставляет метод update() в сочетании с методом filter() или all().
```
My_model.objects.filter(id=1).update(text='some new text')
My_model.objects.all().update(text='some new text for all')
```
* Удаление данных из БД
```
My_model.objects.filter(id=1).delete()
```
* с помощью свойства query можно получить и посмотреть текст выполняемого SQL-запроса
```
data = My_model.objects.all()
print(data.query)
```
#### Организация связей между таблицами

* один-к-одному
* Обычно связь «один-к-одному» легко моделируется в одной таблице.
* В редких случаях связь «один-к-одному» моделируется с использованием двух таблиц. Такой вариант иногда необходим, чтобы преодолеть ограничения СУБД, или с целью увеличения производительности (производится, например, вынесение ключевого поля в отдельную таблицу для ускорения поиска по другой таблице).
* Для создания отношения «один-к-одному» применяется тип связи models.OneToOneField()

```python
class User(models.Model):
    name = models.CharField(max_length=20)


class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
```
![](https://github.com/rublock/helper/raw/main/django/img/django_ORM_one_to_one.png)
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
