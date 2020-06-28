# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
import io

f_name = 'events.txt'


class GroupLog:

    def __init__(self, filename):
        self.filename = filename
        self.prev_date = None
        self.file = None
        self.line = None
        self.nok_counter = 0

    def do_it(self):
        file = open(self.filename)
        for line in file:
            self.line = line
            date, status = self.get_lines()
            self.group_lines(date, status)
        self.group_lines("None", None)
        file.close()

    def get_lines(self):
        date = self.line[:17] + ']'
        status = self.line[-4:-1]
        return date, status

    def group_lines(self, date, status):
        if self.prev_date is None:
            self.prev_date = date

        if date == self.prev_date:
            if status != ' OK':
                self.nok_counter += 1
        else:
            if self.nok_counter > 0:
                self.write_file()
                self.nok_counter = 0
            if status != ' OK':
                self.nok_counter += 1
            self.prev_date = date

    def write_file(self):
        print(self.prev_date, self.nok_counter)
        out = self.prev_date + ' ' + str(self.nok_counter) + '\n'

        with open('out.txt', mode='a') as file:
            file.write(out)

    def get_params(self):
        pass


log = GroupLog(filename=f_name)
log.do_it()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
