#hw4
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_num = int(input("Enter a whole positive number: "))
a = user_num % 10
b = user_num // 10
max = a
while b > 1:
    a = b % 10
    b = b // 10
    if a > max:
        max = a
print (f"Самое большое число равно {max}")