""" 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("my_2.txt", 'x', encoding="utf-8") as f_obj:
    while True:
        txt_inp = input(":")
        if txt_inp != "":
            if f_obj.tell() == 0:
                f_obj.writelines(txt_inp)
            else:
                f_obj.writelines('\n' + txt_inp)
        else:
            break