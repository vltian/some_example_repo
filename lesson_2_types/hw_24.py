"""4.
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

a = input("Введите строку: ").split()
for i in range (0, len(a)):
    string = a[i][0:10:]
    print (f"{i+1}. {string}")