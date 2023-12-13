## Работа с формами через forms.Form и django-widget-tweaks

* форма с выпадающим списком
```python
class NewOrderForm(forms.Form):
    CHOICES = [
        (1, 'Поступил'),
        (2, 'Собран'),
        (3, 'Отправлен'),
        (4, 'Срочно')
    ]

    client = forms.CharField(label="Клиент", max_length=100)
    product = forms.CharField(label="Продукт", max_length=100)
    quantity = forms.IntegerField(label="Количество", initial=1)
    description = forms.CharField(label="Примечание", max_length=200, required=False)
    status = forms.ChoiceField(label="Статус", choices=CHOICES, initial=1)
```
* создаем вьюшку, которая будет обрабатывать данные из формы
```python
def new_order(request):
    if request.method == "GET": #если GET, то просто создается форма
      new_order_form = NewOrderForm()

      return render(request, "new_order.html", {
            "new_order_form": new_order_form,
        })

    elif: request.method == "POST": #если с сервера пришел пост запрос, то заполняем БД данными из формы
      if form.is_valid():
        form_data = form.cleaned_data

        order_position = OrderPosition.objects.create(
            client=form_data['client'],
            product=form_data['product'],
            quantity=form_data['quantity'],
            status=form_data['status'],
            description=form_data['description'],
        )

        order_position.save()

        return HttpResponse('<h1>Данные отправлены</h1>')
```
* добавляем расшинеие для удобной работы с формами в шаблоне
```
pip install django-widget-tweaks
```
* в шаблоне добавляем форму, 
```html
<form class="form new_order" method="post">
      {% csrf_token %}
      <label>{{ new_order_form.client.label_tag }}</label>
      {% render_field new_order_form.client class="form-control" %}

      <label>{{ new_order_form.product.label_tag }}</label>
      {% render_field new_order_form.product class="form-control" %}

      <label>{{ new_order_form.quantity.label_tag }}</label>
      {% render_field new_order_form.quantity class="form-control" %}

      <label>{{ new_order_form.description.label_tag }}</label>
      {% render_field new_order_form.description class="form-control" style="background-color: red" %}

      <label>{{ new_order_form.status.label_tag }}</label>
      {% render_field new_order_form.status class="form-control" %}
      <br>
  <button type="submit" class="btn btn-primary">Создать</button>
</form>
```
### Работа с формами через UserCreationFrom и django-crispy-forms
```
authapp/forms.py
```
```python
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField


class CustomUserCreationForm(UserCreationForm):
    field_order = [
        "username",
        "password1",
        "password2",
        "email",
        "first_name",
        "last_name",
        "age",
        "avatar",
    ]

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "age",
            "avatar",
        )
        field_classes = {"username": UsernameField}
```
* authapp/views.py
```python
class RegisterView(CreateView):
    model = get_user_model()
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy("mainapp:main_page")
```
```
В контроллере шаблон не указывается, его имя сформируется автоматически. Имя шаблона составляется из имени
модели в нижнем регистре и постфикса _form. Постфикс определён в родительском классе контроллера в атрибуте
template_name_suffix. Модель пользователя — CustomUser. Имя шаблона — customuser_form.html. Это ещё одна
конвенция Django. Помимо контроллера создания (CreateView), этот шаблон станет использовать и другой тип
контроллера обновления объекта (UpdateView). При использовании стандартных контроллеров в контекст шаблона,
а именно в переменную form, помещается объект формы. Для генерации вёрстки из объекта формы берутся три функции:
1. as_p — поля формы формируются как параграфы. 
2. as_ul — поля формы формируются как элементы списка.
3. as_table — поля формы формируются как таблица.
```
```
touch authapp/templates/authapp/customuser_form.html
```
```html
{% extends 'base.html' %}

{% block content %}
<div class="row justify-content-center my-2">
  <div class="col-lg-6">

    {% if user.is_anonymous %}
    <h3>Регистрация нового пользователя</h3>
    {% else %}
    <h3>Редактировать профиль</h3>
    <div class="row justify-content-center">
      <div class="col-sm-7 col-md-5 col-lg-4">
        {% if user.avatar %}
        <img src="{{ user.avatar.url }}" alt="" width="100%">
        {% else %}
        <img src="{{ MEDIA_URL }}avatar_default.svg" alt="" width="100%">
        {% endif %}
      </div>
    </div>
    {% endif %}

    <form method="post" class="mt-2" enctype="multipart/form-data">
      {% csrf_token %}
      {{ form }}
      <button type="submit" class="btn btn-primary btn-block">
        {% if user.is_anonymous %}
        Зарегистрироваться
        {% else %}
        Сохранить
        {% endif %}
      </button>
    </form>
  </div>
</div>
{% endblock content %}
```
* Для стилистического оформления форм под некоторые CSS-фреймворки спользуется
дополнительный пакет для Django: django-crispy-forms.
```
pip install django-crispy-forms
```
```python
INSTALLED_APPS = [
    "crispy_forms",
]
```
```
pip install crispy-bootstrap4
```
```python
INSTALLED_APPS = [
    "crispy_forms",
]
```
```
CRISPY_TEMPLATE_PACK = "bootstrap4"
```
```html
{% extends 'base.html' %}
{% load crispy_forms_tags %}

<form method="post" class="mt-2" enctype="multipart/form-data">
      {% csrf_token %}
      {{ form|crispy }}
      <button type="submit" class="btn btn-primary btn-block">
        {% if user.is_anonymous %}
        Зарегистрироваться
        {% else %}
        Сохранить
        {% endif %}
      </button>
</form>

{% endblock content %}
```
* Методы проверки полей формы
```
В формах Django для проверки конкретных полей можно создать метод с суффиксом clean_ и именем поля. Значения формы извлекаются из внутреннего объекта cleaned_data.
a. Метод clean_avatar проверяет изменение аватарки пользователя:
если она изменилась, то файл со старой картинкой удаляется.
b. Метод clean_age проверяет возраст пользователя. Если его значение не соответствует критериям, то возбуждается исключение ValidationError. Текст оттуда система выведет в форму как подсказку.
```
```python
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "age",
            "avatar",
        )
        field_classes = {"username": UsernameField}

    def clean_avatar(self):
        arg_as_str = "avatar"
        if arg_as_str in self.changed_data and self.instance.avatar:
            if os.path.exists(self.instance.avatar.path):
                os.remove(self.instance.avatar.path)
        return self.cleaned_data.get(arg_as_str)

    def clean_age(self):
        data = self.cleaned_data.get("age")
        if data:
            if data < 10 or data > 100:
                raise ValidationError(_("Please, enter a valid age!"))
        return data
```
* получение первичного ключа (pk) пользователя через url адрес
* authapp/views.py
```python
class ProfileEditView(UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = forms.CustomUserChangeForm

    def test_func(self):
        return True if self.request.user.pk == self.kwargs.get("pk") else False

    def get_success_url(self):
        return reverse_lazy("authapp:profile_edit", args=[self.request.user.pk])
```
```
Во время обычной проверки входа любой пользователь сможет изменить значение в адресной строке, чтобы редактировать профили других пользователей. Надо внимательно относиться к возможным проблемам с чувствительными данными и проверять векторы атаки.
Для решения этой проблемы мы используем примесь UserPassesTestMixin. Она добавляет в класс контроллера функцию test_func, которую требуется переопределить. Эта функция делает проверку перед тем, как пропускать запрос на дальнейшую обработку, а затем возвращает булево значение.

get_success_url — способ указания возвратного url, куда системаперенаправит пользователя после успешного редактирования профиля. Контроллер не знает значение pk пользователя в объекте запроса заранее. Чтобы запросить это значение, используется метод get_success_url, который формирует ссылку с использованием объекта запроса.
```
* authapp/urls.py
```python
path("profile_edit/<int:pk>/", views.ProfileEditView.as_view(), name="profile_edit",)
```
* templates/includes/main_menu.html
```html
<a class="dropdown-item" href="{% url 'authapp:profile_edit' pk=request.user.pk %}">Редактировать профиль</a>
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
