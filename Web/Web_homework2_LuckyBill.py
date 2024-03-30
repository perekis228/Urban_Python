def LuckyBill(first, second, third, fourth, fifth, sixth):
    if first + second + third == fourth + fifth + sixth:
        print("Счастливый билет!")
    else:
        print("Увы :(")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = int(input("Введите четвёртое число: "))
e = int(input("Введите пятое число: "))
f = int(input("Введите шестое число: "))
LuckyBill(a, b, c, d, e, f)