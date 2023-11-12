
#Task 2
#Library

class Author:
    def __init__(self, name, country, birthday):
        self.name, self.country, self.birthday, self.books = name, country, birthday, []

    def __repr__(self):
        return f"Author({self.name}, {self.country}, {self.birthday})"

class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name, self.year, self.author = name, year, author
        author.books.append(self)
        Book.total_books += 1

    def __repr__(self):
        return f"Book({self.name}, {self.year}, {self.author})"

class Library:
    def __init__(self, name):
        self.name, self.books, self.authors = name, [], []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        self.authors.append(author) if author not in self.authors else None
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library({self.name}, Books: {len(self.books)}, Authors: {len(self.authors)})"

author1 = Author("John Doe", "USA", "1990-01-01")
author2 = Author("Jane Smith", "UK", "1985-03-15")

library = Library("City Library")

book1 = library.new_book("Book1", 2000, author1)
book2 = library.new_book("Book2", 2005, author2)

print(book1, book2)
print(library.group_by_author(author1), library.group_by_year(2005))
print(library)
