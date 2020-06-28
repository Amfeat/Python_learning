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


class Parser:

    def __init__(self, filename, out_name):
        self.filename = filename
        self.out_file = out_name
        self.prev_date = None
        self.file = None
        self.line = None
        self.nok_counter = 0

    def do_it(self):
        file = open(self.filename)
        for line in file:
            self.line = line
            date, status = self._get_lines()
            self.group_lines(date, status)
        self.group_lines("None", None)
        file.close()

    def _get_lines(self):
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

        with open(self.out_file, mode='a') as file:
            file.write(out)


class MinuteParser(Parser):
    def _get_lines(self):
        date = self.line[:17] + ']'
        status = self.line[-4:-1]
        return date, status


class HourParser(Parser):
    def _get_lines(self):
        date = self.line[:14] + ']'
        status = self.line[-4:-1]
        return date, status


class MonthParser(Parser):
    def _get_lines(self):
        date = self.line[:8] + ']'
        status = self.line[-4:-1]
        return date, status


class YearParser(Parser):
    def _get_lines(self):
        date = self.line[:5] + ']'
        status = self.line[-4:-1]
        return date, status


log = MinuteParser(f_name, 'out_minute.txt')
log.do_it()

h_log = HourParser(f_name, 'out_hour.txt')
h_log.do_it()

h_log = MonthParser(f_name, 'out_month.txt')
h_log.do_it()

y_log = YearParser(f_name, 'out_year.txt')
y_log.do_it()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
