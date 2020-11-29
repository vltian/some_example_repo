"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

def total_fab(x):
    fab_tot_qt = 0
    for _ in x:
        if _.name == "suit" or _.name == "coat":
            fab_tot_qt += _.fab_qt
        else:
            raise ValueError(f"Неопознанная шмотка - {_.name}")
    return round(fab_tot_qt, 2)


class Garment(ABC):
    def __init__(self, name, param):
        self.name = name
        self.param = param

class Suit(Garment):
    name = "suit"
    @property
    def fab_qt (self):
        return self.param * 2 + 0.3

class Coat(Garment):
    name = "coat"
    @property
    def fab_qt (self):
        return round((self.param / 6.5 + 0.5),2)

a = Suit("suit", 10)
b = Coat("coat", 20)
# c = Coat("sss", 15)
a1 = Suit("suit", 12)
b1 = Coat("coat", 55)
a2 = Suit("suit", 15)
b2 = Coat("coat", 80)
a3 = Suit("suit", 11)
b3 = Coat("coat", 100)
a4 = Suit("suit", 13)
b4 = Coat("coat", 200)
a5 = Suit("suit", 5)
b5 = Coat("coat", 70)
a6 = Suit("suit", 16)
b6 = Coat("coat", 85)

x = (a,b,a1,b1,a2,b2,a3,b3,a4,b4,a5,b5,a6,b6)
print (total_fab(x))

""" ТАК МНЕ КАЖЕТСЯ ПРОЩЕ """

def total_fab(x):
    fab_tot_qt = 0
    for _ in x:
            fab_tot_qt += _.fab_qt
    return round(fab_tot_qt, 2)

class Garment(ABC):
    def __init__(self, name, param):
        self.name = name
        self.param = param

    @property
    def fab_qt (self):
        if self.name == "suit":
            return self.param * 2 + 0.3
        elif self.name =="coat":
            return round((self.param / 6.5 + 0.5), 2)
        else:
            raise ValueError(f"Неопознанная шмотка - {self.name}")

class Item(Garment):
    def __init__(self, name, param):
        super().__init__(name, param)

a = Item("suit", 10)
b = Item("coat", 20)
a1 = Item("suit", 12)
b1 = Item("coat", 55)
a2 = Item("suit", 15)
b2 = Item("coat", 80)
a3 = Item("suit", 11)
b3 = Item("coat", 100)
a4 = Item("suit", 13)
b4 = Item("coat", 200)
a5 = Item("suit", 5)
b5 = Item("coat", 70)
a6 = Item("suit", 16)
b6 = Item("coat", 85)

x = (a, b, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5, a6, b6)
print(total_fab(x))