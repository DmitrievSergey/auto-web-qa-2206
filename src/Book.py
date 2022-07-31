from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    genre: str
    pages: int
