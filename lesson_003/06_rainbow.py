# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (1200, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

def rainbow_line():
    x_start = 50
    y_start = 50
    x_end = 350
    y_end = 450



    for color in rainbow_colors:
        start_point = sd.get_point(x_start, y_start)
        end_point = sd.get_point(x_end, y_end)
        sd.line(start_point, end_point, color, 4)
        x_start = x_start + 5
        x_end = x_end + 5
# rainbow_line()


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

def rainbow_circle():
    center = sd.get_point(600, -100)
    radius = 600
    step = 5

    for color in rainbow_colors:
        radius -= step

        sd.circle(center, radius=radius, color=color, width=1)
        color = full_gradient(color)
        sd.circle(center, radius=radius+1, color=color, width=1)
        color = full_gradient(color)
        sd.circle(center, radius=radius+2, color=color, width=1)
        color = full_gradient(color)
        sd.circle(center, radius=radius+3, color=color, width=1)




def full_gradient(color):
    channels = list(color)

    for i, channel in enumerate(channels):

        channels[i] -= int(channel / 3)
        if channels[i] < 0:
            channels[i] = 0

    return tuple(channels)

rainbow_circle()

sd.pause()
