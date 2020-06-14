from random import randint

number = ''


def pick_number():
    global number
    number = ''
    number += str(randint(1, 9))
    while len(number) < 4:
        new_element = str(randint(0, 9))
        if new_element in number:
            continue
        else:
            number += new_element
    return number


def test_number(user_number):
    cows_counter = 0
    bulls_counter = 0
    for i, user_digit in enumerate(user_number):
        if user_digit in number:
            cows_counter += 1
            if number[i] == user_number[i]:
                # print(number[i], '==', user_number[i])
                bulls_counter += 1
                cows_counter -= 1

    return {'bulls': bulls_counter, 'cows': cows_counter}


if __name__ == '__main__':
    pick_number()
    for _ in range(100):
        print("\033[H\033[J")
        my_try = input('>>> - - -  ')
        if my_try == '0000':
            print(number)
        print(test_number(my_try))
