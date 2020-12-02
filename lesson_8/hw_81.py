"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class Date:
    def __init__(self, date_str):
        self.date_str = date_str
    #
    @classmethod
    def conv_date(cls, date_sample):
        date_int = []
        for _ in date_sample.split("-"):
            date_int.append(int(_))
        return date_int

    @staticmethod
    def valid_date (d: list):
        if d[0] > 31:
            raise ValueError ("В месяцк слашком много дней")
        if d[1] > 12:
            raise ValueError ("В году слашком много месяцев")
        if d[2] < 2020:
            raise ValueError ("Этот год уже прошел")
        return d

date_sample = Date('10-11-2019')
print (date_sample.valid_date(date_sample.conv_date('33-11-20')))