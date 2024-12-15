# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Car:
    def __init__(self, color: str, year: int, gearbox: str):
        """

        Создание и подготовка к работе объекта "Автомобиль"

        :param color: цвет автомобиля
        :param year: год выпуска автомобиля
        :param gearbox: тип коробки передач автомобиля

        Примеры:
        >>> car = Car('белый', 2009, 'ручная')  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError('Цвет авто должен быть типа str')
        if not isinstance(year, int):
            raise TypeError('Год выпуска должен быть типа int')
        if not isinstance(gearbox, str):
            raise TypeError('Тип коробки передач должен быть типа str')
        if year <= 1899 or year >= 2024:
            raise ValueError('Год выпуска должен быть реальным')
        self.color = color
        self.year = year
        self.gearbox = gearbox

    def open_or_close_car(self, position: int) -> None:
        """
        Функция, которая открывает или закрывает автомобиль (position = 0 - авто закрыто,
        position = 1 - авто открыто)

        :return ValueError: Если авто уже открыто/закрыто

        Пример:
        >>> car = Car('белый', 2009, 'ручная')
        >>> car.open_or_close_car(1)
        """
        ...

    def is_car_drivable(self) -> bool:
        """
        Функция, которая проверяет, на ходу ли автомобиль

        :return: На ходу ли автомобиль

        Примеры:
        >>> car = Car('белый', 2009, 'ручная')
        >>> car.is_car_drivable()
        """
        ...


class Ball:
    def __init__(self, radius: Union[float, int], color: str):
        """

        Создание и подготовка к работе объекта "Шар"

        :param radius: радиус шара
        :param color: цвет шара

        Примеры:
        >>> ball = Ball(10, "черный")  # инициализация экземпляра класса
        """
        if not isinstance(radius, (float, int)):
            raise TypeError('Радиус шара должен быть типа int или float')
        if not isinstance(color, str):
            raise TypeError('Цвет должен быть типа str')
        if radius < 0:
            raise ValueError('Радиус шара должен быть больше нуля')
        self.radius = radius
        self.color = color

    def volume(self) -> float:
        """
        Функция для вычисления объема шара

        :return: Объем шара

        Примеры:
        >>> ball = Ball(10, 'черный')
        >>> print(ball.volume())
        4186.6
        """
        v = 4/3 * 3.14 * self.radius**3
        return v

    def area(self) -> float:
        """
        Функция для вычисления площади поверхности шара

        :return: Площадь поверхности шара

        Примеры:
        >>> ball = Ball(10, 'черный')
        >>> print(ball.area())
        1256.0
        """
        c = 4 * 3.14 * self.radius**2
        return c


class Human:
    def __init__(self, sex: str, age: int, name: str):
        """

        Создание и подготовка к работе объекта "Человек"

        :param sex: пол человека
        :param age: возраст человека
        :param name: имя человека

        Примеры:
        >>> human = Human('мужчина', 20, 'Клим')  # инициализация экземпляра класса
        """
        if not isinstance(sex, str):
            raise TypeError('Пол должен быть задан типом str')
        if not isinstance(age, int):
            raise TypeError('Возраст должен быть задан типом int')
        if not isinstance(name, str):
            raise TypeError('Имя должно быть задано типом str')
        if age < 0:
            raise ValueError('Возраст не может быть меньше нуля')
        self.sex = sex
        self.age = age
        self.name = name

    def birthday(self):
        """
        Функция увеличения возраста человека на год

        :return: Текущий возраст

        Пример:
        >>> human = Human('мужчина', 20, 'Клим')
        >>> human.birthday()
        """
        ...

    def name_changing(self, new_name: str):
        """
        Функция замены имени

        :param new_name: Новое имя
        :raise ValueError: Если имя не типа str, то вызываем ошибку

        Пример:
        >>> human = Human('мужчина', 20, 'Клим')
        >>> human.name_changing('Евгений')
        """
        ...


if __name__ == "__main__":
    doctest.testmode()
