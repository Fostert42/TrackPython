# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Window:
    def __init__(self, length: float, width: float):
        """
        Создание и подготовка к работе объекта "Окно"

        :param length: Высота окна
        :param width: Ширина окна

        Примеры:
        >>> window = Window(1800, 1000)
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Высота окна должна быть числом")
        if length <= 0:
            raise ValueError("Высота окна должна быть положительной")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина окна должна быть числом")
        if width <= 0:
            raise ValueError("Ширина окна должна быть положительной")
        self.width = width

    def open_window(self) -> None:
        """
        Открыть окно.

        :return: None

        Примеры:
        >>> window = Window(1800, 1000)
        >>> window.open_window()
        """
        ...

    def get_area(self) -> float:
        """
        Получить площадь окна.

        :return: Площадь окна

        Примеры:
        >>> window = Window(1000, 2000)
        >>> window.get_area()
        2000000
        """
        ...


class Car:
    def __init__(self, brand: str, speed: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param speed: Текущая скорость автомобиля

        Примеры:
        >>> car = Car("BMW", 0)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not brand:
            raise ValueError("Бренд не может быть пустым")
        self.brand = brand

        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость должна быть числом")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self.speed = speed

    def stage1(self, add_speed: float) -> None:
        """
        Увеличить скорость автомобиля.

        :param add_speed: Значение, на которое увеличивается скорость.
                          Должно быть положительным числом.

        :return: None

        Примеры:
        >>> car = Car("Audi", 50)
        >>> car.stage1(20)
        """
        if not isinstance(add_speed, (int, float)):
            raise TypeError
        if add_speed < 0:
            raise ValueError
        ...

    def get_brand(self) -> str:
        """
        Получить марку автомобиля.

        :return: Марка автомобиля

        Примеры:
        >>> car = Car("Toyota", 0)
        >>> car.get_brand()
        'Toyota'
        """
        ...


class StackPaper:
    def __init__(self, format: str, count: float):
        """
        Создание и подготовка к работе объекта "Стопка бумаги"

        :param format: Формат бумаги
        :param count: Количество листов

        Примеры:
        >>> paper = StackPaper("A4", 100)
        """
        if not isinstance(format, str):
            raise TypeError("Формат должен быть строкой")
        if not format:
            raise ValueError("Формат не может быть пустым")
        self.format = format

        if not isinstance(count, (int, float)):
            raise TypeError("Количество листов должно быть числом")
        if count < 0:
            raise ValueError("Количество листов не может быть отрицательным")
        self.count = count

    def add_page(self, add_pagee: float) -> None:
        """
        Добавить листы в стопку бумаги.

        :param add_pagee: Количество добавляемых листов.
                          Должно быть положительным числом.

        :return: None

        Примеры:
        >>> paper = StackPaper("A4", 50)
        >>> paper.add_page(10)
        """
        if not isinstance(add_pagee, (int, float)):
            raise TypeError
        if add_pagee < 0:
            raise ValueError
        ...

    def get_page(self) -> float:
        """
        Получить количество листов в стопке.

        :return: Количество листов

        Примеры:
        >>> paper = StackPaper("A4", 80)
        >>> paper.get_page()
        80
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
