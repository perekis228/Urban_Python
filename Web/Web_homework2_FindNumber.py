import random

def Finder(num):
    found = False
    min = 1
    max = 100
    counter = 0
    while not found:
        mid = (max + min) // 2
        if num < mid:
            print("Число меньше", mid)
            max = mid
            counter += 1
        elif num > mid:
            print("Число больше", mid)
            min = mid
            counter += 1
        else:
            print("Вы отгадали число, загаданное число:", mid)
            print("Количество попыток:", counter)
            found = True

rand = random.randint(1, 100)
Finder(rand)