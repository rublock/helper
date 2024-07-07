# Django ORM

взято из <https://stepik.org/lesson/1146709/step/1?unit=1158607>

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

### Манипуляция с данными в Django на основе CRUD 

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
My_model.objects.get(id=1)
My_model.objects.all()[5:10]
My_model.objects.filter(id=1)
My_model.objects.exclude(id=1)
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
# Организация связей между таблицами

### one-to-one

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

* on_delete=models.CASCADE говорит, что данные текущей модели Account будут удаляться в случае удаления связанного объекта главной модели User

* primary_key=True указывает, что внешний ключ (через который идет связь с главной моделью) одновременно будет выступать и в роли первичного ключа. И соответственно, создавать отдельное поле для первичного ключа не надо.

* В результате миграции в базе данных SQLite будут создаваться следующие таблицы:

```sql
CREATE TABLE "onetoone_user" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "name" varchar(20) NOT NULL
)
CREATE TABLE "onetoone_account" (
    "login" varchar(20) NOT NULL, 
    "password" varchar(20) NOT NULL, 
    "user_id" bigint NOT NULL PRIMARY KEY REFERENCES "onetoone_user" ("id") DEFERRABLE INITIALLY DEFERRED
)
```
![](https://github.com/rublock/helper/raw/main/django/img/django_ORM_one_to_one.png)

* С помощью атрибута user (поле user_id) в модели Account мы можем манипулировать связанным объектом модели User
```
alex = User.objects.create(name="Александр")
acc = Account.objects.create(login="1234", password="6565", user=alex)

acc.user.name = "Саша"
acc.user.save()
```
* При этом через модель User мы также можем оказывать влияние на связанный объект Account.
```
alex = User.objects.create(name="Александр")

асс = Account(login="1234", password="6565")
alex.account = асс
alex.account.save()

alex.account.login = "qwerty"
alex.account.password = "123456"
alex.account.save()
```
* Подобным образом можно выполнять фильтрацию по обеим моделям и их атрибутам:
```
alex = User.objects.get(name="Александр")
alex_acc = Account.objects.get(user=alex)
print(f"login: {alex_acc.login}, password: {alex_acc.password}")

alexander_acc = Account.objects.get(user__name="Aлeкcaндp")
print(f"login: {alexander_acc.login}, password: {alexander_acc.password}")
```
*  Через два знака подчеркивания мы можем указать имя поля второй модели - например, user__name или user__id.
```
user = User.objects.get(account__login="qwerty")
print(user.name)
```

### one-to-many

* одна главная сущность может быть связаны с несколькими зависимыми сущностями
```python
class Company(models.Model):
    name = models.CharField(max_length=30)
 
class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
```
![](https://github.com/rublock/helper/raw/main/django/img/django_ORM_one_to_many.png)

* Конструктор типа models.ForeignKey в классе Product настраивает связь с главной сущностью.

* Здесь первый параметр указывает, с какой моделью будет создаваться связь, - в нашем случае это модель Company

* Создадим компанию и присвоим ей 2 продукта
```
c = Company(name='Nestle')
c.save()

e = Product(company=c, name='Chocolate', price=100)
e.save()

e = Product(company=c, name='Dragees', price=200)
e.save()
```
```
Product.objects.get(id=1).company.id
# получим 1

Product.objects.get(id=2).company.name
# получим 'Nestle'
```
```
Product.objects.filter(company__name='Nestle')
# получим <QuerySet [<Product: Product object (1)>, <Product: Product object (2)>]>
```
Здесь нужно обратить особое внимание на выражение company__name. С помощью выражения модель__атрибут (обратите внимание: два подчеркивания!) можно использовать атрибут главной модели для фильтрации объектов (записей в таблице БД) зависимой модели.
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
