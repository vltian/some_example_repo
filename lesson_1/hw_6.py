#hw6
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.

a = int(input("a= "))
b = int(input("b= "))
day = 1
while a < b:
    a = a * 1.1
    day = day + 1

print (f"на {day}-й день спортсмен достиг результата — не менее {b} км/день.")