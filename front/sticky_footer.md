### прилипающий футер
* html
```
<body>
   <div class="content">
      <p>I am content</p>
   </div>
   <div class="footer">
      <p>I am footer</p>
   </div>
</body>
```
* css
```
body,html {
   height: 100%;
}

body {
   display: flex;
   flex-direction: column;
}

.content {
   flex: 1 0 auto;
}

.footer {
   flex-shrink: 0;
}
```
