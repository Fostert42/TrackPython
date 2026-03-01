class Book:
    """ Базовый класс книги """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    # --- name и author только для чтения ---
    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    # --- Можно унаследовать ---
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    # Базовый repr (будет переопределён в дочерних)
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Бумажная книга """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # вызывается setter

    # --- pages с проверками ---
    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("pages должно быть целым числом")
        if value <= 0:
            raise ValueError("pages должно быть больше 0")
        self._pages = value

    # --- Перегружаем repr ---
    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(name={self.name!r}, author={self.author!r}, pages={self.pages})")


class AudioBook(Book):
    """ Аудиокнига """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # вызывается setter

    # --- duration с проверками ---
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("duration должно быть числом")
        if value <= 0:
            raise ValueError("duration должно быть больше 0")
        self._duration = float(value)

    # --- Перегружаем repr ---
    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(name={self.name!r}, author={self.author!r}, duration={self.duration})")