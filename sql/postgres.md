### PostgreSQL

```
sudo apt update
```
```
sudo apt install postgresql
```
* БД создается с дефолтным пользователем postgres
* запускаем консоль от имени пользователя postgres
```
sudo -u postgres psql
```
* посмотреть все БД
```
\l
```
* посмотреть всех пользователей
```
\du
```
* создать БД
```
CREATE DATABASE db_name;
```
* зайти под БД
```
\c db_name
```
* список таблиц БД
```
\d
```
* создать таблицу
```
CREATE TABLE table (id SERIAL);
```
* посмотреть таблицу
```
\d table_name
```
* вставить данные в таблицу
```
INSERT INTO table (id)
VALUES (1);
```
* посмотреть таблицу
```
SELECT * FROM table;
```
* создаем связи между таблицами
```sql
CREATE TABLE table1 (
	id SERIAL
	some_data TEXT,
)

CREATE TABLE table2 (
	id SERIAL
	from_table1 BIGINT unsigned not null,

	FOREIGN KEY (from_table1) references table1(id)
)
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
