# 📌Дорабатываем класс прямоугольник из прошлого семинара.
# 📌Добавьте возможность сложения и вычитания.
# 📌При этом должен создаваться новый экземпляр прямоугольника.
# 📌При вычитании не допускайте отрицательных значений.


from functools import total_ordering


class MyException(Exception):
    def __init__(self,value,  side: str):
        self.side = side
        self.value = value

    def __str__(self):
        return f'{self.side} должна быть положительной, а не {self.value}'


class NegativeValueError(MyException):

    def __init__(self, value, side):
        super(NegativeValueError, self).__init__(value, side)


@total_ordering
class Rectangle:

    def __init__(self, width: int, height: int = None):
        if width < 0:
            raise NegativeValueError(width, 'Ширина')
        self._width = width
        if height and height < 0:
            raise NegativeValueError(height, "Высота")
        self._height = height or width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise NegativeValueError(value, "Ширина")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise NegativeValueError(value, "Высота")
        self._height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.width > other.width and self.height > other.height:
                return Rectangle(self.width - other.width, self.height - other.height)
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами: {self.width} и {self.height}'

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


# rect1 = Rectangle(5, 10)
# rect2 = Rectangle(3, 7)
#
# print(f"Периметр rect1: {rect1.perimeter()}")
# print(f"Площадь rect2: {rect2.area()}")
# print(f"rect1 < rect2: {rect1 < rect2}")
# print(f"rect1 == rect2: {rect1 == rect2}")
# print(f"rect1 <= rect2: {rect1 <= rect2}")
#
# rect3 = rect1 + rect2
# print(f"Периметр rect3: {rect3.perimeter()}")
# rect4 = rect1 - rect2
# print(f"Ширина rect4: {rect4.width}")
#
# rect1.height = -2

# r = Rectangle(4, 4)
# r.height = -3
