#1
a = 100
x = 26
print(f'{(a/x):.3f}')

#2
list_ = [['*', '*'], [], []]
list_.clear()
list_.extend([['*', '*', '*']] * 3)
print(list_, "\n")

#3

list_ = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

#Рисование поля
def draw_area():
    for i in list_:
        print(*i)
        
#Проверка хода или победы
def step_or_win(count, stop):
    if count == 9 and not stop:
        stop = True;
        print("Ничья")
    elif stop:
        if count % 2 == 1:
            print("Победа x")
        else:
            print("Победа o")
    else:
        if count % 2 == 0:
            print("Ход x\n")
        else:
            print("Ход o\n")

#Проверка победы
def check_win(stop, list_):
    # транспонированное поле
    trans_list_ = [[list_[j][i] for j in range(len(list_))] for i in range(len(list_[0]))]

    # Перебор всех вариантов победы
    if len(set(list_[0])) == 1 and set(list_[0]) != {'*'}:
        stop = True;
    elif len(set(list_[1])) == 1 and set(list_[1]) != {'*'}:
        stop = True;
    elif len(set(list_[2])) == 1 and set(list_[2]) != {'*'}:
        stop = True;
    elif len(set(trans_list_[0])) == 1 and set(trans_list_[0]) != {'*'}:
        stop = True;
    elif len(set(trans_list_[1])) == 1 and set(trans_list_[1]) != {'*'}:
        stop = True;
    elif len(set(trans_list_[2])) == 1 and set(trans_list_[2]) != {'*'}:
        stop = True;
    elif list_[0][0] == list_[1][1] == list_[2][2] != '*':
        stop = True;
    elif list_[0][2] == list_[1][1] == list_[2][0] != '*':
        stop = True;
    return stop

print("Ход х")          # Первый ходит х
draw_area()
stop = False
count = 0               # Количество ходов

while not stop:
    x = int(input("Введите координату х "))     # Запрашиваем координаты, куда ставить х или о
    y = int(input("Введите координату у "))

    #Проверяем, занята ли ячейка, если занята, то чел ходит заново
    if list_[3 - y][x - 1] == 'x' or list_[3 - y][x - 1] == 'o':
        print("Ячейка занята!\n")
        draw_area()
        step_or_win(count, stop)
        continue
    #Если вышел за поле, ходит заново
    elif x < 1 or x > 3 or y < 1 or y > 3:
        print("Вы вышли за пределы поля!\n")
        draw_area()
        step_or_win(count, stop)
        continue
    elif count % 2 == 0:           # Начинают ходить х, значит его ходы 0,2...
        list_[3 - y][x - 1] = 'x'
    else:                        # У о ходы 1,3...
        list_[3 - y][x - 1] = 'o'
    draw_area()                  # Показываем обновлённое поле
    count += 1

    stop = check_win(stop, list_)

    # Показываем, кто в данный момент ходит/побеждает
    step_or_win(count, stop)
