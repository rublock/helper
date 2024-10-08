#### Кодирование длин серий — это базовый алгоритм сжатия данных.

В этой задаче мы реализуем одну из самых простых его вариантов.

На вход алгоритму подаётся строка, содержащая символы латинского алфавита. Эта строка разбивается на группы одинаковых символов, идущих подряд ("серии"). Каждая серия характеризуется повторяющимся символом и количеством повторений. Именно эта информация и записывается в код: сначала пишется длина серии повторяющихся символов, затем сам символ. У серий длиной в один символ количество повторений будем опускать.

Например, рассмотрим строку

aaabccccCCaB
Разобъём её на серии
aaa b cccc CC a B
После чего закодируем серии и получим итоговую строку, которую и будем считать результатом работы алгоритма.
3ab4c2CaB
Формат ввода:
Одна строка, содержащая произвольные символы латинского алфавита.

Формат вывода:
Строка, содержащая закодированную последовательность.

Sample Input 1:
```
aaabccccCCaB
```
Sample Output 1:
```
3ab4c2CaB
```
Sample Input 2:
```
a
```
Sample Output 2:
```
a
```
```python

text = 'aaabccccCCaB'

count = 1

for i in range(0, len(text)):
    if i + 1 < len(text) and text[i] == text[i+1]:
        count += 1
    else:
        if count == 1:
            print(text[i], end='')
            count = 1
        else:
            print(str(count) + text[i], end='')
            count = 1
#3ab4c2CaB
```
Дано натуральное число 
n
n. Напишите программу, которая печатает численный треугольник с высотой равной 
n
n, в соответствии с примером:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
```python
input = int(input('>>>'))
count = 0
for i in range(input):
    for _ in range(i + 1):
        count += 1
        print(f'{count} ', end='')
    print()
    
```
