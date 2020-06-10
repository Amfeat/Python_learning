# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

y = 500
x = 100

y2 = 450
x2 = 150
n_flakes = 1
x_points = [sd.random_number(1, 1200) for _ in range(n_flakes)]
y_points = [sd.random_number(500, 600) for _ in range(n_flakes)]
lengths = [sd.random_number(10, 50) for _ in range(n_flakes)]
# points = list(zip(x_points, y_points))
wind_speed = 0

while True:
    wind_speed += random.choice([1, -1])
    x_points.append(sd.random_number(1, 1200))
    y_points.append(sd.random_number(500, 600))
    lengths.append(sd.random_number(10, 50))

    # sd.clear_screen()
    for i, x_point in enumerate(x_points):

        if y_points[i] > 50:
            sd.start_drawing()
            point = sd.get_point(x_point, y_points[i])
            sd.snowflake(center=point, length=lengths[i], color=sd.background_color)
            y_points[i] -= 10
            x_points[i] += wind_speed * random.random()

        point = sd.get_point(x_points[i], y_points[i])
        sd.snowflake(center=point, length=lengths[i])

        if y_points[i] < 50:
            x_points.pop(i)
            y_points.pop(i)
            lengths.pop(i)
        if x_points[i] < -100 or x_points[i] > 1300:
            x_points.pop(i)
            y_points.pop(i)
            lengths.pop(i)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
