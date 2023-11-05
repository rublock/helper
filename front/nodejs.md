* Создание Express сервера:
```
npm init -y
```
 
```
npm install express axios
```
* Создайте файл server.js
```
touch server.js
```
* добавьте следующий код:
```javascript
const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

app.use(express.static('public')); // Папка для статических файлов (HTML, CSS, JS)

app.get('/api/data', async (req, res) => {
  try {
    const apiResponse = await axios.get('https://jsonplaceholder.typicode.com/posts/1');
    res.json(apiResponse.data);
  } catch (error) {
    console.error('Ошибка при запросе к API:', error);
    res.status(500).json({ error: 'Ошибка при запросе к API' });
  }
});

app.listen(port, () => {
  console.log(`Сервер запущен на порту ${port}`);
});

```
* mkdir public && cd publick $$ touch index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Express Server with Axios</title>
</head>
<body>
  <h1>Express Server with Axios Example</h1>
  <button id="getData">Получить данные с API</button>
  <div id="result"></div>
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const getDataButton = document.getElementById('getData');
      const resultDiv = document.getElementById('result');

      getDataButton.addEventListener('click', function() {
        fetch('/api/data')
          .then(response => response.json())
          .then(data => {
            resultDiv.textContent = 'Данные с API: ' + JSON.stringify(data, null, 2);
          })
          .catch(error => {
            console.error('Ошибка при запросе к API:', error);
          });
      });
    });
  </script>
</body>
</html>

```
* Запуск сервера
```
node server.js
```

```
http://localhost:3000
```
* заменить строчку вашим API
```
const apiResponse = await axios.get('');
```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
* 
```

```
