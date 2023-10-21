class InvalidNameError(ValueError):
    pass


class InvalidAgeError(ValueError):
    pass


class InvalidIdError(ValueError):
    pass


class Person:

    def __init__(self, name: str, surname: str, patronymic: str, age: int):
        self.validate_name(name, surname, patronymic)
        self.validate_age(age)
        self._name = name
        self._surname = surname
        self._patronymic = patronymic
        self._age = age

    def validate_name(self, name: str, surname: str, patronymic: str):
        if not isinstance(name, str) or name == '':
            raise InvalidNameError('Invalid name: . Name should be a non-empty string.')
        if not isinstance(surname, str) or surname == '':
            raise InvalidNameError('Invalid surname: . Surname should be a non-empty string.')
        if not isinstance(patronymic, str) or patronymic == '':
            raise InvalidNameError('Invalid patronymic: . Patronymic should be a non-empty string.')

    def validate_age(self, age: int):
        if not isinstance(age, int) or age < 0:
            raise InvalidAgeError(f'Invalid age: {age}. Age should be a positive integer.')

    def __eq__(self, other):
        if isinstance(other, Person):
            return (self._name == other._name and self._surname == other._surname and
                    self._patronymic == other._patronymic and self._age == other._age)

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_patronymic(self):
        return self._patronymic

    def get_age(self):
        return self._age

    def birthday(self):
        self._age += 1


class Employee(Person):

    def __init__(self, name: str, surname: str, patronymic: str, age: int, id: int):
        super().__init__(name, surname, patronymic, age)
        self.validate_id(id)
        self._id = id

    def validate_id(self, id):
        if not isinstance(id, int) or id < 100000 or id > 999999:
            raise InvalidIdError(
                f'Invalid id: {id}. Id should be a 6-digit positive integer between 100000 and 999999.')

    def __eq__(self, other):
        if isinstance(other, Employee):
            return (self._name == other._name and self._surname == other._surname and
                    self._patronymic == other._patronymic and self._age == other._age)

    def get_id(self):
        return self._id

    def get_level(self):
        return sum(map(int, (list(str(self._id))))) % 7
