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


def compare():
    count = 0
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


num = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку\nВведите ваше число\n')
compare()



