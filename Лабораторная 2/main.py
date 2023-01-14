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
    """
    Класс, описывающий книгу
    """
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация экземпляра класса "Книга"

        :param id_: индентификатор книги
        :param name: название книги
        :param pages: количество страниц в книге
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        :return: строка формата - Книга "название книги"
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        :return: строка, по которой можно инициализировать экземпляр класса
        """
        return f"Book(id_={self.id_}, name={self.name!r}, pages={self.pages})"


class Library:
    """
    Класс для работы со списком книг
    """
    def __init__(self, books: list = None):
        """
        Инициализация экземпляра класса "Библиотека"

        :param books: спикок экземпляров класса Book
        """
        if books is None:
            self.books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку

        :return: идентификатор последней книги увеличенный на 1, если книг нет - 1
        """
        if not self.books:
            return 1
        last_book = self.books[-1]
        return last_book.id_ + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса

        :param book_id: id, по которому ищется книга
        :return: индекс книги в списке
        """
        index = 0.5
        for i, book in enumerate(self.books):
            if book.id_ == book_id:
                index = i
        if index == 0.5:
            raise ValueError("Книги с запрашиваемым id не существует")
        return index


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
