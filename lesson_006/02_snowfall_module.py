# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall as sf

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

sf.make_flakes(10)
while True:
    sf.draw_flakes(color=sd.background_color)
    sf.move_flake()
    sf.draw_flakes(color=sd.COLOR_WHITE)
    if sf.get_fallen_flakes():
        count = len(sf.get_fallen_flakes())
        sf.del_flakes(sf.get_fallen_flakes())
        sf.make_flakes(count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
