# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if other == Air:
            return Storm()


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if other == Air:
            return Stom()


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if other == Air:
            return Stom()


class Ground:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if other == Air:
            return Stom()


class Storm:
    def __str__(self):
        return 'Шторм'

    def __add__(self, other):
        if other == Air:
            return Stom()


class Steam:
    def __str__(self):
        return 'Пар'

    def __add__(self, other):
        if other == Air:
            return Stom()


class Dirt:
    def __str__(self):
        return 'Грязь'

    def __add__(self, other):
        if other == Air:
            return Stom()


class Lightning:
    def __str__(self):
        return 'Молния'

    def __add__(self, other):
        if other == Air:
            return Stom()


class Dust:
    def __str__(self):
        return 'Пыль'

    def __add__(self, other):
        if other == Air:
            return Stom()


class Lava:
    def __str__(self):
        return 'Лава'

    def __add__(self, other):
        if other == Air:
            return Stom()

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
