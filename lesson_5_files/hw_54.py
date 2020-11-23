""" 4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять"}

with open("my_3.txt",  encoding = "utf-8") as f_obj:
    new_file = []
    for line in f_obj:
        a = line.split(" — ")
        new_file.append(my_dict.get(a[0]) + " - " + a[1])
with open("my_3_rus.txt", "w", encoding = "utf-8") as f_obj1:
    for i in range(len(new_file)):
        print(str(new_file[i]), file=f_obj1, end='')