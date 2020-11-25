"""5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def draw(self, phrase="Запуск отрисовки"):
        print(phrase)

class Pen(Stationery):
    def draw(self):
        return (f"{super().draw('Напиши что-нибудь')}")

class Pencil(Stationery):
    def draw(self):
        super().draw("Нарисуй что-нибудь")

class Handle(Stationery):
    def draw(self):
        print("Выдели что-нибудь")


S1 = Stationery()
S1.draw()
S2 = Pen()
S2.draw()
S3 = Pencil()
S3.draw()
S4 = Handle()
S4.draw()
