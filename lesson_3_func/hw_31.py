"""1.
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def div_2(d1, d2):
    try:
        d = d1/d2
        return d
    except ZeroDivisionError:
        return "Zero division error"

a = float(input ("Введите 2 числа: \na = "))
b = float(input ("b = "))
print (f"a/b = {div_2(a,b)}")

