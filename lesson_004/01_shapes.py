# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны

#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg
#

# point_0 = sd.get_point(300, 100)
# point_1 = sd.get_point(900, 100)
# point_2 = sd.get_point(300, 350)
# point_3 = sd.get_point(900, 350)
#
#
# def triangle(start_point, angle, side_length):
#     v1 = sd.get_vector(start_point=start_point, angle=angle, length=side_length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=side_length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120 + 120, length=side_length, width=3)
#     v3.draw()
#
#
# def four_angle(start_point, angle, side_length):
#     v1 = sd.get_vector(start_point=start_point, angle=angle, length=side_length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=side_length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 90 + 90, length=side_length, width=3)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 90 + 90 + 90, length=side_length, width=3)
#     v4.draw()
#
#
# def five_angle(start_point, angle, side_length):
#     v1 = sd.get_vector(start_point=start_point, angle=angle, length=side_length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=side_length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 72 + 72, length=side_length, width=3)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 72 + 72 + 72, length=side_length, width=3)
#     v4.draw()
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 72 + 72 + 72 + 72, length=side_length, width=3)
#     v5.draw()
#
#
# def six_angle(start_point, angle, side_length):
#     v1 = sd.get_vector(start_point=start_point, angle=angle, length=side_length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=side_length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 60 + 60, length=side_length, width=3)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 60 + 60 + 60, length=side_length, width=3)
#     v4.draw()
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 60 + 60 + 60 + 60, length=side_length, width=3)
#     v5.draw()
#     v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 60 + 60 + 60 + 60 + 60, length=side_length, width=3)
#     v6.draw()
#
#
# triangle(point_0, 0, 120)
# four_angle(point_1, 20, 120)
# five_angle(point_2, 50, 120)
# six_angle(point_3, 80, 120)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


def point_gen(n_sides, start_point, angle, side_length):
    points_lists = [[start_point]]
    next_point = start_point
    next_angle = angle
    for i in range(n_sides - 1):
        vector = sd.get_vector(start_point=next_point, angle=next_angle, length=side_length, width=3)
        next_point = vector.end_point
        next_angle = next_angle + (360 / n_sides)
        points_lists.append([])
        points_lists[i].append(next_point)
        points_lists[i + 1].append(next_point)

    points_lists[n_sides-1].append(start_point)
    return points_lists


def triangle(start_point, angle, side_length):
    for points in point_gen(3, start_point, angle, side_length):
        sd.line(points[0], points[1], color=sd.COLOR_YELLOW, width=3)


def four_angle(start_point, angle, side_length):
    for points in point_gen(4, start_point, angle, side_length):
        sd.line(points[0], points[1], color=sd.COLOR_YELLOW, width=3)


def five_angle(start_point, angle, side_length):
    for points in point_gen(5, start_point, angle, side_length):
        sd.line(points[0], points[1], color=sd.COLOR_YELLOW, width=3)


def six_angle(start_point, angle, side_length):
    for points in point_gen(6, start_point, angle, side_length):
        sd.line(points[0], points[1], color=sd.COLOR_YELLOW, width=3)


def n_angle(n_points, start_point, angle, side_length):
    for points in point_gen(n_points, start_point, angle, side_length):
        sd.line(points[0], points[1], color=sd.COLOR_YELLOW, width=3)


point_0 = sd.get_point(300, 100)
point_1 = sd.get_point(900, 100)
point_2 = sd.get_point(300, 350)
point_3 = sd.get_point(900, 350)
# triangle(point_0, 0, 120)
four_angle(point_1, 20, 120)
five_angle(point_2, 50, 120)
six_angle(point_3, 80, 120)
n_angle(10, point_0, 0, 100)

sd.pause()
