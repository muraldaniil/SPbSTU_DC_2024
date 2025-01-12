import doctest

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация объекта "Книга".

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге

        :raise TypeError: Если id_ или pages не являются целыми числами
        :raise ValueError: Если id_ или pages имеют некорректные значения
        """
        if not isinstance(id_, int):
            raise TypeError("Айди должно быть типа int")
        if id_ <= 0:
            raise ValueError("Айди должно быть положительным числом")
        self.id = id_

        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строку с названием книги.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку с полным представлением объекта.
        """
        return f"Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})"

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
