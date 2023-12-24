### Django tests
* django.test TestCase
```
TestCase из пакета django.test. Он позволяет создавать unit-тесты, сосредоточенные на
проверке одного небольшого участка кода. Например, контроллера. В одном из атрибутов
(client) содержится эмулятор клиента (браузера), который после вызова возвращает полное
состояние ответа: контекст, выборку, статус ответа сервера и т. д.

Client из пакета django.test. От этого класса отделяется дочерний объект TestCase.client. Он
позволяет создавать отдельный клиент, с которым удобно тестировать открытие страницы от
аутентифицированного и неаутентифицированного пользователя.

В пакете http стандартной библиотеки Python содержится класс, куда входят все цифровые значения
кодов ответа от сервера по HTTP-протоколу, записанные в виде буквенного обозначения.
```
* Тест для проверки открытия страницы
* mainapp/tests.py
```python
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class TestMainPage(TestCase):
    def test_page_open(self):
        path = reverse("mainapp:main_page")
        result = self.client.get(path)
        self.assertEqual(result.status_code, HTTPStatus.OK)
```
* запуск всех тестов
```
python manage.py test
```
* запуск одиночного теста
```
python manage.py test mainapp.tests.TestMainPage.test_page_open
```
### Тестовый клиент с аутентификацией
* authapp/fixtures/001_user_admin.json
```json
[
    {
        "model": "authapp.customuser",
        "pk": 1,
        "fields": {
            "password": "pbkdf2_sha256$260000$vNK7LRbyZjjMFaFoh6nYQm$w6qmPwBvMRAoLHC5Q7ZNuMC5h+K7rDI/3XSuhHofZxM=",
            "last_login": "2022-01-01T01:02:03.044Z",
            "is_superuser": true,
            "username": "admin",
            "first_name": "",
            "last_name": "",
            "age": null,
            "avatar": "",
            "email": "admin@local.ru",
            "is_staff": true,
            "is_active": true,
            "date_joined": "2022-01-01T00:01:02.033Z",
            "groups": [],
            "user_permissions": []
        }
    }
]
```
```
Для аутентификации нового клиента в контроллер посылается POST-запрос. Это требуется, чтобы
войти на сайт, содержащий поля username и password. Результат — клиент, который выполнил вход на
сайт (установлены соответствующие cookie). Такая операция проводится в методе setUp, который
запускается при каждом запуске любого внутреннего теста в классе. Имея два клиента
(аутентифицированного и нет) проверяем, что доступ к разным операциям отличается у разных
пользователей. Например, администратору CRUD-страницы доступны, анонимному пользователю —
нет.
```
* mainapp/tests.py
```python
from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse

from authapp import models as authapp_models
from mainapp import models as mainapp_models


class TestNewsPage(TestCase):
    fixtures = (
        "authapp/fixtures/001_user_admin.json",
        "mainapp/fixtures/001_news.json",
    )

    def setUp(self):
        """Логинимся под админом"""
        super().setUp()
        self.client_with_auth = Client()
        self.user_admin = authapp_models.CustomUser.objects.get(username="admin")
        self.client_with_auth.force_login(self.user_admin, backend="django.contrib.auth.backends.ModelBackend")

    def test_page_open_update_deny_access(self):
        """Тест на открытие страницы изменения новости"""
        news_obj = mainapp_models.News.objects.first()
        path = reverse("mainapp:news_update", args=[news_obj.pk])
        result = self.client.get(path)
        self.assertEqual(result.status_code, HTTPStatus.FOUND)

    def test_page_open_update_by_admin(self):
        """Тест на открытие страницы изменения новости под администратором"""
        news_obj = mainapp_models.News.objects.first()
        path = reverse("mainapp:news_update", args=[news_obj.pk])
        result = self.client_with_auth.get(path)
        self.assertEqual(result.status_code, HTTPStatus.OK)
```
```
POST-запросы в клиенте посылаются через метод post. Чтобы передать в них данные, надо указать в
именованном аргументе data словарь с подходящими данными.

Тесты, связанные с изменением количества объектов (создание, удаление), проверяются запросом
количества объектов в БД. В тесте на обновление данных выбранный объект обновляется из БД через
метод refresh_from_db.

Фикстуры с данными указываются в атрибуте тестового класса fixtures. Например, в описанном классе
подгружаются фикстуры с объектами новостей и пользователем-администратором.
```
### Консервация объектов и объекты-пустышки
```
Часто функция, которую мы тестируем, делает вызовы из внешних систем, например, обращение по
API или кешу. Если тест не проверяет результат взаимодействия двух систем, то функция
28изолируется. Для этого используются объекты-пустышки или mock-объекты. Они подменяют собой
вызов сторонних систем.

Чтобы сохранить ответ от внешней системы, используется инструментарий стандартной библиотеки
Python — pickle или консервация объектов.
```
* mainapp/views.py
```python
class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):

        cached_feedback = cache.get(f"feedback_list_{pk}")

        if not cached_feedback:
            context["feedback_list"] = (
                mainapp_models.CourseFeedback.objects.filter(course=context["course_object"])
                .order_by("-created", "-rating")[:5]
                .select_related()
            )
            cache.set(f"feedback_list_{pk}", context["feedback_list"], timeout=300)  # 5 minutes

            import pickle
            """Архивируем объект для тестов"""
            with open(f"mainapp/fixtures/005_feedback_list_{pk}.bin", "wb") as outf:
                pickle.dump(context["feedback_list"], outf)

        else:
            context["feedback_list"] = cached_feedback

        return context
```
* Сохранённый объект переиспользуется в тестах
* mainapp/tests.py
```python
import pickle
from unittest import mock


class TestCoursesWithMock(TestCase):
    fixtures = (
        "authapp/fixtures/001_user_admin.json",
        "mainapp/fixtures/002_courses.json",
        "mainapp/fixtures/003_lessons.json",
        "mainapp/fixtures/004_teachers.json",
    )

    def test_page_open_detail(self):
        course_obj = mainapp_models.Courses.objects.get(pk=1)
        path = reverse("mainapp:courses_detail", args=[course_obj.pk])
        with open("mainapp/fixtures/005_feedback_list_1.bin", "rb") as inpf, mock.patch(
            "django.core.cache.cache.get"
        ) as mocked_cache:
            mocked_cache.return_value = pickle.load(inpf)
            result = self.client.get(path)
            self.assertEqual(result.status_code, HTTPStatus.OK)
            self.assertTrue(mocked_cache.called)
```
```
Подмена вызова функции происходит с применением функции mock.patch(). К ней на вход подаётся
указание на объект в виде строки. В нашем случае этот объект — функция получения значения из
кеша cache.get модуля django.core.cache. Когда функция mock.patch применится как контекстный
менеджер через оператор with, произойдёт подмена. Важно указать возвращаемое значение через
атрибут return_value. В качестве этого значения станет возвращаться расконсервированный из файла
объект.

Mock-объект содержит атрибуты и методы, которые позволяют проверить, был ли объект вызван
(called), то есть было ли обращение к кешу.
```
### Тесты отложенных задач
* тест отправки электронного письма
* mainapp/tests.py
```python
from django.core import mail as django_mail

from mainapp import tasks as mainapp_tasks


class TestTaskMailSend(TestCase):
    fixtures = ("authapp/fixtures/001_user_admin.json",)

    def test_mail_send(self):
        message_text = "test_message_text"
        user_obj = authapp_models.CustomUser.objects.first()
        mainapp_tasks.send_feedback_mail({"user_id": user_obj.id, "message": message_text})
        self.assertEqual(django_mail.outbox[0].body, message_text)
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
