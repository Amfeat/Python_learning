# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

WIND = 0


class Snowflake:
    def __init__(self):
        self.speed = sd.random_number(5, 15)
        self.length = sd.random_number(10, 50)
        self.x = sd.random_number(10, 600)
        self.y = sd.random_number(300, 600)

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color)
        pass

    def move(self):
        self.x += WIND
        self.y -= self.speed
        pass

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.COLOR_WHITE)
        pass

    def can_fall(self):
        if self.y <= 10:
            return False
        else:
            return True

    pass


# flake = Snowflake()

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


def get_flakes(count):
    return [Snowflake() for _ in range(count)]


def get_fallen_flakes():
    i = 0
    for flake in flakes:
        if not flake.can_fall():
            i += 1
            del flake
    return i


def append_flakes(count):
    global flakes
    for _ in range(count):
        flakes.append(Snowflake())


def pop_fallen_flakes():
    global flakes
    for i, flake in enumerate(flakes):
        if not flake.can_fall():
            flakes.pop(i)


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=10)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    pop_fallen_flakes()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
