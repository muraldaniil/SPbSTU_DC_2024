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


class Library:
    def __init__(self, books: list[Book] = None):
        """
        Инициализация объекта "Библиотека".

        :param books: Список объектов класса Book. Если не передан, используется пустой список.
        """
        if books is None:
            books = []
        if not isinstance(books, list):
            raise TypeError("Аргумент books должен быть списком")
        if not all(isinstance(book, Book) for book in books):
            raise TypeError("Все элементы в списке books должны быть экземплярами класса Book")
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает следующий идентификатор для добавления новой книги.

        Если книг нет, возвращает 1.
        Если книги есть, возвращает идентификатор последней книги + 1.
        """
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по ее идентификатору.

        :param book_id: Идентификатор книги, для которой ищется индекс.
        :raise ValueError: Если книги с данным id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError(f"Нет книги с id {book_id}")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
