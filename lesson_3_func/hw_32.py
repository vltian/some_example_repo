"""2.
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""
def pers_file (n, f, y, c, e, t):
    stroka = f"Имя - {n.title()} {f.title()}, год рождения - {y}, город рождения - {c.title()}, email - {e}, телефон - {t}."
    return stroka
n = input("Name - ")
f = input("Surname - ")
y = input("Year - ")
c = input("City - ")
e = input("email - ")
t = input("Tel. - ")
print (pers_file (n, f, y, c, e, t))