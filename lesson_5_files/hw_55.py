""" 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random
with open("numb.txt", "r+") as f_obj:
    "генерация набора чисел"
    for _ in range(10):
        x = str(random.randint(1,100))
        f_obj.write(x + ' ')
    f_obj.seek(0)
    "генерация набора чисел"
    num = 0
    for y in f_obj:
        b = y.split()
        for i in range(len(b)):
            num += int(b[i])
    print(num)