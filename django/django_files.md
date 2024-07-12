### Work with files in Django

```python
uploaded_file = request.FILES['file']
fs = FileSystemStorage(location=settings.MEDIA_ROOT)
fs.save(uploaded_file.name, uploaded_file)
```