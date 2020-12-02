"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
""" 5 """

from abc import ABC, abstractmethod

class Store(ABC):
    def __init__ (self, item: list):
        self.item = item

class W_h(Store):
    def __init__(self, item):
        super().__init__(item)
        self.item = []

    def to_store(self, param):
        self.item.append(param.id)
        param.acptstore = True

    def to_dpt(self, param, dp_id):
        del self.item[param.id - 1]
        param.dpt = dp_id

class Appliance:
    id = 0
    def __init__(self, id, brand, model, origin, dpt, acptstore):
        self.brand = brand
        self.model = model
        self.origin = origin
        self.dpt = dpt
        self.acptstore = acptstore
        Appliance.id += 1

class Scanner(Appliance):
    c = 0
    def __init__(self, id, brand, model, origin, dpt, acptstore, resol):
        super().__init__(id, brand, model, origin, dpt, acptstore)
        self.resol = resol
        self.id = Appliance.id
        Scanner.c += 1

class Printer(Appliance):
    c = 0
    def __init__(self, id, brand, model, origin, dpt, acptstore, laser: bool):
        super().__init__(id, brand, model, origin, dpt, acptstore)
        self.laser = laser
        self.id = Appliance.id
        Printer.c += 1

class Copier(Appliance):
    c = 0
    def __init__(self, id, brand, model, origin, dpt, acptstore, laser: bool):
        super().__init__(id, brand, model, origin, dpt, acptstore)
        self.laser = laser
        self.id = Appliance.id
        Copier.c += 1


wh =W_h([])
sc = Scanner(None , "Samsung", "S-111", "CHN", None, False, 300)
sc1 = Scanner(None, "Samsung", "S-111", "CHN", None, False, 300)
wh.to_store(sc)
wh.to_store(sc1)

print (wh.item)
wh.to_dpt(sc1, input("Dpt id: "))
print (wh.item)
print(sc1.id, sc1.brand, sc1.model, sc1.origin, sc1.resol, sc1.acptstore, sc1.dpt)
print(sc1.c)
