class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title):
        self.books.append(Book(title))
        print(f"Book '{title}' added successfully.")

    def register_patron(self, name):
        self.patrons.append(Patron(name))
        print(f"Patron '{name}' registered successfully.")

    def borrow_book(self, patron_name, book_title):
        patron = next((p for p in self.patrons if p.name == patron_name), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if patron and book and book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print(f"{patron_name} borrowed '{book_title}'.")
        else:
            print("Book not available or patron not found.")

    def return_book(self, patron_name, book_title):
        for p in self.patrons:
            if p.name == patron_name:
                for b in p.borrowed_books:
                    if b.title == book_title:
                        b.available = True
                        p.borrowed_books.remove(b)
                        print(f"{patron_name} returned '{book_title}'.")
                        return
        print("Return failed.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.title} - {status}")


library = Library()
library.add_book("Python Basics")
library.add_book("Data Structures")
library.add_book("Machine Learning")

library.register_patron("Saniya")
library.register_patron("Rahul")

library.borrow_book("Saniya", "Python Basics")
library.display_books()

library.return_book("Saniya", "Python Basics")
library.display_books()
