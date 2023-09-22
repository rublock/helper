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
* удалить таблиу
```
DROP TABLE table;
```
* посмотреть таблицу
```
\d table_name
```
* вставить данные в таблицу
```sql
INSERT INTO table (id)
VALUES (1);
```
```sql
ALTER TABLE employees
ADD COLUMN email VARCHAR(255);
```
* посмотреть таблицу
```
SELECT * FROM table;
```
* создаем связи между таблицами
```sql
CREATE TABLE table1 (
        id SERIAL PRIMARY KEY,
        some_data TEXT 
);
```
```sql
CREATE TABLE table2 (
    id SERIAL PRIMARY KEY,
    from_table1 BIGINT NOT NULL,
    FOREIGN KEY (from_table1) REFERENCES table1(id)
);
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
