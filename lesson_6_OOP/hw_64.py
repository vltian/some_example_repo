"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print (f"{self.name} driving")

    def stop(self):
        print (f"{self.name} stopped")

    def turn(self, direction):
        self.direction = direction
        print (f"{self.name} turned {direction}")

    def show_speed(self):
        return (f"{self.name}: speed - {self.speed}")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print (f"{self.name}! speed exceeded")

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.name}! speed exceeded")

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

c1 = Car(60, "any", "CAR", False)
c1.go()
c1.stop()
c1.turn("not")
c1.show_speed()

c2 = TownCar(70, "red", "BMW", False)
print(f"{c2.name} is {c2.color}")
c2.go()
c2.show_speed()
c2.turn("right")

c3 = SportCar (50, "blue", "Ferrari", False)
print(f"{c3.name} is {c3.color}")
c3.go()
c3.stop()
c3.turn("left")

c4 = WorkCar(50, "black", "AUDI", False)
c4.go()
c4.show_speed()
c4.turn("left")

c5 = SportCar (50, "white", "HUMMER", True)
print(f"{c3.name} is {c3.color}")
c5.go()
c5.stop()
c5.turn("never")
