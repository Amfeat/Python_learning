# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

def brick(x, y):
    # def rectangle(left_bottom, right_top, color=COLOR_YELLOW, width=0):
    left_bottom = sd.get_point(x, y)
    right_top = sd.get_point(x + 100, y + 50)
    sd.rectangle(left_bottom, right_top, width=5)


start_x = -25

for y in range(0, 600, 50):
    for x in range(start_x-25, 1200, 100):
        brick(x, y)
    start_x = -start_x

sd.pause()
