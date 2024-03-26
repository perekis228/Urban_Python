#1
a = 100
x = 26
print(f'{(a/x):.3f}')

#2
list_ = [['*', '*'], [], []]
list_.clear()
list_.append(['*','*','*'])
list_.append(['*','*','*'])
list_.append(['*','*','*'])
print(list_, "\n")

#3
def check_win(count, stop, list_):
    # транспонированное поле
    trans_list_ = [[list_[j][i] for j in range(len(list_))] for i in range(len(list_[0]))]

    # Перебор всех вариантов победы
    if count == 9:
        stop = True
        print("Ничья")
    elif set(list_[0]) == {'x'}:
        stop = True;
        print('х Победил')
    elif set(list_[0]) == {'o'}:
        stop = True;
        print('o Победил')
    elif set(list_[1]) == {'x'}:
        stop = True;
        print('х Победил')
    elif set(list_[0]) == {'o'}:
        stop = True;
        print('o Победил')
    elif set(list_[0]) == {'x'}:
        stop = True;
        print('х Победил')
    elif set(list_[0]) == {'o'}:
        stop = True;
        print('o Победил')
    elif set(trans_list_[0]) == {'x'}:
        stop = True;
        print('х Победил')
    elif set(trans_list_[0]) == {'o'}:
        stop = True;
        print('o Победил')
    elif set(trans_list_[1]) == {'x'}:
        stop = True;
        print('х Победил')
    elif set(trans_list_[1]) == {'o'}:
        stop = True;
        print('o Победил')
    elif set(trans_list_[0]) == {'x'}:
        stop = True;
        print('х Победил')
    elif set(trans_list_[2]) == {'o'}:
        stop = True;
        print('o Победил')
    elif list_[0][0] == list_[1][1] == list_[2][2] == 'x':
        stop = True;
        print('х Победил')
    elif list_[0][0] == list_[1][1] == list_[2][2] == 'o':
        stop = True;
        print('o Победил')
    elif list_[0][2] == list_[1][1] == list_[2][0] == 'x':
        stop = True;
        print('х Победил')
    elif list_[0][2] == list_[1][1] == list_[2][0] == 'o':
        stop = True;
        print('o Победил')
    return count, stop

print("Ход х")          # Первый ходит х
print(*list_, sep='\n') # Показываем исходное поле
stop = False
count = 0               # Количество ходов

while not stop:
    x = int(input("Введите координату х "))     # Запрашиваем координаты, куда ставить х или о
    y = int(input("Введите координату у "))

    if count % 2 == 0:           # Начинают ходить х, значит его ходы 0,2...
        list_[3 - y][x - 1] = 'x'
    else:                        # У о ходы 1,3...
        list_[3 - y][x - 1] = 'o'
    print(*list_, sep='\n')      # Показываем обновлённое поле
    count += 1

    count, stop = check_win(count, stop, list_)

    # Показываем, кто в данный момент ходит
    if count % 2 == 0 and count < 9 and stop == False:
        print("Ход x")
    if count % 2 == 1 and stop == False:
        print("Ход o")
