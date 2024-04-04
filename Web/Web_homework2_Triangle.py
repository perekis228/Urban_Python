def IsTriangle(side1, side2, side3):
    sides = [side1, side2, side3]
    Max = max(sides)
    sides.remove(Max)
    Mid = max(sides)
    Min = min(sides)
    if Min == 0:
        print("Треугольника не существует")
    elif Max ** 2 == Mid ** 2 + Min ** 2:
        print("Треугольник прямой")
    elif Max == Mid == Min:
        print("Треугольник равносторонный")
    elif Mid == Min or Mid == Max or Max == Min:
        print("Треугольник равнобедренный")
    elif Max < Mid + Min:
        print("Треугольник разносторонний")
    else:
        print("Треугольника не существует")

a = int(input("Введите длину первой стороны: "))
b = int(input("Введите длину второй стороны: "))
c = int(input("Введите длину третьей стороны: "))
IsTriangle(a, b, c)
