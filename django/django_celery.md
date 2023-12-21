### Отложенные задачи на примере Celery + Redis
* Рассмотрим задачи по отправке запроса в техподдержку по электронной почте. В качестве
обработчика сообщений воспользуемся программой Celery, а вместо брокера — Redis.
```
pip install "celery[redis]"
```
* config/settings.py
```python
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_ACCEPT_CONTENT = {'application/json'}
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = "redis://localhost:6379"
```
```
touch config/celery.py
```
```python
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")# переменные окружения
celery_app = Celery("ed_portal")# инициализация приложения
celery_app.config_from_object("django.conf:settings", namespace="CELERY") #пространство имен
celery_app.autodiscover_tasks() #celery будет искать задачи в tasks.py
```
* регистрируем новое приложение
* config/__init__.py
```python
from .celery import celery_app

__all__ = ("celery_app",)
```
* mainapp/tasks.py
```python
from celery import shared_task
from django.core.mail import send_mail


@shared_task(bind=True)
def send_feedback_mail(self, user_message, user_mail):
    mail_subject = "Welcome on Board!"
    send_mail(
        subject=mail_subject,
        message=user_message,
        from_email='lpsys1@gmail.com',
        recipient_list=[user_mail],
        fail_silently=False,
    )
    return "Done"
```
```
После настройки Celery в проекте Django появляется ещё одна конвенция. Celery автоматически
считывает все задачи, которые содержатся в модулях tasks.py в корне приложений, и позволяет
запускать их с указанными параметрами.

Важно! Параметры, которые передаются в функции как входные (отложенные задачи), обязательно
сериализуются в JSON-формат. Общение происходит через сторонний сервис — брокер, поэтому
передача Python-объектов невозможна. Рекомендуется передавать словарь, у которого ключи и
значения содержат примитивные типы: числа и строки.
```
* Для отправки электронных писем в Django доступны такие бэкенды:
```
1. django.core.mail.backends.smtp.EmailBackend — для отправки писем через почтовый сервер по
SMTP-протоколу.
2. django.core.mail.backends.console.EmailBackend — отправка писем в консоль. Ещё один
вариант отладки.
3. django.core.mail.backends.locmem.EmailBackend — отправка писем в память. Сообщения
помещаются в объект django.core.mail. Удобный вариант для тестирования.
4. django.core.mail.backends.dummy.EmailBackend — заглушка для отправки писем. Функция
отправки письма отрабатывает корректно без каких-либо результатов.
```
* config/settings.py
```python
# SMTP SETTINGS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "lpsys1@gmail.com"
EMAIL_HOST_PASSWORD = "okvqqgnzccvttuak"
DEFAULT_FROM_EMAIL = "lpsys1@gmail.com"
```
* mainapp/forms.py
```python
class MailFeedbackForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput)
    message = forms.CharField(
        widget=forms.Textarea,
        help_text=_("Enter your message"),
        label=_("Message"),
    )

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields["user_id"].initial = user.pk
```
* mainapp/views.py
```python
class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"

    def get_context_data(self, **kwargs):
        context = super(ContactsPageView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["form"] = mainapp_forms.MailFeedbackForm(user=self.request.user)
        return context

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            cache_lock_flag = cache.get(f"mail_feedback_lock_{self.request.user.pk}")
            if not cache_lock_flag:
                cache.set(
                    f"mail_feedback_lock_{self.request.user.pk}",
                    "lock",
                    timeout=3,
                )
                messages.add_message(self.request, messages.INFO, _("Message sended"))
                pk = self.request.POST.get("user_id")
                model = get_user_model()
                user_email = model.objects.get(pk=pk).email
                user_message = self.request.POST.get("message")
                mainapp_tasks.send_feedback_mail.delay(user_message, user_email)
            else:
                messages.add_message(
                    self.request,
                    messages.WARNING,
                    _("You can send only one message per 3 seconds"),
                )
        return HttpResponseRedirect(reverse_lazy("mainapp:contacts"))
```
* mainapp/templates/mainapp/contacts.html
```html
{% if form %}
<p>
<h3>Отправить сообщение в техподдержку</h3>
<form method="post">
  {% csrf_token %}
  {{ form|crispy }}
  <button type="submit" class="btn btn-primary btn-block">Отаправить</button>
</form>
</p>
{% endif %}
```
* запускаем celery паралельно с отладочным севером Django
* INFO - лог сообщения уровня INFO и выше
```
celery -A config worker -l INFO
```
* если все ок
```
celery@mack-wm ready.
```
* если необходимо очистить весь Redis
```
redis-cli FLUSHALL
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
