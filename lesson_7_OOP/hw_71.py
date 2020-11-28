"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, mtrx: list):
        self.mtrx = mtrx

    def __str__(self):
        global mtx_list
        mtx = ""
        mtx_list = []
        z = 0
        for i in range(len(self.mtrx)):
            line = []
            for j in range(len(self.mtrx[i])):
                t = str(self.mtrx[i][j])
                if len(t) > z:
                    z = len(t)
                line.append(t)
            mtx_list.append(line)
        for k in range (len(mtx_list)):
            for m in range (len(mtx_list[k])):
                l = z + 1 - len(mtx_list[k][m])
                mtx = mtx + f"{mtx_list[k][m]}{l*' '}"
            mtx = f"{mtx} \n"
        return mtx


    def __add__(self, other):
        ttl = []
        for i in range(len(self.mtrx)):
            c = []
            for j in range(len(self.mtrx[i])):
                c.append(self.mtrx[i][j] + other.mtrx[i][j])
            ttl.append(c)
        return ttl


f = [[1,2,3],[2,5,65],[7,88,9],[8,9,554],[2,254,7]]
m = [[2,4,60],[8,9,500],[26,4,7],[8,922,5],[2,4,7]]

d = Matrix(f)
e = Matrix(m)
h = Matrix(d+e)
print (h)