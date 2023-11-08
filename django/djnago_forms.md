## Работа с формами

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
```
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
