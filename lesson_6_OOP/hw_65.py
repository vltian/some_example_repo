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


s1 = Stationery()
s1.draw()
s2 = Pen()
s2.draw()
s3 = Pencil()
s3.draw()
s4 = Handle()
s4.draw()
