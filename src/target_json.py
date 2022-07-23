import json
import csv

from src.Book import Book
from src.Target import Target
from src.Users import Users

users_list = []
active_user_list = []
user_books = []
with open("/Users/sergejdmitriev/Otus/qa_python/auto-web-qa-2206/users.json", "r") as f:
    users = json.loads(f.read())
    for user in users:
        users_list.append(Users(**user))

books_list = []
with open('/Users/sergejdmitriev/Otus/qa_python/auto-web-qa-2206/books.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        book = Book(row.get('Title'), row.get('Author'), row.get('Genre'), row.get('Pages'))
        books_list.append(book)


def final_json():
    for i in range(len(users_list) - 1, -1, -1):
        book_u = []
        user_cnt = len(users_list)
        book_cnt = len(books_list)
        user_books_cnt = book_cnt // user_cnt
        t = Target(users_list[i].name, users_list[i].gender, users_list[i].address, users_list[i].age, book_u)
        for j in range(len(books_list) - 1, -1, -1):
            t.books.append(books_list[j])
            user_books_cnt -= 1
            books_list.remove(books_list[j])
            if user_books_cnt == 0:
                users_list.remove(users_list[i])
                break
        user_books.append(t)
    return user_books


user_books = final_json()
with open("result.json", "w") as outfile:
    json.dump(user_books, outfile, default=lambda o: o.__dict__, indent=4)

