# 📌Создайте класс окружность. 📌Класс должен принимать радиус окружности при создании экземпляра.
# 📌У класса должно быть два метода, возвращающие длину окружности и её площадь.


from math import pi


class Circle:

    def __int__(self, rad):
        self.rad = rad

    def length_c(self):
        return 2 * self.rad * pi

    def area(self):
        return pi * self.rad**2
