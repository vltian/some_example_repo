"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""

from abc import ABC, abstractmethod

class Store(ABC):
    def __init__ (self, item = {}):
        self.item = item

class W_h(Store):
    def __init__(self, item):
        super().__init__(item)
        self.item = dict()
    def to_store(self, param):
        if self.item.setdefault(param.art) == None:
            self.item.setdefault(param.art)
            self.item[param.art] = 1
        else:
            self.item[param.art] += 1
        param.acptstore = True

    def to_dpt(self, art, qt):
        self.item[art] = self.item[art] - qt
        # param.dpt = dp_id

class Appliance:
    id = 0
    def __init__(self, id, art, brand, model, origin, dpt, acptstore):
        self.art = art
        self.brand = brand
        self.model = model
        self.origin = origin
        self.dpt = dpt
        self.acptstore = acptstore
        Appliance.id += 1

class Scanner(Appliance):
    c = 0
    def __init__(self, id, art, brand, model, origin, dpt, acptstore, resol):
        super().__init__(id, art, brand, model, origin, dpt, acptstore)
        self.resol = resol
        self.id = Appliance.id
        Scanner.c += 1

class Printer(Appliance):
    c = 0
    def __init__(self, id, art, brand, model, origin, dpt, acptstore, laser: bool):
        super().__init__(id, art, brand, model, origin, dpt, acptstore)
        self.laser = laser
        self.id = Appliance.id
        Printer.c += 1

class Copier(Appliance):
    c = 0
    def __init__(self, id, art, brand, model, origin, dpt, acptstore, laser: bool):
        super().__init__(id, art, brand, model, origin, dpt, acptstore)
        self.laser = laser
        self.id = Appliance.id
        Copier.c += 1

wh =W_h([])
print (type(wh.item))

x = int(input("Выберите тип оборудования (1 - принтер, 2 - сканер, 3 - ксерокс) : "))
br = input("Введите название производителя: ")
md = input("Введите модель: ")
art = str(input("Введите артикул модели: "))
orn = input("Введите страну произваодства: ")
if x == 1:
    ls = input("Тип принтера - лазерный (да - 1/нет - 0): ")
elif x == 2:
    rs = int(input("Введите разрешение: "))
else:
    rs = int(input("Введите разрешение: "))


qt = int(input("Введите размер партии: "))
for _ in range(qt):
    if x == 1:
        sc = [Printer(None, art, br, md, orn, None, False, ls)]
    elif x == 2:
        sc = [Scanner(None, art, br, md, orn, None, False, rs)]
    else:
        sc = [Copier(None, art, br, md, orn, None, False, rs)]
    wh.to_store(sc[0])

art1 = str(input("Введите артикул модели для передачи в отдел: "))
dpt1 = str(input("Введите отдел: "))
qt1 = int(input("Введите размер партии: "))

wh.to_dpt(art1, qt1)

art = str(input("Введите артикул модели: "))
qt = int(input("Введите размер партии: "))
for _ in range(qt):
    if x == 1:
        sc1 = [Printer(None, art, br, md,  orn, None, False, ls)]
    elif x == 2:
        sc1 = [Scanner(None, art, br, md, orn, None, False, rs)]
    else:
        sc1 = [Copier(None, art, br, md, orn, None, False, rs)]
    wh.to_store(sc1[0])

art = str(input("Введите артикул модели: "))
qt = int(input("Введите размер партии: "))
for _ in range(qt):
    if x == 1:
        sc2 = [Printer(None, art, br, md,  orn, None, False, ls)]
    elif x == 2:
        sc2 = [Scanner(None, art, br, md, orn, None, False, rs)]
    else:
        sc2 = [Copier(None, art, br, md, orn, None, False, rs)]
    wh.to_store(sc2[0])

print (f"Остатки на складе: {wh.item.items()}")



