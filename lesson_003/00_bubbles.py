# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (21, 23, 60)
detalization = 5
bubble_width = 2


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def bubble(point, step, radius, color=(255, 255, 0)):
    x, y = point
    center = sd.get_point(x, y)

    for _ in range(detalization):
        radius -= step
        sd.circle(center, radius=radius, color=color, width=bubble_width)
        color = full_gradient(color)


def full_gradient(color):
    channels = list(color)

    for i, channel in enumerate(channels):

        channels[i] -= int(channel / detalization)
        if channels[i] < 0:
            channels[i] = 0

    return tuple(channels)


# Нарисовать 10 пузырьков в ряд

# for x in range(100, 1001, 100):
#     bubble((x, 200), 5, 70)

# Нарисовать три ряда по 10 пузырьков


# for y in range(200, 501, 100):
#     for x in range(100, 1001, 100):
#         bubble((x, y), 5, 70)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    x = random.randint(0, 1200)
    y = random.randint(0, 600)
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    radius = random.randint(30, 50)
    bubble((x, y), bubble_width, radius, rand_color)
sd.pause()
