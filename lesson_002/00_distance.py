#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}


moscow_london = ((sites['Moscow'][0] - sites['London'][0])**2 + (sites['Moscow'][1] - sites['London'][1])**2)**0.5
moscow_paris = ((sites['Moscow'][0] - sites['Paris'][0])**2 + (sites['Moscow'][1] - sites['Paris'][1])**2)**0.5
paris_london = ((sites['Paris'][0] - sites['London'][0])**2 + (sites['Paris'][1] - sites['London'][1])**2)**0.5
distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris
distances['London'] = {}
distances['London']['Moscow'] = moscow_london
distances['London']['Paris'] = paris_london
distances['Paris'] = {}
distances['Paris']['London'] = paris_london
distances['Paris']['Moscow'] = moscow_paris


print(distances)




