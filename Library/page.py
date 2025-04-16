class Book:
    def __init__(self, title, author, isbn, edition):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.edition = edition

    def fetch_books(self):
        print('-' * 50)
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Edition: {self.edition}")
        print('-' * 50)


class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} added successfully!")
    def display_books(self):
        for book in self.books:
            book.fetch_books()



if __name__ == "__main__":
    myLib = Library()

    # book1 = Book('Python Fundamentals', 'Brainzima', '9954-5456465454', '2026')
    # myLib.add_book(book1)

    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    edition = input("Edition: ")
    myLib.add_book(Book(title,author,isbn,edition))

    myLib.display_books()

