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
from functools import reduce


def total_fab(name, qt)
    garm_qt = reduce(lambda x: x + self.fab_qt if name = "suit" else x + self.fab_qt1)
    return garm_qt


class Garment(ABC):
    def __init__(self, name):
        self.name = name


class Suit(Garment):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    @property
    def fab_qt (self):
        return self.h * 2 + 0.3


class Coat(Garment):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    @property
    def fab_qt1 (self):
        return self.v / 6.5 + 0.5