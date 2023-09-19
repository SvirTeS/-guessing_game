import random


def is_valid(gnum):
    return gnum.isdigit() and 1 <= int(gnum) <= 100


def gamer_num():
    while True:
        gnum = input()
        if is_valid(gnum):
            return int(gnum)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


def compare(start_num, end_num):
    num = random.randint(start_num, end_num)
    count = 1
    while True:
        gnum = gamer_num()
        if gnum < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        elif gnum > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        else:
            print(f'Вы угадали c {count} попытки, поздравляем!')
            break


def start_game():
    print('Добро пожаловать в числовую угадайку\nВведите ваше число\n')
    while True:
        print('Укажите, в каком диапазоне Вы готовы угадывать числа\n(В пределах от 1 до 100):\n')
        x, y = gamer_num(), gamer_num()
        if x > y:
            x, y = y, x
        print('Введите число от', x, 'до', y, '\n')
        compare(x, y)
        if restart_game():
            continue
        else:
            break


def restart_game():
    ans = input('Продолжить ("да" или "нет")?\n')
    while True:
        if ans not in ('да', 'нет'):
            ans = input('Еще раз ("да"или "нет")?\n')
        elif ans in ('нет'):
            print('До новых встреч!!!')
            return False
        else:
            return True
