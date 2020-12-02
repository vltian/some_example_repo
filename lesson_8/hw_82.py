"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class Exc_DivZero (Exception):
    def __init__(self, *args, **kwargs):
        self. text = args[0]



def div(a,b):
    if b == 0:
        raise Exc_DivZero("Деление на 0!")
    else:
        return a/b

x = int(input ("делимое: "))
y = int(input ("делитель: "))

try:
    print (round(div(x, y), 2))
except Exception as err:
    print("Ошибка: ", err)