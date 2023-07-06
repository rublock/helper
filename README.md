# this

пример вызова this
```javascript
const data = 'text_data'

const dictData = {
    data: 'text_dictData',
    consoleLogInfo: function() {
        console.log(this.data) //text_dictData
        console.log(data) //text_data
    }
}

dictData.consoleLogInfo();
```

# Promise

пример Promise
```javascript
//базовый промис
const p = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log('Preparing data...')
        const data = '1123581321'
        resolve(data)
    }, 2000)
})

// этот коллбэк будет вызван только после выполнения resolve()
p.then(data => {
    console.log(`Data preparied ${data}`) //Data preparied 1123581321
})

//если нужно вызвать еще один промис, без глубокой вложенности
//удобно, что объект p можно передавать между функциями, модулями..
p.then(data => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('Modifying data...')
            data += ' fibonachi'
            resolve(data) //или если ошибка reject()
        }, 2000)
    })
}).then(data => {
    console.log(`Modified data ${data}`)//Modified data 1123581321 fibonachi
    return data //можно делать манипуляции с данными и возвращать их
}).catch(err => console.log('Error', err)) //обработка ошибки если reject()
  .finally(() => console.log('Finally')) //окончание скрипта
```