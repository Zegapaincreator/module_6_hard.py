from math import pi

class Figure:
    side_count = 0
    __color = (0, 0, 0)
    __sides = []

    def __init__(self, *args, **kwargs):
        if isinstance(args[0], tuple) and len(args[0]) == 3:
            self.set_color(*args[0])
        else:
            raise ValueError("No color given")
        sides = args[1:]
        if len(sides) == 0:
            raise ValueError("No sides given")
        else:
            self.set_sides(*sides)

        if "field" in kwargs.keys():
            self.field = kwargs["field"]
        else:
            self.field = False

    def __is_valid_color(self, r, g, b):
        result = True
        result = result and isinstance(r, int) and (r >= 0) and (r < 256)
        result = result and isinstance(g, int) and (g >= 0) and (g < 256)
        result = result and isinstance(b, int) and (b >= 0) and (b < 256)
        return result

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            Exception(f'Не задан цвет фигуры!')

    def get_color(self):
        return self._Figure__color

    def __is_valid_side(self, sides: list):
        if len(sides) != self.side_count:
            return False
        for side in sides:
            if isinstance(side, int) and (side <= 0):
                return False
        return True

    def set_sides(self, *args):
        new_sides = args
        if self.side_count == 0:
            self.side_count = len(new_sides)
        if self.side_count != len(new_sides):
            new_sides = [1 for i in range(self.side_count)]
        if self.__is_valid_side(new_sides):
            self.__sides = [x for x in new_sides]

    def get_sides(self):
        return self._Figure__sides

    def __len__(self):
        return sum(self.get_sides())


class Circle(Figure):
    side_count = 1
    __radius = 0
    __sides = [0]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sides = self.get_sides()
        self.__radius = sides[0] / pi / 2

    def get_square(self):
        return pi * self._Circle__radius ** 2


class Triangle(Figure):
    side_count = 3
    __sides = [0, 0, 0]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2
        square = p
        for side in sides:
            square *= (p - side)
        return square ** 0.5


class Cube(Figure):
    side_count = 12
    __sides = [0 for i in range(12)]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_sides(self, *args):
        if len(args) == 1:
            self._Figure__sides = [args[0] for x in range(self.side_count)]
        elif len(args) == 12:
            self._Figure__sides = [x for x in range(self.side_count)]

    def get_volume(self):
        return self.get_sides()[0] ** 3


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)


    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77) # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15) # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15) # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    triangle1 = Triangle((0, 0, 0),3, 4, 5)
    print(triangle1.get_square())