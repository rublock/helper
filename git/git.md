## Git

``` 
sudo apt install git
```
* проверить есть ли ssh ключи на компьютере
```
cd .ssh && cat ./id_rsa.pub
```

* сгенерировать ssh ключ + копируем ключь и вставляем на github
```
ssh-keygen && cd .ssh/ && cat ./id_rsa.pub
```
* говорим гиту кто мы
```
git config --global user.email "hypermail@yandex.ru" && git config --global user.name "mack"
```
* запросить данные с удаленного репозитория и сравнить
```
git fetch && git status
```
* добавить все файлы и закомитить и запушить
```
git add . && git commit -am '' && git push
```
* стянуть ветку из пулл-реквеста
```
git fetch origin pull/9/head:[branch_name] && git switch [branch_name]
```
* скопировать репозиторий с Git через ssh
```
git clone [git link]
```
* создать ветку и переключиться
```
git checkout -b [yourbranchname]
```
* удаляет все локальные изменения
```
git stash -u
```
* создать такую же ветку на удаленном репозитории и отправить
```
git push -u origin master
```
* просмотреть все вести
```
git branch -a
```
* удалить локальную ветку
```
git branch -d [local_branch_name]
```
* удалить последний коммит в локальной ветке
```
git reset HEAD~1
```
* пуш если нет такой ветки на удаленном репозитории
```
git push --set-upstream origin [local_branch_name]
```
* вернуться в состояние удаленной ветки
```
git reset --hard origin/[branch_name]
```
* вывести все коммиты
```
git log --oneline
```
* если коммитим с нового устройства, то нужно задать имя
```
git config --global user.name [user name]
```
* или
```
git config --global user.email [user email]
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
