# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


user_figures = ['треугольник', 'квадрат', 'пятиугольник', 'шестиугольник', 'семиугольник']
figures = [3, 4, 5, 6, 7]


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


def n_angle(n_points, start_point, angle, side_length):
    for points in point_gen(n_points, start_point, angle, side_length):
        sd.line(points[0], points[1], width=3)


print('Доступные фигуры:')
for i, figure in enumerate(user_figures):
    print(i, ':', figure)

while True:
    user_figure = input('Выберите номер фигуры: ')
    if user_figure.isdigit():
        if int(user_figure) <= len(figures)-1:
            figure = figures[int(user_figure)]
            break

    print('Номер введен неверно!')

point_0 = sd.get_point(200, 200)

n_angle(figure, point_0, 0, 200)

sd.pause()
