# Django ORM

* mainapp/models.py
```python
from django.db import models


class Client(models.Model):
    name = models.CharField(verbose_name="ФИО", max_length=100)
    contact = models.TextField(verbose_name="Контакт", blank=True, max_length=200)
    where_from = models.TextField(verbose_name="Источник заказа", blank=True, max_length=200)
    oder_details = models.TextField(verbose_name="Индивидуальные условия заказа", blank=True, max_length=200)
    address = models.TextField(verbose_name="Адрес доставки", blank=True, max_length=200)
    notes = models.TextField(verbose_name="Заметки", blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
* если нам нужно вернуться к миграции к другой миграции мы выполним следующую команду
```
python manage.py migrate mainapp 0005_second_last_migration
```
* если нам нужно отменить все миграции приложения, мы воспользуемся следующей командой
```
python manage.py migrate mainapp zero
```
* если нам нужно полностью очистить всю базу данных, мы можем использовать следующую команду
```
python manage.py flush
```
```
* передать данные из view в БД
```python
from mainapp.models import Book

def orm(request):
    data = Client(name='some_data')
    data.save()

    return render(request, 'mainapp/orm.html')
```
* получение данных из БД
```python
from mainapp.models import Book

def get_data_orm(request):
    data = Client.objects.all()
    #действие с данными
    context = {
            data: 'data',
        }

    return render(request, 'mainapp/orm.html', context)
```
* настройка админки
```
python manage.py createsuperuser
```
* в mainapp/admin.py
```python
from django.contrib import admin
from .models import Client, Product, Order

admin.site.register(Client)
```
```
http://127.0.0.1:8000/admin/
```
* shell_plus для доступа к данным БД
```
pip install django-extensions
```
* Добавим django-extensions в файл config/settings.py
```python
INSTALLED_APPS = [
    # ...
    'django_extensions',
    'mainapp',
]
```
* чтобы shell отрисовывал SQL запросы
```
python manage.py shell_plus --print-sql
```
### отношения Django One-To-One
* в родительской таблице Employee вы добавите OneToOneField, который используется для определения связи между двумя таблицами
```python
class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.phone


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
```
* при этом связать данные между таблицами прийдется вручную, например
```
e = Employee(first_name='John',last_name='Doe')
e.save()
```
```
c = Contact(phone='+79120000000', address='Moscow city, Leninsky avenue, house 11')
c.save()
```
* делаем связку
```
e.contact = c
e.save()
```
* при попытке привязать такойже Contact к еще одному сотрудникоу возникнет ошибка
```
django.db.utils.IntegrityError: duplicate key value violates unique constraint "mainapp_employee_contact_id_key"
```
### отношения Django One-To-Many
* например когда несколько сотрундников работают в одном отделе, но при этом один конкретный сотрудник может работать тольков одном отделе
* данная структура реализуюется через строку
```
department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)
```
```python
class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.phone


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
```
* запускаем shell_plus
```
python manage.py shell_plus --print-sql
```
* добавляем сотрудника
```
e = Employee(first_name='Jane',last_name='Doe')
e.save()
```
* добавляем отдел
```
d = Department(name='IT',description='Information Technology')
d.save()
```
* присваиваем сотруднику отдел
```
e.department = d
```
### отношения Django Many-to-Many
* например когда скольок угодно сотрудников имеют зарплатные программы и соответственно зарплатные программы могут относиться к скольки угодно сотрудникам
* связь реализуется через строчку
```
compensations = models.ManyToManyField(Compensation)
```
```python
class Compensation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.phone


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)
    compensations = models.ManyToManyField(Compensation)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
```
* Djnago создает соединительную таблицу hr_employee_compensations. Она имеет два внешних ключа employee_id  и  compensation_id
* внешний employee_id ключ ссылается на id таблицу hr_employee, а compensation_id внешний ключ ссылается id на hr_compensation таблицу.
* запускаем shell_plus
```
python manage.py shell_plus --print-sql
```
* Создадим три зарплатные программы
```
c1 = Compensation(name='Stock')
c1.save()
c2 = Compensation(name='Bonuses') 
c2.save()
c3 = Compensation(name='Profit Sharing')  
c3.save()
```
* выберем любого сотрудника
```
e = Employee.objects.get(id=8)
```
* присвоим ему пару зарплатных программ
```
e.compensations.add(c1)
e.compensations.add(c2) 
e.save()
```
* внутри Django вставил идентификаторы сотрудников и компенсаций в таблицу соединений - hr_employee_compensations
* мы можем найти всех сотрудников по зарплатной программе использую set
```
c1.employee_set.all()
```
* или тоже самое, но подругому
```
Employee.objects.filter(compensations__id=1)
```
* чтобы удалить зарплатную программу у сотрудника используем remove()
```
e.compensations.remove(c2)
```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
