# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)
# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg



colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
user_colors = ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'пурпурный']


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

    points_lists[n_sides - 1].append(start_point)
    return points_lists


def triangle(start_point, angle, side_length):
    for points in point_gen(3, start_point, angle, side_length):
        sd.line(points[0], points[1], color=color, width=3)


def four_angle(start_point, angle, side_length):
    for points in point_gen(4, start_point, angle, side_length):
        sd.line(points[0], points[1], color=color, width=3)


def five_angle(start_point, angle, side_length):
    for points in point_gen(5, start_point, angle, side_length):
        sd.line(points[0], points[1], color=color, width=3)


def six_angle(start_point, angle, side_length):
    for points in point_gen(6, start_point, angle, side_length):
        sd.line(points[0], points[1], color=color, width=3)


def n_angle(n_points, start_point, angle, side_length):
    for points in point_gen(n_points, start_point, angle, side_length):
        sd.line(points[0], points[1], color=color, width=3)


print('Доступные цвета:')
for i, color in enumerate(user_colors):
    print(i, ':', color)

while True:
    user_color = input('Выберите цвет: ')
    if user_color.isdigit():
        color = colors[int(user_color)]
        break
    else:
        print('Цвет введен неверно!')

point_0 = sd.get_point(300, 100)
point_1 = sd.get_point(900, 100)
point_2 = sd.get_point(300, 350)
point_3 = sd.get_point(900, 350)
triangle(point_0, 0, 120)
four_angle(point_1, 20, 120)
five_angle(point_2, 50, 120)
six_angle(point_3, 80, 120)

sd.pause()
