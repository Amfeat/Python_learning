# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
try:
    leeloo = int(input_data[4])
except ValueError:
    print('невозможно преобразовать к числу')
except IndexError:
    print('выход за границы списка')
except Exception:
    print('Unknown Error')
else:
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение




