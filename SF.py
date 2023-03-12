game_field = ([' ', 0, 1, 2], [0, '-', '-', '-'], [1, '-', '-', '-'], [2, '-', '-', '-'])

def greetings():
    print('---------------')
    print('  Приветствую  ')
    print('  вас в игре   ')
    print('крестики-нолики')
    print('---------------')
    print('\n')

def pr_gf():
    for i in range(len(game_field)):
        print(*game_field[i], sep=' | ')
        print('--------------')


def coords(x,y, sign):
    global game_field
    game_field[int(y) + 1][int(x) + 1] = sign

def sign():
    i = 0
    while True:
        yield 'x' if i % 2 == 0 else 'o'
        i += 1

def game_over(cur_s):
    if all(i == cur_s for i in game_field[1][1:]):
        print(f'Game over, победили {cur_s}')
        exit()
    elif all(i == cur_s for i in game_field[2][1:]):
        print(f'Game over, победили {cur_s}')
        exit()
    elif all(i == cur_s for i in game_field[3][1:]):
        print(f'Game over, победили {cur_s}')
        exit()
    elif game_field[1][1] == cur_s and game_field[2][2] == cur_s and game_field[3][3] == cur_s:
        print(f'Game over, победили {cur_s}')
        exit()
    elif game_field[3][1] == cur_s and game_field[2][2] == cur_s and game_field[1][3] == cur_s:
        print(f'Game over, победили {cur_s}')
        exit()
    elif game_field[1][1] == cur_s and game_field[2][1] == cur_s and game_field[3][1] == cur_s:
        print(f'Game over, победили {cur_s}')
        exit()
    elif game_field[1][2] == cur_s and game_field[2][2] == cur_s and game_field[3][2] == cur_s:
        print(f'Game over, победили {cur_s}')
        exit()
    elif game_field[1][3] == cur_s and game_field[2][3] == cur_s and game_field[3][3] == cur_s:
        print(f'Game over, победили {cur_s}')
        exit()
    elif all(i != '-' for i in game_field[1][1:]) and all(i != '-' for i in game_field[2][1:]) and all(i != '-' for i in game_field[3][1:]):
        print('Game over, победителя нет!')
        exit()

a = sign()
current_sign = next(a)
greetings()
pr_gf()

while  True:
    

    while (x := input(f'Ходит {current_sign} введите координату по горизонтали от 0 до 2: ')) not in ['0', '1', '2']:
        print('Неподходящая координата')
    while (y := input(f'Ходит {current_sign} введите координату по вертикали от 0 до 2: ')) not in ['0', '1', '2']:
        print('Неподходящая координата')
    if game_field[int(y) + 1][int(x) + 1] != '-':
        print('Данная координата уже занята, введите другое значение')
        continue

    coords(x, y, current_sign)
    pr_gf()
    
    game_over(current_sign)




    current_sign = next(a)
