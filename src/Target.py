from typing import List
from dataclasses import dataclass
from src.Book import Book

@dataclass
class Target:
    name: str
    gender: str
    address: str
    age: int
    books: List[Book]
 #   def __init__(self, name, gender, address, age, books: List[Book]):
 #       self.name = name
 #       self.gender = gender
 #       self.address = address
 #       self.age = age
 #       self.books = books
