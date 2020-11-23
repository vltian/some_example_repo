"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
with open("my_4.txt", 'r+', encoding="utf-8") as f_obj:
    """ построчный ввод фамилии и оклада, устранение пустых строк"""
    while True:
        txt_inp = input("Введите фамилию и оклад:")
        if txt_inp != "":
            if f_obj.tell() == 0:
                f_obj.writelines(txt_inp)
            else:
                f_obj.writelines('\n' + txt_inp)
        else:
            break
    f_obj.seek(0)
    """ создание словаря сотрудников с окладами"""
    def inf(x_str):
        a = x_str.split()
        inf_dict = dict(Name=a[0], Wage=int(a[1]))
        return inf_dict
    """ выбор малооплачиваемых и расчет среднего оклада """
    av_wage = 0
    len_list = 0
    for line in f_obj:
        b = inf(line)
        av_wage += b.get("Wage")
        len_list += 1
        if b.get("Wage") < 20000:
            print(b.get("Name"))
    try:
        print(av_wage/len_list)
    except ZeroDivisionError as err:
        print("Ошибка", err)