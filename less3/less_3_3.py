# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.


def my_func(arg_1, arg_2, arg_3):
    arg = sorted((arg_1, arg_2, arg_3))
    arg.pop(0)
    return arg[0] + arg[1]


print(my_func(10, 9, 2))
