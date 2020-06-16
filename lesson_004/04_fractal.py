# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
v = 1


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


# def draw_branches(start_point, angle, length):
#     v1 = sd.get_vector(start_point, angle, length)
#     v1.draw()
#     v2 = sd.get_vector(v1.end_point, angle + 30, length * 0.75)
#     v2.draw()
#     v3 = sd.get_vector(v1.end_point, angle - 30, length * 0.75)
#     v3.draw()


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


def draw_branches(start_point, angle, length):
    if length < 8:
        return
    v1 = sd.get_vector(start_point, angle, length)
    v1.draw()
    draw_branches(v1.end_point, angle - 35, length * 0.8)
    draw_branches(v1.end_point, angle + 35, length * 0.8)
    draw_branches(v1.end_point, angle, length * 0.8)


# draw_branches(start_point=root_point, angle=90, length=100)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

def draw_random_branches(start_point, angle, length):
    global v
    v += 1
    # print('vetki =', v)
    color = (125, 78, 8)
    width = int(length / 10)
    if width < 1:
        width = 1
    if length < 40:
        color = (66, 80, 0)
        if length < 9.5:
            # color = (0, sd.random_number(150, 255), 0)
            color = sd.random_color()
            width = 10

            if length < 9:
                return
    v1 = sd.get_vector(start_point, angle, length, width=width)
    v1.draw(color)
    for i in range(sd.random_number(1, 2)):
        draw_random_branches(v1.end_point, angle - sd.random_number(25, 40), length * sd.random_number(65, 75) / 100)
        draw_random_branches(v1.end_point, angle + sd.random_number(25, 40), length * sd.random_number(65, 75) / 100)
    draw_random_branches(v1.end_point, angle + sd.random_number(-15, 15), length * sd.random_number(75, 90) / 100)


root_point = sd.get_point(600, 30)
root_point_1 = sd.get_point(400, 30)
root_point_2 = sd.get_point(800, 30)

draw_random_branches(start_point=root_point, angle=90, length=100)
# draw_branches(start_point=root_point_1, angle=90, length=80)
# draw_random_branches(start_point=root_point, angle=90, length=80)
#
# Пригодятся функции
# sd.random_number()
print(v)
sd.pause()
