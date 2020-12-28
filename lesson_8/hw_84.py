"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


from abc import ABC, abstractmethod

class Store(ABC):
    def __init__ (self, items: list):
        self.items = items

class W_h(Store):
    pass

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

sc = Scanner(None, "Samsung", "S-111", "CHN", None, False, 300)
pr = Printer(None, "HP", "H-111", "CHN", None, False, True)
cp = Copier(None, "Xerox", "X-111", "CHN", None, False, False)
cp1 = Copier(None, "Xerox", "X-111", "CHN", None, False, False)
sc1 = Scanner(None, "Samsung", "S-111", "CHN", None, False, 300)
pr1 = Printer(None, "HP", "H-111", "CHN", None, False, True)
sc2 = Scanner(None, "Samsung", "S-111", "CHN", None, False, 300)
sc3 = Scanner(None, "Samsung", "S-111", "CHN", None, False, 300)
pr2 = Printer(None, "HP", "H-111", "CHN", None, False, True)
pr3 = Printer(None, "HP", "H-111", "CHN", None, False, True)
cp2 = Copier(None, "Xerox", "X-111", "CHN", None, False, False)
sc4 = Scanner(None, "Samsung", "S-111", "CHN", None, False, 300)
sc5 = Scanner(None, "Samsung", "S-111", "CHN", None, False, 300)
print(sc4.id, sc4.brand, sc.model, sc.origin, sc.resol)
print(sc4.c)
print(cp.id, cp.brand, cp.model, cp.origin, cp.laser)
print(cp2.c)
print(pr2.id, pr2.brand, pr2.model, pr2.origin, pr2.laser)
print(pr3.c)