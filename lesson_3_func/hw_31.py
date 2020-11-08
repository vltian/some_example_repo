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

# a = float(input ("Введите 2 числа: \na = "))
# b = float(input ("b = "))
# print (f"a/b = {round(div_2 (a,b),2)}")

# def div_2(d1, d2):
#     if d2 == 0:
#         return "Zero division error"
#     else:
#         return d1/d2
# a = float(input ("Введите 2 числа: \na = "))
# b = float(input ("b = "))
# print (div_2 (a,b))

