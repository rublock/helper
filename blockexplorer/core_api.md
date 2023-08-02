## info
* `http://127.0.0.1:8000/` - django
* `http://127.0.0.1:3002/` - btc-rpc-explorer
* `offset` - сдвиг транзакций в запросе
* `http://127.0.0.1:3002/api/address/1GicDd3XUgowrkzmJCPo6MjoeR5GmWTjEQ` - пример запроса адреса
* `http://127.0.0.1:3002/api/tx/f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16` - пример запроса транзакции


## запуск btc-rpc-explorer для API

запускаем bitcoin core
```
bitcoind
```
ждем когда прогрузятся все транзакции

запускем electrum server
```
cd Git/electrs/ && ./target/release/electrs --log-filters INFO --db-dir ./db --electrum-rpc-addr="127.0.0.1:50001"
```
ждем пока проиндексируются все транзакции chain updated

запускаем btc-rpc-explorer
```
cd Git/NODEJS_btc-rpc-explorer-api/ && npm start
```
запускаем сервер Django
```
cd Git/Django_blockexplorer/ && . venv/bin/activate && python manage.py runserver
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
