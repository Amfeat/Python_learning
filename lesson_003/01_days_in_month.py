# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом


while True:
    user_input = input("Введите, пожалуйста, номер месяца: ")
    if user_input.isdigit():
        month = int(user_input)
        if 1 <= month <= 12:
            print('Вы ввели', month)
            break
    print('Неправильный ввод, повторите!')
if month in [1, 3, 5, 7, 8, 10, 12]:
    n_days = 31
elif month == 2:
    n_days = 28
else:
    n_days = 30
print('В этом месяце', n_days, 'дней!')
