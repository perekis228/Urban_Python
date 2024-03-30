def IsTriangle(side1, side2, side3):
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        print("Треугольник можно построить")
    else:
        print("Треугольник построить нельзя")

a = int(input("Введите длину первой стороны: "))
b = int(input("Введите длину второй стороны: "))
c = int(input("Введите длину третьей стороны: "))
IsTriangle(a, b, c)