import math

class Figure:
    __sides_count = 0
    __color = (0, 0, 0)
    def __init__(self, color, *sides):
        self.color = list(color)
        self.filled = False
        if len(sides) == 0 or not self._is_valid_sides(*sides):
            self.sides = [1 for i in range(self.sides_count)]
        else:
            self.sides = list(sides)

    def get_color(self):
        return self.color

    def _is_valid_color(self, r, g, b):
        return all([isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b)])

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.color = [r, g, b]

    def _is_valid_sides(self, *new_sides):
        return (
            len(new_sides) == self.sides_count
            and all(isinstance(side, int) and side > 0 for side in new_sides)
        )

    def get_sides(self):
        return self.sides

    def __len__(self):
        return sum(self.sides)

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self.sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.radius = self.sides[0] / (2 * math.pi)

    def get_radius(self):
        return self.radius

    def get_area(self):
        return math.pi * self.radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)

    def get_area(self):
        a, b, c = self.sides
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(sides) != 12:
            self.sides = [sides[0]] * 12

    def get_volume(self):
        return self.sides[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
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
