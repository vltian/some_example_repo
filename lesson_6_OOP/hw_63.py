"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    income = {}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income

class Position(Worker):
    @property
    def get_full_name(self):
        return self.name, self.surname

    @property
    def get_total_income(self):
        income_tot = self.income.get("wage") + self.income.get("bonus")
        return income_tot

pos = Position("Вася", "Петров", "Директор", {"wage": 10, "bonus": 10})
print(f"ФИО - {pos.get_full_name[0]} {pos.get_full_name[1]}")
print(f"общий доход - {pos.get_total_income}")