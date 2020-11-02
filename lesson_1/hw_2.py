#hw2
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_sec = int(input ("Enter your time in sec"))
hours = time_sec // 3600
minutes = (time_sec % 3600)//60
seconds = (time_sec % 3600) % 60
time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
print (time_str)