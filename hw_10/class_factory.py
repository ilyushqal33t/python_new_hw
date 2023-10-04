# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Animals:

    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.spec = None

    def get_spec(self):
        return self.spec

    def voice(self):
        return f'____'

    def info(self):
        return f'____'


class PetFactory:

    @staticmethod
    def create_pet(pet_class: str, color, name, age, spec):
        if pet_class.lower() == 'dog':
            return Dog(color, name, age, spec)
        if pet_class.lower() == 'cat':
            return Cat(color, name, age, spec)
        if pet_class.lower() == 'fish':
            return Fish(color, name, age, spec)
        else:
            return 'TypeError'


# """второй вариант решения"""
#
#
# class PetFactory:
#
#     def __init__(self, pet_class):
#         self.pet_class = pet_class
#
#     def create_pet(self, color, name, age, spec):
#         if self.pet_class.lower() == 'dog':
#             return Dog(color, name, age, spec)
#         if self.pet_class.lower() == 'cat':
#             return Cat(color, name, age, spec)
#         if self.pet_class.lower() == 'fish':
#             return Fish(color, name, age, spec)
#         else:
#             return 'TypeError'
#
#
# factory_1 = PetFactory('dog')
# dog_1 = factory_1.create_pet('purple', 'name_1', 5, 'home')
# print(dog_1.info())


class Dog(Animals):

    def __init__(self, color, name, age, spec):
        super().__init__(name, age)
        self.color = color
        self.spec = spec

    def voice(self):
        return f'wof-wof'

    def info(self):
        return f'{self.__class__.__name__}, {self.name}, age: {self._age}, {self.color}, spec: {self.get_spec()}'


class Cat(Animals):

    def __init__(self, color, name, age, spec):
        super().__init__(name, age)
        self.color = color
        self.spec = spec

    def voice(self):
        return f'meow-meow'

    def info(self):
        return f'{self.__class__.__name__}, {self.name}, age: {self._age}, {self.color}, spec: {self.get_spec()}'


class Fish(Animals):

    def __init__(self, color, name, age, spec):
        super().__init__(name, age)
        self.color = color
        self.spec = spec

    def voice(self):
        return f'silence'

    def info(self):
        return f'{self.__class__.__name__}, {self.name}, age: {self._age}, {self.color}, spec: {self.get_spec()}'


pet_1 = PetFactory.create_pet('Dog', 'purple', 'name_1', 5, 'home')
pet_2 = PetFactory.create_pet('cat', 'black', 'name_2', 5, 'sleep')
pet_3 = PetFactory.create_pet('FiSh', 'red', 'name_3', 5, 'swim')
print(pet_1.info(), pet_1.voice())
print(pet_2.info(), pet_2.voice())
print(pet_3.info(), pet_3.voice())