my_string = input()  # Ввод пользователя
print(len(my_string))  # Вывод длины строки
print(my_string.upper())  # Вывод строки в верхнем регистре
print(my_string.lower())  # Вывод строки в нижнем регистре
print(my_string.replace(" ", ""))  # Удаление пробелов
print(my_string.split(my_string[1])[0])  # Вывод первого символа строки
print(my_string.split(my_string[-2])[-1])  # Вывод последнего символа строки
