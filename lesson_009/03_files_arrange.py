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


class Sorter:

    def __init__(self, start_folder, out_folder):
        self.start_folder = start_folder

        self.out_folder = out_folder
        self.date = None
        self.file = None
        self.path_to_copy = None
        self.file_list = []

    def close_file(self):
        pass

    def get_date(self):
        pass

    def get_file_list(self):
        pass

    def make_dir(self):
        self.path_to_copy = os.path.join(OUT_FOLDER, str(self.date[0]), f'{self.date[1]:0>2}', f'{self.date[2]:0>2}')
        if not os.path.exists(self.path_to_copy):
            os.makedirs(self.path_to_copy)

    def copy_file(self):
        pass

    def do_it(self):
        self.get_file_list()
        for self.file in self.file_list:
            self.get_date()
            self.make_dir()
            self.copy_file()
        self.close_file()


class ZipSorter(Sorter):

    def __init__(self, start_folder, out_folder):
        super().__init__(start_folder, out_folder)
        self.z = zipfile.ZipFile(self.start_folder, 'r')

    def get_file_list(self):
        self.file_list = [file for file in self.z.namelist() if file[-1] != '/']

    def get_date(self):
        self.date = self.z.getinfo(self.file).date_time

    def copy_file(self):
        # print(self.path_to_copy)
        zip_file = self.z.getinfo(self.file)
        zip_file.filename = os.path.basename(zip_file.filename)
        self.z.extract(zip_file, path=self.path_to_copy)

    def close_file(self):
        self.z.close()


class FolderSorter(Sorter):

    def get_file_list(self):
        for dir_path, _, file_names in os.walk(self.start_folder):
            for file in file_names:
                full_file_path = os.path.join(dir_path, file)
                self.file_list.append(full_file_path)

    def get_date(self):
        gm_time = os.path.getmtime(self.file)
        self.date = time.gmtime(gm_time)

    def copy_file(self):
        shutil.copy2(self.file, self.path_to_copy)


# test = ZipSorter('icons.zip', OUT_FOLDER)
# test2 = FolderSorter('icons', OUT_FOLDER)
#
# test.do_it()
# test2.do_it()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
