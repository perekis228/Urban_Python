class NotIntExc(Exception):
    def __init__(self, arg):
        self.arg = arg

class LengthExc(Exception):
    def __init__(self, arg):
        self.arg = arg

def sumInt(int1, int2):
    if not int1.isdigit():
        raise NotIntExc(int1)
    if not int2.isdigit():
        raise NotIntExc(int2)

    int1 = int(int1)
    int2 = int(int2)

    if int1 >= 1000:
        raise LengthExc(int1)
    if int2 >= 1000:
        raise LengthExc(int2)

    return int1 + int2

try:
    int1 = input('Введите первое целое число не более 1000: ')
    int2 = input('Введите второе целое число не более 1000: ')
    print(sumInt(int1, int2))
except NotIntExc as exc:
    print(f'Ошибка. Вы ввели не целое число или строку, имеющую не только цифры: {exc.arg}')
except LengthExc as exc:
    print(f'Ошибка. Вы ввели число больше 1000: {exc.arg}')
else:
    print('Поздравляем! Вы нигде не совершили ошибки!')
finally:
    print('Удачного дня.')
