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

# import os
# import zipfile

# z_file = zipfile.ZipFile(
#     '/home/amfeat/PycharmProjects/Python_learning/lesson_009/python_snippets/voyna-i-mir.txt.zip', 'r'
# )
# for filename in z_file.namelist():
#     z_file.extract(filename)
#     file_name = filename

file_name = 'voyna-i-mir.txt'


class SortCharTable:

    def __init__(self, file_name):
        self.file_name = file_name
        self.char_stat = {}

    def make_stat(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if not char.isalpha():
                        continue
                    if char in self.char_stat:
                        self.char_stat[char] += 1
                    else:
                        self.char_stat[char] = 1

    def print_table(self, sort_by='count', rev=True):
        table = self.sort_table(sort_by, rev)
        print('+' + '-' * 10 + '+' + '-' * 10 + '+')
        print('|' + f'{"Буква": ^10}' + '|' + f'{"Частота": ^10}' + '|')
        total = 0
        for char, stat in table:
            total += stat
            print('+' + '-' * 10 + '+' + '-' * 10 + '+')
            print('|' + f'{char: ^10}' + '|' + f'{stat: ^10}' + '|')
        print('+' + '-' * 10 + '+' + '-' * 10 + '+')
        print('|' + f'{"ИТОГО:": ^10}' + '|' + f'{total: ^10}' + '|')
        print('+' + '-' * 10 + '+' + '-' * 10 + '+')

    def sort_table(self, sort_by='count', rev=True):
        if sort_by == 'count':
            if rev:
                return reversed(sorted(self.char_stat.items(), key=lambda i: i[1]))
            if not rev:
                return sorted(self.char_stat.items(), key=lambda i: i[1])


tolstoy = SortCharTable(file_name)
tolstoy.make_stat()
tolstoy.print_table(rev=False)

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
