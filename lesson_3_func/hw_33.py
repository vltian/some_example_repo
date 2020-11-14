"""3.
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""
def my_func(*args):
    result_list = list(args)
    sum_max = 0
    for i in (1, 2):
        sum_max = sum_max + max (result_list)
        result_list.pop(result_list.index(max (result_list)))
    return sum_max

x = my_func(5000, 100, 10000)
print (x)