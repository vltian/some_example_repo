"""7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class Complex_num:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return (f"{self.a}" if self.b == 0 else (f"{self.a}+{self.b}*i" if self.b > 0 else f"{self.a}{self.b}*i"))

    def __mul__(self, other):
        return Complex_num((self.a * other.a - self.b*other.b), (self.a * other.b + other.a * self.b))
    def __add__(self, other):
        return Complex_num((self.a + other.a), (self.b + other.b))

x = Complex_num(10, 50)
y = Complex_num(8, -50)

print (x + y)
print (type(x + y))
print (x * y)
print (type(x*y))