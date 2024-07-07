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

* открываем шелл консоль
```
python manage.py shell
``` 
```
from my_app.models import My_model
```
* Добавление данных в БД
```
data = My_model.objects.create(text='some text')
data.save()
```
* 
```

```
