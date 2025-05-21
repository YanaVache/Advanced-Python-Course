import requests
import json


def add_book(title, author, year):
    data = {"title": title, "author": author, "year": year}
    response = requests.post("http://localhost:8000/books", json=data)
    if response.status_code == 201:
        print("Book added successfully")
    else:
        print("Error adding book")


def add_person(name, mail):
    data = {"name": name, "mail": mail}
    response = requests.post("http://localhost:8000/persons", json=data)
    if response.status_code == 201:
        print("Person added successfully")
    else:
        print("Error adding person")


def list_books():
    response = requests.get("http://localhost:8000/books")
    if response.status_code == 200:
        books = json.loads(response.text)
        for book in books:
            print(f'{book["title"]} by {book["author"]} published in {book["year"]}')
    else:
        print("Error getting book list")


def list_persons():
    response = requests.get("http://localhost:8000/persons")
    if response.status_code == 200:
        persons = json.loads(response.text)
        for person in persons:
            print(f'{person["name"]} email: {person["mail"]}')
    else:
        print("Error getting persons list")


def get_book(book_id):
    response = requests.get(f"http://localhost:8000/books/{book_id}")
    if response.status_code == 200:
        book = json.loads(response.text)
        print(f'{book["title"]} by {book["author"]} published in {book["year"]}')
    elif response.status_code == 404:
        print("Book not found")
    else:
        print("Error getting book")


def get_person(person_id):
    response = requests.get(f"http://localhost:8000/persons/{person_id}")
    if response.status_code == 200:
        person = json.loads(response.text)
        print(f'{person["name"]} email: {person["mail"]}')
    elif response.status_code == 404:
        print("Person not found")
    else:
        print("Error getting person")


def update_book(book_id, title=None, author=None, year=None):
    data = {}
    if title:
        data["title"] = title
    if author:
        data["author"] = author
    if year:
        data["year"] = year
    response = requests.put(f"http://localhost:8000/books/{book_id}", json=data)
    if response.status_code == 200:
        print("Book updated successfully")
    elif response.status_code == 404:
        print("Book not found")
    else:
        print("Error updating book")


def update_person(person_id, name=None, mail=None):
    data = {}
    if name:
        data["name"] = name
    if mail:
        data["mail"] = mail
    response = requests.put(f"http://localhost:8000/persons/{person_id}", json=data)
    if response.status_code == 200:
        print("Person updated successfully")
    elif response.status_code == 404:
        print("Person not found")
    else:
        print("Error updating person")


def delete_book(book_id):
    response = requests.delete(f"http://localhost:8000/books/{book_id}")
    if response.status_code == 204:
        print("Book deleted successfully")
    elif response.status_code == 404:
        print("Book not found")
    else:
        print("Error deleting book")


def delete_person(person_id):
    response = requests.delete(f"http://localhost:8000/persons/{person_id}")
    if response.status_code == 204:
        print("Person deleted successfully")
    elif response.status_code == 404:
        print("Person not found")
    else:
        print("Error deleting person")


def borrow_book(book_id, person_id):
    data = {"book_id": book_id, "person_id": person_id}
    response = requests.put("http://localhost:8000/borrow", json=data)
    if response.status_code == 200:
        print("Book borrowed successfully")
    else:
        print("Error borrowing book")

def return_book(book_id):
    data = {"book_id": book_id}
    response = requests.put("http://localhost:8000/return", json=data)
    if response.status_code == 200:
        print("Book returned successfully")
    else:
        print("Error returning book")

