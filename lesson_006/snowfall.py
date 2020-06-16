# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

WIND_SPEED = 0
STEP = -10
flakes_list = []


def make_flakes(count):
    global flakes_list
    x_points = [sd.random_number(1, 1200) for _ in range(count)]
    y_points = [sd.random_number(100, 600) for _ in range(count)]
    lengths = [sd.random_number(10, 50) for _ in range(count)]
    flakes_list.extend([[x_points[i], y_points[i], lengths[i]] for i in range(count)])


def draw_flakes(color):
    sd.start_drawing()
    for flake in flakes_list:
        point = sd.get_point(flake[0], flake[1])
        sd.snowflake(center=point, length=flake[2], color=color)
    sd.finish_drawing()


def move_flake():
    for flake in flakes_list:
        flake[0] += WIND_SPEED
        flake[1] += STEP


def get_fallen_flakes():
    fallen_list = []
    for i, flake in enumerate(flakes_list):
        if flake[0] < -60 or flake[0] > 1260:
            fallen_list.append(i)
        elif flake[1] < 10:
            fallen_list.append(i)
    return fallen_list


def del_flakes(del_list):
    for i in reversed(del_list):
        flakes_list.pop(i)

