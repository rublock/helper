### Пользователи Django
* Недостатки модели пользователя «по умолчанию»
```
Недостатки модели пользователя «по умолчанию»
При обширном наборе полей в этой модели пользователя выделяется ряд недостатков:
1. Имя пользователя считается регистрозависимым. То есть, с точки зрения Django, имена, типа
John и john, разные.
2. Имя пользователя часто состоит из unicode-символов. Например, в него входят такие
символы, как @, +, _ и даже
😎.
3. Адрес электронной почты не считается уникальным значением. Это значит, что пользователь с
одним мейлом сможет создать множество аккаунтов. И если в одной учётной записи есть
чувствительные данные, то потом будет сложно восстановить пароль через электронную
почту.
4. Поле адреса электронной почты заполнять необязательно. Однако без этой информации
сложно определить, кто зарегистрировался на сайте: бот или человек.
5. Иногда при создании пользователя в метод установки пароля передаётся параметр None.
Из-за этого блокируется возможность смены пароля для пользователя.
6. При использовании модели «по умолчанию» трудно переключиться на новую модель
пользователя, когда проводятся первые миграции.
Важно! Нельзя задать аватар или возраст для пользователя.
Для решения большинства этих проблем разработчики Django рекомендуют создавать собственную
реализацию модели пользователя.
```
* создание приложения
```
python manage.py startapp authapp
```
* config/settings.py
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "mainapp",
    "authapp", #new
]
```
* переопределяем стандартную модель пользователя
```python
from pathlib import Path
from time import time

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _

# функция динамического задания имени по времени в unicode:
# instance — экземпляр класса модели пользователя
# filename — имя загруженного файла
def users_avatars_path(instance, filename):
    # file will be uploaded to
    #   MEDIA_ROOT / user_<username> / avatars / <filename>
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return "user_{0}/avatars/{1}".format(instance.username, f"pic_{num}{suff}")


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    # поле для аватарки
    avatar = models.ImageField(upload_to=users_avatars_path, blank=True, null=True)
    email = models.CharField(
        _("email address"),
        max_length=256,
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. \
            Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    # метод для нормализации e-mail
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    # полное имя пользователя имя, фамилия через пробел
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    # только имя
    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    # отправить пользователю письмо по e-mail
    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
```
* что изменилось
```
1. Валидатор для поля username. Валидаторы — это функции, которые проверяют содержимое
поля перед созданием записи в таблице БД. Теперь поле содержит только ASCII-символы.
2. Добавилось поле возраста — age.
3. Поле email теперь обязательно для заполнения и уникально.
4. Теперь есть поле avatar для загрузки фотографии пользователя.
```
* устанавливаем Pillow для работы с изображениями (аватарки)
```
pip install Pillow
```
* в config/settings.py прописываем путь до медиафайлов
```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```
* для работы с медиафайлами в процессе отладки надо дополнительно указать соответствующие
адреса в корневом диспетчере config/urls.py
```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="mainapp/")),
    path("mainapp/", include("mainapp.urls", namespace="mainapp")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
* config/settings.py
```python
AUTH_USER_MODEL = "authapp.CustomUser"
```
* config/settings.py
```python
LOGIN_REDIRECT_URL = "mainapp:main_page"
LOGOUT_REDIRECT_URL = "mainapp:main_page"
```
* config/settings.py
```python
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"
```
* config/settings.py
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
