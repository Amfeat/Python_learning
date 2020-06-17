# -*- coding: utf-8 -*-

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py
# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from termcolor import cprint
from random import randint, choice


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.alive = True

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            self.fullness -= 5
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= max(self.house.money//2, 50)
            self.house.food += max(self.house.money//2, 50)
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        # cprint('{} Вьехал в дом'.format(self.name), color='cyan')
        house.settle_citizens(self)

    def pick_cat(self, cat):
        cat.house = self.house
        self.house.settle_citizens(cat)

        cprint('{} принес кота {} в дом!'.format(self.name, cat.name), color='cyan')

    def buy_cat_food(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.money -= max(self.house.money//2, 50)
            self.house.cat_food += max(self.house.money//2, 50)
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_up(self):
        if self.fullness > 20:
            if self.house.dirt > 100:
                self.house.dirt -= 100
            else:
                self.house.dirt = 0
            self.fullness -= 20
            cprint('{} прибрался дома'.format(self.name), color='blue')
        else:
            cprint('{} обессилен и не может прибраться'.format(self.name), color='blue')
            self.eat()

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            self.alive = False
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif self.house.food < 30:
            self.shopping()
        elif self.house.cat_food < 50:
            self.buy_cat_food()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.clean_up()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0
        self.citizens = []

    def __str__(self):
        return 'В доме еды осталось {}, кошачьей еды осталось {} денег осталось {}, грязи {} '.format(
            self.food, self.cat_food, self.money, self.dirt)

    def settle_citizens(self, other):
        self.citizens.append(other)
        cprint('{} заселился в дом'.format(other.name), color='blue')


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.alive = True

    def __str__(self):
        return 'Кот {}, МЯУ {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('кот {} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.cat_food -= 10
        else:
            self.fullness -= 5
            cprint('Кот {}: МЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯУУУУУУУУУУУУУУУ!!!!!'.format(self.name), color='red')

    def work(self):
        cprint('Кот {} драл обои'.format(self.name), color='blue')
        self.house.dirt += 10
        self.fullness -= 10

    def sleep(self):
        cprint('Кот {} спал целый день'.format(self.name), color='green')
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            cprint('Кот {} умер...'.format(self.name), color='red')
            self.alive = False
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]
cat_names = ['Масик', 'Маврик', 'Митчел', 'Мурзик', 'Максимус', 'Маркиз', 'Марс', 'Макс',
             'Мотя', 'Маркус', 'Марти', 'Моцарт', 'Марио', 'Мандаринчик', 'Митька', 'Монгол',
             'Марик', 'Майкл', 'Митяй', 'Мэнесон', 'Мурчелло', 'Марик', 'Марсель', 'Мейсон',
             'Мусик', 'Маин', 'Мотька', 'Михаель', 'Матрос', 'Матвей', 'Мачо', 'Метеор', 'Миф',
             'Майки', 'Муренок', 'Микс', 'Морган']

my_sweet_home = House()

for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)

for _ in range(6):
    i = choice([0, 1, 2])
    name = choice(cat_names)
    citizens[i].pick_cat(Cat(name))

for day in range(1, 365):
    print('================ день {} =================='.format(day))
    for citizen in my_sweet_home.citizens:
        citizen.act()
    print('--- в конце дня ---')
    for citizen in my_sweet_home.citizens:
        print(citizen)
    print(my_sweet_home)

for citizen in my_sweet_home.citizens:
    print(citizen.alive)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
