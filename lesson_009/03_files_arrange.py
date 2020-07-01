# -*- coding: utf-8 -*-

import os, time, shutil, zipfile

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

from pprint import pprint

OUT_FOLDER = 'icons_by_year'


def get_from_zip():
    with zipfile.ZipFile('icons.zip', 'r') as z:
        return [file for file in z.namelist() if file[-1] != '/']


def get_from_folder(start_folder):
    files = []
    for dirpath, dirnames, filenames in os.walk(start_folder):
        for file in filenames:
            full_file_path = os.path.join(dirpath, file)
            files.append(full_file_path)
    return files


#########################################################################################
class Sorter:

    def __init__(self, start_folder, out_folder):
        self.start_folder = start_folder

        self.out_folder = out_folder
        self.date = None
        self.file = None
        self.path_to_copy = None
        self.file_list = None

    def get_date(self):
        gm_time = os.path.getmtime(self.file)
        self.date = time.gmtime(gm_time)

    def get_file_list(self):
        self.file_list = get_from_folder(self.start_folder)
        pass

    def make_dir(self):
        self.path_to_copy = os.path.join(OUT_FOLDER, str(self.date[0]), f'{self.date[1]:0>2}', str(self.date[2]))
        if not os.path.exists(self.path_to_copy):
            os.makedirs(self.path_to_copy)

    def copy_file(self):
        shutil.copy2(self.file, self.path_to_copy)

    def do_it(self):
        self.get_file_list()
        for self.file in self.file_list:
            self.get_date()
            self.make_dir()
            self.copy_file()


class ZipSorter(Sorter):

    def get_file_list(self):
        self.file_list = get_from_zip()

    def copy_file(self):
        with zipfile.ZipFile('icons.zip', 'r') as z:
            z.extract(self.file, path=self.path_to_copy)

    def get_date(self):
        with zipfile.ZipFile('icons.zip', 'r') as z:
            self.date = z.getinfo(self.file).date_time
            print(self.date)
         #    gm_time = os.path.getmtime(self.file)
         # time.gmtime(gm_time)


test = ZipSorter('icons', OUT_FOLDER)

test.do_it()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
