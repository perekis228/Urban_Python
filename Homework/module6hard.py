from math import sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *args):
        self.__sides = list(args)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if type(r) == type(g) == type(b) is int and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *args):
        if self.__is_valid_sides(args):
            self.__sides = list(args)

    def __is_valid_sides(self, *args):
        if len(args) != len(self.__sides):
            return False
        for side in args:
            if side < 0 or type(side) is not int:
                return False
        return True

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *args):
        super().__init__(color, args)
        if len(args) != Circle.sides_count:
            self.__sides = [1] * Circle.sides_count
        self.__radius = self.__sides[0] / 6.28

    def get_square(self):
        return 3.14 * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, args):
        super().__init__(color, args)
        if len(args) != Triangle.sides_count:
            self.__sides = [1] * Triangle.sides_count
        a = self.__sides[0]
        b = self.__sides[1]
        c = self.__sides[2]
        p = (a+b+c)/2
        self.__height = 2 * sqrt(p*(p-a)*(p-b)*(p-c)) / c

    def get_square(self):
        return self.__sides[2] * self.__height / 2

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, args):
        super().__init__(color, args)
        if len(args) > 1 and len(args) != Cube.sides_count:
            self.__sides = [1] * Cube.sides_count
        elif len(args) == 1:
            self.__sides = [self.__sides[0]] * 12

    def get_volume(self):
        return self.__sides[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# cube1.set_color(300, 70, 15) # Не изменится
# print(circle1.get_color())
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# circle1.set_sides(15) # Изменится
# print(cube1.get_sides())
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())