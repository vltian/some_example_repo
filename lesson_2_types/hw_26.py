"""6.
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}), (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{“название”: [“компьютер”, “принтер”, “сканер”], “цена”: [20000, 6000, 2000], “количество”: [5, 2, 7], “ед”: [“шт.”]}
"""

"""  Ввод исходных данных """
spec = []
n_spec = int(input("Введите кол-во позиций для ввода: "))
for i in range (0, n_spec):
    Name = input("Название - ")
    Price = float(input("Цена - "))
    Qt = int(input("Кол-во - "))
    Item = input("ед. - ")
    spec.append((i+1, {"Название": Name,  "Цена": Price, "Кол-во": Qt, "ед.": Item}))
print (spec)

""" данные для быстрого тестирования """
# spec = [(1, {'Название': 'aaaa', 'Цена': 100.0, 'Кол-во': 1, 'ед.': 'a'}), (2, {'Название': 'ssss', 'Цена': 200.0, 'Кол-во': 2, 'ед.': 's'})]

""" Выделить данные по позиции """
pos = []
for i in range (0, len(spec)):
    pos.append(spec[i][1])

""" Сформировать список параметров """
params = []
params = list(spec[1][1].keys())

""" Перебор параметров/выборки списка значений по каждому """
p = []
param_value = []
for j in range(0, len(params)):
    k = params[j]
    p = []
    for m in range(0, len(pos)):
        p.append(pos[m].get(k))
    param_value.append(p)

""" Слияние данных """
w = zip (params, param_value)
analitics = dict(w)

print (analitics)
