* HTMX to display an alert with the server response
```html
<!DOCTYPE html>
<html>
<head>
  <title>HTMX Example - Alert Server Response</title>
  <script src="https://unpkg.com/htmx.org/dist/htmx.js"></script>
</head>
<body>
  <h1>HTMX Example - Alert Server Response</h1>
  
  <form hx-post="/submit" hx-target="#result" hx-swap="innerHTML">
    <input type="text" name="name" placeholder="Enter your name">
    <button type="submit">Submit</button>
  </form>
  
  <div id="result" hx-trigger="load">
    <!-- Server response will be displayed here -->
  </div>
  
  <script>
    // Trigger an alert with the server response
    document.addEventListener('htmx:afterSettle', function (event) {
      if (event.detail.xhr.responseURL.endsWith('/submit')) {
        alert(event.detail.xhr.responseText);
      }
    });
  </script>
</body>
</html>
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
* 
```

```
* 
```

```
* 
```

```
