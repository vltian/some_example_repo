"""3.
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# a = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
# b = int(input("Введите номер меясца: "))
# for i in range (0, len(a)):
#     if b == i + 1:
#         print (a[i])

""" Формирование list() и dict()
"""
a = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
a1 = a.copy()
for j in range (0, 2*len(a1), 2):
    a1.insert(j, int(j/2+1))
b = {a1[i]: a1[i + 1] for i in range(0, len(a1), 2)}


if input ("Выберите способ список - 1, словарь - 2: ") == "1":
    b = int(input("list() Введите номер месяца: "))
    for i in range (0, len(a)):
        if b == i + 1:
            print (a[i])
else:
    d = int(input("dict() Введите номер месяца: "))
    print (b.get(d))