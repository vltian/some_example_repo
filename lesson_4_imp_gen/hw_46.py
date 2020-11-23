"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

def w_n(a, end):
    for el in count(a):
        if el == end:
            break
        else:
            yield (el)

def r_el (b, end):
    cnt = 0
    for el in cycle (b):
        if cnt == end:
            break
        else:
            yield (el)
        cnt += 1

""" Целые числа """
print(w_n (int(input("Введите точку отсчета  - ")), int(input("Введите условие окончания цикла - "))))

""" Повторения """
print(r_el([input("Введите набор элементов - ")], int(input("Введите условие окончания цикла - "))))