#hw5
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int (input("Enter your revenue - "))
cost = int (input("Enter your costs - "))
res = revenue - cost
if res < 0:
        print(f"Loss is {res}")
elif res == 0:
        print ("Zero")
else:
        print (f"Profit is {res}")
        prof_ty = res * 100 / revenue
        print (f"Your profitability is {round(prof_ty, 2)} %")
        pers = int (input("Enter personnel number - "))
        prof_pers = res/pers
        print (f"Profit per person is {round(prof_pers, 2)}")