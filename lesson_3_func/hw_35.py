"""5.
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу.
"""

""" Ввод строки чисел, формирование списка символов """
def inp():
    a = input ("Введите строку чисел: ")
    simb_l = list(a)
    return simb_l

""" Проверка списка символов на прерывание, создание итогового списка чисел-строк для суммирования """
def intrpt (simb_l):
    c = len(simb_l)
    for i in range(0,len(simb_l)):
        if simb_l[i] == x:
            c = i
            break
    simb_x = (simb_l[0:c:])
    b1 = ''.join(simb_x)
    b2 = b1.split()
    return b2

""" Подсчет суммы. Аргумент - список чисел-строк"""
def summa (str):
    s = 0
    for j in range(0, len(str)):
        s = s + int(str[j])
    return s

s_sum = 0
x = input("Введите символ прерывания: ")
s = inp()
while True:
    s_temp = ''.join(s)
    str_fin = intrpt(s)
    s_sum = s_sum + summa(str_fin)
    print(s_sum)
    if s_temp.find(x) == -1:
        s = inp()
    else:
        break

# l = []
# for j in range(0, len(simb_x)):
#     k = int(simb_x[j])
#     l[j].append(k)
# print (sum(l))

#     for i in range (0, len(list_a)):
#         if a[i] == "n":
#             c = a[0:i:]
#             b = c.split()
#             return ('the end')
#         else:
#             c = a
#             b = c.split()
#     for j in range(0, len(b)):
#         s = s + int(b[i])
#     return (s)
# print(inp())
