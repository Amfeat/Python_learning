# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
import os
import zipfile
from pprint import pprint

file_name = 'voyna-i-mir.txt'

# z_file = zipfile.ZipFile(
#     '/home/amfeat/PycharmProjects/Python_learning/lesson_009/python_snippets/voyna-i-mir.txt.zip', 'r'
# )
# for filename in z_file.namelist():
#     z_file.extract(filename)
#     file_name = filename
char_stat = {}
with open(file_name, 'r', encoding='cp1251') as file:
    lines_counter = 20
    for line in file:
        for char in line:
            if not char.isalpha():
                continue
            if char in char_stat:
                char_stat[char] += 1
            else:
                char_stat[char] = 1


table = reversed(sorted(char_stat.items(), key=lambda i: i[1]))


def print_table(items):
    print('+' + '-' * 10 + '+' + '-' * 10 + '+')
    print('|' + f'{"Буква": ^10}' + '|' + f'{"Частота": ^10}' + '|')
    total = 0
    for char, stat in items:
        total += stat
        print('+' + '-' * 10 + '+' + '-' * 10 + '+')
        print('|' + f'{char: ^10}' + '|' + f'{stat: ^10}' + '|')
    print('+' + '-' * 10 + '+' + '-' * 10 + '+')
    print('|' + f'{"ИТОГО:": ^10}' + '|' + f'{total: ^10}' + '|')
    print('+' + '-' * 10 + '+' + '-' * 10 + '+')


print_table(table)
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
