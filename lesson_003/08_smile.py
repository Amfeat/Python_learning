# -*- coding: utf-8 -*-

# (определение функций)
import random

import simple_draw as sd

sd.resolution = (1200, 600)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color=(255, 200, 0), radius=200):
    center = sd.get_point(x, y)
    detalization = 50

    # radius = 100
    # color = (255, 200, 0)

    # body
    step = radius // detalization
    body_radius = radius
    for _ in range(detalization):
        sd.circle(center, radius=body_radius, color=color, width=step)
        body_radius -= step
        color = full_gradient(color, detalization)
    sd.circle(center, radius=body_radius, color=color, width=0)
    # eyes
    # ellipse(left_bottom, right_top, color=COLOR_YELLOW, width=0)
    left_bottom = sd.get_point(x - radius * 0.30, y + radius * 0.20)
    right_top = sd.get_point(x - radius * 0.1, y + radius * 0.60)
    sd.ellipse(left_bottom, right_top, color=sd.COLOR_BLACK, width=0)
    left_bottom = sd.get_point(x + radius * 0.10, y + radius * 0.20)
    right_top = sd.get_point(x + radius * 0.3, y + radius * 0.60)
    sd.ellipse(left_bottom, right_top, color=sd.COLOR_BLACK, width=0)

    # mouth используем параболу
    point_list = []
    mouth_step = int(radius * 1.2 // detalization)
    for x_mouth in range(int(-radius * 0.6), int(radius * 0.6) + mouth_step, mouth_step):
        y_mouth = x_mouth ** 2 / (radius * 1.2) - radius / 2
        point_list.append(sd.get_point((x_mouth + x), (y_mouth + y)))
        print(sd.get_point(x_mouth, y_mouth))
    sd.lines(point_list, color=sd.COLOR_BLACK, closed=False, width=int(radius * 0.05))


def full_gradient(color, detalization):
    channels = list(color)

    for i, channel in enumerate(channels):

        channels[i] += int(255 / detalization)
        if channels[i] < 0:
            channels[i] = 0
        if channels[i] > 255:
            channels[i] = 255

    return tuple(channels)


for _ in range(10):
    x_random = random.randint(50, 1150)
    y_random = random.randint(50, 550)
    smile(x_random, y_random, sd.random_color(), )
sd.pause()
