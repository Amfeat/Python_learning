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



class Water:
    def __str__(self):
        return 'Вода'

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __add__(self, other):
        if other == Air():
            return Storm()
        elif other == Fire():
            return Steam()
        elif other == Ground():
            return Dirt()
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __add__(self, other):
        if other == Water():
            return Storm()
        elif other == Fire():
            return Lightning()
        elif other == Ground():
            return Dust()
        else:
            return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __add__(self, other):
        if other == Air():
            return Lightning()
        elif other == Water():
            return Steam()
        elif other == Ground():
            return Lava()
        else:
            return None


class Ground:
    def __str__(self):
        return 'Земля'

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __add__(self, other):
        if other == Air():
            return Dust()
        elif other == Water():
            return Dirt()
        elif other == Fire():
            return Lava()
        else:
            return None


class Storm:
    def __str__(self):
        return 'Шторм'

    def __add__(self, other):
        return None


class Steam:
    def __str__(self):
        return 'Пар'

    def __add__(self, other):
        return None


class Dirt:
    def __str__(self):
        return 'Грязь'

    def __add__(self, other):
        return None


class Lightning:
    def __str__(self):
        return 'Молния'

    def __add__(self, other):
        return 3


class Dust:
    def __str__(self):
        return 'Пыль'

    def __add__(self, other):
        return None


class Lava:
    def __str__(self):
        return 'Лава'

    def __add__(self, other):
        return None


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
