"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""
class Exc_int_type:
    def __init__(self, *args):
        self.text = args[0]


def check_int (a):
    if type(a) == "int" or "float":
        return (a)
    else:
        Exc_int_type("Это не число")


num_list = []
while True:
    try:
        x = int(input("введите элемент: "))
    except:

    try:
        num_list.append(int(x))
    except: Exception as err:
        print("Ошибка: ", err)
    finally:
        if x == "stop":
            break