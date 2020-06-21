# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint, choice


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    MIN_MONEY = 100
    MIN_FOOD = 50
    MAX_FOOD = 200

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0

    def __str__(self):
        self.dirt += 5
        return 'В доме: денег {},еды {}, грязи {}'.format(self.money, self.food, self.dirt)


class Person:
    min_fullness = 20
    min_happiness = 30
    total_food = 0

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def __str__(self):
        return '{}: сытость {}, счастье {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.food >= 30:
            self.fullness += 30
            self.house.food -= 30
            self.total_food += 30
        elif self.house.food > 0:
            self.fullness += self.house.food
            self.total_food += self.house.food
            self.house.food = 0
        cprint('{} поел!'.format(self.name))

    def alive(self):
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness <= 0:
            cprint('{} умер от голода.....RIP'.format(self.name), color='red', on_color='on_cyan')
            return False
        elif self.happiness <= 10:
            cprint('{} умер от депрессии.....RIP'.format(self.name), color='red', on_color='on_cyan')
            return False
        else:
            return True


class Husband(Person):
    total_money = 0
    total_gaming = 0

    #
    # def __init__(self):
    #     pass
    #
    def __str__(self):
        return super().__str__()

    def act(self):
        if not self.alive():
            return
        dice = randint(1, 6)
        if self.fullness <= self.min_fullness and self.house.food > 0:
            self.eat()
            return
        elif self.happiness <= self.min_happiness:
            self.gaming()
        elif self.house.money <= self.house.MIN_MONEY:
            self.work()
        elif dice > 3:
            self.work()
        else:
            self.gaming()
        self.fullness -= 10

        pass

    #
    # def eat(self):
    #     pass

    def work(self):
        self.total_money += 150
        self.house.money += 150
        cprint('{} весь день работал'.format(self.name), color='green')

    def gaming(self):
        self.total_gaming += 1
        self.happiness += 20
        cprint('{} весь день играл в WoT'.format(self.name), color='yellow')

        pass

    def stat(self):
        cprint('{} съел {} еды, заработал {} днег, играл в танки {} дней'.format(
            self.name, self.total_food, self.total_money, self.total_gaming), on_color='on_cyan')


class Wife(Person):
    total_fur_coat = 0

    #
    # def __init__(self):
    #     pass
    #
    def __str__(self):
        return super().__str__()

    def act(self):
        if not self.alive():
            return
        if self.fullness <= self.min_fullness and self.house.food > 0:
            self.eat()
            return
        elif self.house.food <= self.house.MIN_FOOD:
            self.shopping()
        elif self.house.dirt >= 80:
            self.clean_house()
        elif self.house.money >= 500:
            self.buy_fur_coat()
        else:
            self.clean_house()
        self.fullness -= 10

    #
    # def eat(self):
    #     pass

    def shopping(self):
        available_food = min(self.house.money, self.house.MAX_FOOD)
        self.house.money -= available_food
        self.house.food += available_food
        cprint('{} купила {} еды'.format(self.name, available_food), color='yellow')

    def buy_fur_coat(self):
        self.house.money -= 350
        self.happiness += 60
        self.total_fur_coat += 1
        cprint('{} купила шубу!'.format(self.name), color='magenta')

    def clean_house(self):
        self.house.dirt = 0
        cprint('{} прибиалась в доме весь день'.format(self.name), color='green')

    def stat(self):
        cprint('{} села {} еды и купила {} шуб'.format(self.name, self.total_food, self.total_fur_coat),
               on_color='on_cyan')


class Child(Person):

    # def __init__(self):
    #     pass

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness < 0:
            cprint('{} умер....'.format(self.name), color='red')
            return
        if self.fullness <= 20 and self.house.food > 0:
            self.eat()
        else:
            self.sleep()
        pass

    def eat(self):
        self.fullness += min(self.house.food, 10)
        self.house.food -= min(self.house.food, 10)
        cprint('{} поел!'.format(self.name), color='yellow')

    def sleep(self):
        cprint('{} поспал!'.format(self.name), color='blue')
        self.fullness -= 10


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(home, color='cyan')

cprint('================== итоги ==================', color='red')
masha.stat()
serge.stat()


#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)
class Child(Person):

    # def __init__(self):
    #     pass

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness < 0:
            cprint('{} умер....'.format(self.name), color='red')
            return
        if self.fullness <= 20 and self.house.food > 0:
            self.eat()
        else:
            self.sleep()
        pass

    def eat(self):
        self.fullness += min(self.house.food, 10)
        self.house.food -= min(self.house.food, 10)
        cprint('{} поел!'.format(self.name), color='yellow')

    def sleep(self):
        cprint('{} поспал!'.format(self.name), color='blue')


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
