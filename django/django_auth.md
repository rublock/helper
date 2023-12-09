### Пользователи Django
* Недостатки модели пользователя «по умолчанию»
```
Недостатки модели пользователя «по умолчанию»
1. Имя пользователя считается регистрозависимым. То есть, с точки зрения Django, имена, типа
John и john, разные.
2. Имя пользователя часто состоит из unicode-символов. Например, в него входят такие
символы, как @, +, _ и даже😎.
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
* authapp/models.py переопределяем стандартную модель пользователя
```python
from pathlib import Path
from time import time

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.db import models
#фреймворк перевода
from django.utils.translation import gettext_lazy as _

# функция которая возвращает путь к файлу и имя файла аватарки в формате вермени в юникод
# instance — экземпляр класса модели пользователя
# filename — имя загруженного файла
# формат файла pic_1702039183
def users_avatars_path(instance, filename):
    # файл будет загружен в:
    # MEDIA_ROOT / user_<username> / avatars / <filename>
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
        #проверка имени пользователя на символы -*/!@#$%^&*() и т.д.
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    #этого поля например нет в стандартной модели
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

    #стандатный менеджер модели, для модели пользователя
    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    #как мы будем видеть поля в админке
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
* config/settings.py прописываем путь до медиафайлов
```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```
* создадим диспетчеры адресов (корневой и в приложении)
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
    path("authapp/", include("authapp.urls", namespace="authapp")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
* authapp/urls.py
```python
from django.urls import path
from authapp import views
from authapp.apps import AuthappConfig


app_name = AuthappConfig.name

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("profile_edit/", views.ProfileEditView.as_view(), name="profile_edit"),
]
```
* config/settings.py меняем в найтройках стандартную модель аутентификации пользователя
```python
AUTH_USER_MODEL = "authapp.CustomUser"
```
* config/settings.py перенаправления пользователя при входе и выходе
```python
LOGIN_REDIRECT_URL = "mainapp:main_page"
LOGOUT_REDIRECT_URL = "mainapp:main_page"
```
* config/settings.py дабавляем контекстный процессор для медиафайлов
```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media", #new
                "django.contrib.auth.context_processors.auth",
                "mainapp.context_processors.example.simple_context_processor",
            ],
        },
    },
]
```
### Фреймвок сообщений
```
В Django «из коробки» предоставляется фреймворк сообщений. Этот механизм позволяет выводить
для пользователя различную служебную информацию, например, в виде всплывающих сообщений.
Эти сообщения предназначены для конкретного пользователя и создаются в момент формирования
ответа от сервера. Требуемый входной параметр — объект запроса.
Сообщения сохраняются:

●в текущей сессии пользователя;
●cookies;
●своей реализации хранилища.

Сообщения также разделяются по уровню важности: debug, info, success, warning, error. Это позволяет, например, отсекать отладочные (debug) уведомления в продуктовой среде. Сообщения удобно использовать при отладке, в качестве приветственных или информационных объявлений и т. д. Сочетая возможности шаблонов Django и JavaScript, уведомления выводятся и в консоль браузера. Однако не стоит злоупотреблять этим инструментом: слишком частые сообщения раздражают пользователей.
В качестве основного хранилища сообщений мы будем использовать сессии.
```
* config/settings.py
```python
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"
```
* config/settings.py
```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages", #new
                "mainapp.context_processors.example.simple_context_processor",
            ],
        },
    },
]
```
* authapp/views.py контроллер для обработки страницы входа с выводом соощбений
```python
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.utils.safestring import mark_safe
#фреймворк перевода на другой язык
from django.utils.translation import gettext_lazy as _


class CustomLoginView(LoginView):
    def form_valid(self, form):
        ret = super().form_valid(form)
        #код для вывода сообщения
        message = _("Login success!<br>Hi, %(username)s") % {
            "username": self.request.user.get_full_name()
            if self.request.user.get_full_name()
            else self.request.user.get_username()
        }
        messages.add_message(self.request, messages.INFO, mark_safe(message))
        return ret

    def form_invalid(self, form):
        #код для вывода сообщения
        for _unused, msg in form.error_messages.items():
            messages.add_message(
                self.request,
                messages.WARNING,
                mark_safe(f"Something goes worng:<br>{msg}"),
            )
        return self.render_to_response(self.get_context_data(form=form))
```
* создаем папку для шаблонов
```
mkdir -p authapp/templates/registration/
```
* переносим в нее файл login.html
```
mv ./mainapp/templates/mainapp/login.html ./authapp/templates/registration/
```
* authapp/templates/registration/login.html с всплывающими окнами
```html
{% extends 'base.html' %}
{% load static %}
{% block content %}

    {% include 'includes/messages.html' %}

    <div class="row justify-content-around align-items-center" style="height: 100vh; margin: 0px">
        <div class="text-center">
            <p>
                <a href="{% url 'mainapp:main_page' %}"><img src="{% static 'img/logo.png' %}" alt=""></a>
            </p>
            <h2>Вход пользователя</h2>
            <form method="POST">

                {% csrf_token %}
                <p>
                    <input type="text" name="username" autofocus="" autocapitalize="none" autocomplete="username"
                        maxlength="150" class="textinput textInput form-control" required="" id="id_username"
                        placeholder="Username">
                </p>
                <p>
                    <input type="password" name="password" autocomplete="current-password"
                        class="textinput textInput form-control" required="" id="id_password" placeholder="Password">
                </p>
                <p>
                    <button type="submit" class="btn btn-primary btn-block">Войти</button>
                </p>
            </form>
            <p>
            <div class="row justify-content-between">
                <div class="col">
                    <a href="{% url 'authapp:register' %}"><small>Регистрация</small></a>
                </div>
                <div class="col">
                    <a href="#"><small>Забыли пароль?</small></a>
                </div>
            </div>
            </p>
            <h4>Вход через социальные сети</h4>
            <p>
            <div class="btn-group btn-block" role="group">
                <a class="btn btn-primary" href="#" role="button"><i class="fab fa-vk"></i></a>
                <a class="btn btn-primary" href="#" role="button"><i class="fab fa-github"></i></a>
                <a class="btn btn-primary" href="#" role="button"><i class="fab fa-facebook"></i></a>
            </div>
            </p>
        </div>
    </div>

{% endblock content %}
```
* код самих всплывающиих сообщений
```
touch templates/includes/messages.html
```
```html
<div class="position-absolute w-100" style="z-index: 1;">
    <div aria-live="polite" aria-atomic="true" class="m-2">
      <!-- Position it -->
      <div class="d-flex align-items-end flex-column">

        {% for message in messages %}
        <!-- Then put toasts within -->
        <div class="toast flex-fill w-100
      {% if message.level == 30 %}
      border-warning
      {% endif %}
        " role="alert" aria-live="assertive" aria-atomic="true"
          style="right: 0;">
          <div class="toast-header">
            <span class="mr-2"><i class="far fa-envelope"></i></span>
            <strong
              class="mr-auto {% if message.level == 30 %}text-warning{% endif %}">
              {{ message.tags|capfirst }} message</strong>
            <small class="text-muted">just now</small>
            <button type="button" class="ml-2 mb-1 close" data-dismiss="toast"
              aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="toast-body">
            {{ message }}
          </div>
        </div>
        {% if message.level > 20 %}
        <!-- If message will dissapere you will find message in console -->
        <script>
          console.log("{{ message }}");
        </script>
        {% endif %}

        {% endfor %}

      </div>
    </div>
  </div>
```
* mainapp/templates/mainapp/base.html добавляем блок {% block js %} для интерактивного вывода сообщений
```html
{% load static %}

<!doctype html>
<html lang="ru">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport"
    content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">

  <!-- ChartJS -->
  <link rel="stylesheet" href="{% static 'css/Chart.min.css' %}">

  <!-- FontAwesome -->
  <link rel="stylesheet" href="{% static 'css/fontawesome.all.min.css' %}">

  <title>
    {% block title %}
    Welcome to Braniac!
    {% endblock title %}
  </title>
</head>

<body>

  {% include 'includes/main_menu.html' %}

  {% block messages %}
  {% include 'includes/messages.html' %}
  {% endblock messages %}

  <div class="container-md">

    {% block content %}{% endblock content %}

  </div>

  <!-- Footer -->

  <div class="container-lg mt-auto">
    <hr>
    <div class="row justify-content-center">
      <div class="col-sm-6 col-md-3 text-center">
        <p>
          <strong>Braniac</strong>
        </p>
        <p>
        <ul class="list-unstyled">
          <li><a href="{% url 'mainapp:main_page' %}">Домашняя</a></li>
          <li><a href="{% url 'mainapp:news' %}">Новости</a></li>
          {% if user.is_authenticated %}
          <li><a href="{% url 'authapp:logout' %}">Выйти</a></li>
          {% else %}
          <li><a href="{% url 'authapp:login' %}">Войти</a></li>
          {% endif %}
        </ul>
        </p>
      </div>
      <div class="col-sm-6 col-md-3 text-center">
        <p>
          <strong>Полезное</strong>
        </p>
        <p>
        <ul class="list-unstyled">
          <li><a href="#">Положения &amp; Условия</a></li>
          <li><a href="#">Конфиденциальность &amp; Cookies</a></li>
          <li><a href="#">Документация по API</a></li>
          <li><a href="{% url 'mainapp:doc_site' %}">Документация по сайту</a>
          </li>
        </ul>
        </p>
      </div>
      <div class="col-sm-6 col-md-3 text-center">
        <p>
          <strong>Мы в социальных сетях</strong>
        </p>
        <p>
        <div class="row justify-content-around">
          <div><a href="#"><i class="fab fa-vk fa-2x"></i></a></div>
          <div><a href="#"><i class="fab fa-facebook-f fa-2x"></i></a>
          </div>
          <div><a href="#"><i class="fab fa-instagram fa-2x"></i></a>
          </div>
          <div><a href="#"><i class="fab fa-pinterest-p fa-2x"></i></a></div>
        </div>
        </p>
        <p>
          <strong>Наше приложение</strong>
        </p>
        <p>
        <div class="row justify-content-around">
          <div><a href="#"><i class="fab fa-app-store fa-2x"></i></a>
          </div>
          <div><a href="#"><i class="fab fa-google-play fa-2x"></i></a></div>
          <div><a href="#"><i class="fab fa-windows fa-2x"></i></a>
          </div>
        </div>
        </p>
      </div>
    </div>
    <div class="row justify-content-center">
      <div>
        <p><small>&copy; GeekBrains 2021</small></p>
      </div>
    </div>
  </div>

  <!-- /Footer -->

  <!-- JavaScript section -->
  <!-- Bootstrap -->
  <script src="{% static 'js/jquery-3.6.0.min.js' %}"></script>
  <script src="{% static 'js/popper.min.js' %}"></script>
  <script src="{% static 'js/bootstrap.min.js' %}"></script>

  <!-- ChartJs -->
  <script src="{% static 'js/Chart.min.js' %}"></script>

  <!-- FontAwesome -->
  <script src="{% static 'js/fontawesome.all.min.js' %}"></script>

  {% block js %}
  <script>
    $(document).ready(function () {

      {% if messages %}
      // Toasts
      $(".toast").toast({ delay: 5000 });
      $(".toast").toast("show");
      {% endif %}

    });
  </script>
  {% endblock js %}

</body>

</html>
```
* страница выхода
* При выходе пользователь переходит по адресу, указанному в настройках переменной LOGOUT_REDIRECT_URL
* authapp/views.py добавляем вниз следующий код
```python
class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, _("See you later!"))
        return super().dispatch(request, *args, **kwargs)
```
* страница регистрации нового пользователя
* свойство enctype="multipart/form-data", позволяет отправлять файлы картинок на сервер
```
touch authapp/templates/registration/register.html
```
```html
{% extends 'base.html' %}

{% block content %}
<div class="row justify-content-center my-2">
  <div class="col-lg-6">
    <h3>Регистрация нового пользователя</h3>
    <form method="post" class="mt-2" enctype="multipart/form-data">
      {% csrf_token %}
      <div id="div_id_username" class="form-group"> <label for="id_username"
          class=" requiredField">
          Username<span class="asteriskField">*</span> </label>
        <div class=""> <input type="text" name="username" maxlength="150"
            class="textinput textInput form-control" required=""
            id="id_username"> <small id="hint_id_username"
            class="form-text text-muted">Required. 150 characters or fewer.
            Letters, digits and @/./+/-/_ only.</small> </div>
      </div>
      <div id="div_id_password1" class="form-group"> <label for="id_password1"
          class=" requiredField">
          Password<span class="asteriskField">*</span> </label>
        <div class=""> <input type="password" name="password1"
            autocomplete="new-password" class="textinput textInput form-control"
            required="" id="id_password1"> <small id="hint_id_password1"
            class="form-text text-muted">
            <ul>
              <li>Your password can’t be too similar to your other personal
                information.</li>
              <li>Your password must contain at least 8 characters.</li>
              <li>Your password can’t be a commonly used password.</li>
              <li>Your password can’t be entirely numeric.</li>
            </ul>
          </small> </div>
      </div>
      <div id="div_id_password2" class="form-group"> <label for="id_password2"
          class=" requiredField">
          Password confirmation<span class="asteriskField">*</span> </label>
        <div class=""> <input type="password" name="password2"
            autocomplete="new-password" class="textinput textInput form-control"
            required="" id="id_password2"> <small id="hint_id_password2"
            class="form-text text-muted">Enter the same password as before, for
            verification.</small> </div>
      </div>
      <div id="div_id_first_name" class="form-group"> <label for="id_first_name"
          class="">
          First name
        </label>
        <div class=""> <input type="text" name="first_name" maxlength="150"
            class="textinput textInput form-control" id="id_first_name"> </div>
      </div>
      <div id="div_id_last_name" class="form-group"> <label for="id_last_name"
          class="">
          Last name
        </label>
        <div class=""> <input type="text" name="last_name" maxlength="150"
            class="textinput textInput form-control" id="id_last_name"> </div>
      </div>
      <div id="div_id_age" class="form-group"> <label for="id_age" class="">
          Age
        </label>
        <div class=""> <input type="number" name="age" min="0"
            class="numberinput form-control" id="id_age"> </div>
      </div>
      <div id="div_id_avatar" class="form-group"> <label for="id_avatar"
          class="">
          Avatar
        </label>
        <div class=""> <input type="file" name="avatar" accept="image/*"
            class="clearablefileinput form-control-file" id="id_avatar"> </div>
      </div>
      <div id="div_id_email" class="form-group"> <label for="id_email"
          class=" requiredField">
          Email address<span class="asteriskField">*</span> </label>
        <div class=""> <input type="text" name="email" maxlength="256"
            class="textinput textInput form-control" required="" id="id_email">
        </div>
      </div>

      <button type="submit"
        class="btn btn-primary btn-block">Зарегистрироваться</button>
    </form>
  </div>
</div>

{% endblock content %}
```
* authapp/views.py добавляем вниз следующий код
```python
from authapp import models
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy

class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def post(self, request, *args, **kwargs):

        # код оборачивается в try/except, чтобы код отработал до конца, и если что сообщил об ошибке
        # через фреймоворк сообщений
        try:
            if all(
                (
                    request.POST.get("username"),
                    request.POST.get("email"),
                    request.POST.get("password1"),
                    request.POST.get("password1") == request.POST.get("password2"),
                )
            ):
                #если все ок, создаем нового пользователя
                new_user = models.CustomUser.objects.create(
                    username=request.POST.get("username"),
                    first_name=request.POST.get("first_name"),
                    last_name=request.POST.get("last_name"),
                    age=request.POST.get("age") if request.POST.get("age") else 0,
                    avatar=request.FILES.get("avatar"),
                    email=request.POST.get("email"),
                )
                #пароли забираются ввиде хэшсуммы SHA256
                new_user.set_password(request.POST.get("password1"))
                new_user.save()
                # _ - феймворк сообщений, в зависимости от того какой язык включен
                messages.add_message(request, messages.INFO, _("Registration success!"))
                # reverse_lazy - формируется пусть для перенеправления пользователя сразу из пространства имен
                return HttpResponseRedirect(reverse_lazy("authapp:login"))
        except Exception as exp:
            messages.add_message(
                request,
                messages.WARNING,
                mark_safe(f"Something goes worng:<br>{exp}"),
            )
            return HttpResponseRedirect(reverse_lazy("authapp:register"))
```
* Страница редактирования профиля
* authapp/views.py добавляем в конец
* LoginRequiredMixin - проверяет вошел ли пользователь на сайт
* login_url - укажет, куда перенаправить пользователя, чтобы он мог войти на сайт
```python
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def post(self, request, *args, **kwargs):
        try:
            if all(
                (
                    request.POST.get("username"),
                    request.POST.get("email"),
                    request.POST.get("password1"),
                    request.POST.get("password1") == request.POST.get("password2"),
                )
            ):
                new_user = models.CustomUser.objects.create(
                    username=request.POST.get("username"),
                    first_name=request.POST.get("first_name"),
                    last_name=request.POST.get("last_name"),
                    age=request.POST.get("age") if request.POST.get("age") else 0,
                    avatar=request.FILES.get("avatar"),
                    email=request.POST.get("email"),
                )
                new_user.set_password(request.POST.get("password1"))
                new_user.save()
                messages.add_message(request, messages.INFO, _("Registration success!"))
                return HttpResponseRedirect(reverse_lazy("authapp:login"))
        except Exception as exp:
            messages.add_message(
                request,
                messages.WARNING,
                mark_safe(f"Something goes worng:<br>{exp}"),
            )
            return HttpResponseRedirect(reverse_lazy("authapp:register"))
```
* touch authapp/templates/registration/profile_edit.html
```html
{% extends 'base.html' %}

{% block content %}
<div class="row justify-content-center my-2">
  <div class="col-lg-6">
    <h3>Редактирование профиля</h3>

    <div class="row justify-content-center">
      <div class="col-sm-7 col-md-5 col-lg-4">
        {% if user.avatar %}
        <img src="{{ user.avatar.url }}" alt="" width="100%">
        {% else %}
        <img src="{{ MEDIA_URL }}avatar_default.svg" alt="" width="100%">
        {% endif %}
      </div>
    </div>

    <form method="post" class="mt-2" enctype="multipart/form-data">
      {% csrf_token %}
      <div id="div_id_username" class="form-group"> <label for="id_username"
          class=" requiredField">
          Username<span class="asteriskField">*</span> </label>
        <div class=""> <input type="text" name="username" maxlength="150"
            class="textinput textInput form-control" required id="id_username"
            value="{{ user.username }}"> <small id="hint_id_username"
            class="form-text text-muted">Required. 150 characters or fewer.
            Letters, digits and @/./+/-/_ only.</small> </div>
      </div>
      <div id="div_id_first_name" class="form-group"> <label for="id_first_name"
          class="">
          First name
        </label>
        <div class=""> <input type="text" name="first_name" maxlength="150"
            class="textinput textInput form-control" id="id_first_name"
            value="{{ user.first_name }}"> </div>
      </div>
      <div id="div_id_last_name" class="form-group"> <label for="id_last_name"
          class="">
          Last name
        </label>
        <div class=""> <input type="text" name="last_name" maxlength="150"
            class="textinput textInput form-control" id="id_last_name"
            value="{{ user.last_name }}"> </div>
      </div>
      <div id="div_id_age" class="form-group"> <label for="id_age" class="">
          Age
        </label>
        <div class=""> <input type="number" name="age" min="0"
            class="numberinput form-control" id="id_age" value="{{ user.age }}">
        </div>
      </div>
      <div id="div_id_avatar" class="form-group"> <label for="id_avatar"
          class="">
          Avatar
        </label>
        <div class=""> <input type="file" name="avatar" accept="image/*"
            class="clearablefileinput form-control-file" id="id_avatar"> </div>
      </div>
      <div id="div_id_email" class="form-group"> <label for="id_email"
          class=" requiredField">
          Email address<span class="asteriskField">*</span> </label>
        <div class=""> <input type="text" name="email" maxlength="256"
            class="textinput textInput form-control" required="" id="id_email"
            value="{{ user.email }}">
        </div>
      </div>

      <button type=" submit"
        class="btn btn-primary btn-block">Сохранить</button>
    </form>
  </div>
</div>

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
