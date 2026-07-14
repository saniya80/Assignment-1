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
        book = Book(title)
        self.books.append(book)
        print(title, "added successfully.")

    def register_patron(self, name):
        patron = Patron(name)
        self.patrons.append(patron)
        print(name, "registered successfully.")

    def borrow_book(self, patron_name, book_title):
        for patron in self.patrons:
            if patron.name == patron_name:
                for book in self.books:
                    if book.title == book_title and book.available:
                        book.available = False
                        patron.borrowed_books.append(book)
                        print(patron_name, "borrowed", book_title)
                        return
                print("Book not available.")
                return
        print("Patron not found.")

    def return_book(self, patron_name, book_title):
        for patron in self.patrons:
            if patron.name == patron_name:
                for book in patron.borrowed_books:
                    if book.title == book_title:
                        book.available = True
                        patron.borrowed_books.remove(book)
                        print(book_title, "returned successfully.")
                        return
                print("Book not borrowed.")
                return
        print("Patron not found.")

    def display_books(self):
        print("\\nLibrary Books:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(book.title, "-", status)


library = Library()

library.add_book("Python Programming")
library.add_book("Data Structures")
library.add_book("Machine Learning")

library.register_patron("Saniya")
library.register_patron("Rahul")

library.display_books()

library.borrow_book("Saniya", "Python Programming")

library.display_books()

library.return_book("Saniya", "Python Programming")

library.display_books()

"""
Expected Output:

Python Programming added successfully.
Data Structures added successfully.
Machine Learning added successfully.
Saniya registered successfully.
Rahul registered successfully.

Library Books:
Python Programming - Available
Data Structures - Available
Machine Learning - Available

Saniya borrowed Python Programming

Library Books:
Python Programming - Borrowed
Data Structures - Available
Machine Learning - Available

Python Programming returned successfully.

Library Books:
Python Programming - Available
Data Structures - Available
Machine Learning - Available
"""
