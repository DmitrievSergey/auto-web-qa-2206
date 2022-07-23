from typing import List

from src.Book import Book


class Target:

    def __init__(self, name, gender, address, age, books: List[Book]):
        self.name = name
        self.gender = gender
        self.address = address
        self.age = age
        self.books = books

