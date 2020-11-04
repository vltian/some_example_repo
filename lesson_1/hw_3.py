#hw3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input("Enter a number ")
sum_N = int(n) + int((f"{n}{n}")) + int (f"{n}{n}{n}")
print (f'Total sum "n+nn+nnn" = {sum_N}')