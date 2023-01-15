def decorator(decorator_arg):
    def inner_decorator(func):
        def wrapper(*args, **kwargs): # принимает любое кол-во любых параметров или ничего
            func(*args, **kwargs)
            print('Данные из декоратора')
            print(decorator_arg) # принимает аргумент из декоаратора @decorator('Аргумент декоратора')
        return wrapper
    return inner_decorator

@decorator('Аргумент декоратора') #декорирование функции, добавление нового функционала с аргументом
def foo(arg):
    print(f'{arg}')

foo('Агрументы функции') # Агрументы функции
                         # Данные из декоратора
                         # Аргумент декоратора
