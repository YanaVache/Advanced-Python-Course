from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///baza.db"
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    year = db.Column(db.String)
    borrowed_by_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=True)
    borrowed_by = db.relationship("Person", backref=db.backref("books", lazy=True))
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    mail = db.Column(db.String)
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

db.create_all()

@app.route("/books", methods=["GET"])
def list_books():
    books = Book.query.all()
    return jsonify([book.serialize() for book in books])

@app.route("/books", methods=["POST"])
def add_book():
    title = request.json.get("title")
    author = request.json.get("author")
    year = request.json.get("year")
    book = Book(title=title, author=author, year=year)
    db.session.add(book)
    db.session.commit()
    return jsonify(book.serialize()), 201

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.filter_by(id=book_id).first()
    if book:
        return jsonify(book.serialize())
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route("/books/int:book_id", methods=["PUT"])
def update_book(book_id):
    book = Book.query.filter_by(id=book_id).first()
    if book:
        title = request.json.get("title")
        author = request.json.get("author")
        year = request.json.get("year")
        if title:
            book.title = title
        if author:
            book.author = author
        if year:
            book.year = year
        db.session.commit()
        return jsonify(book.serialize())
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route("/books/int:book_id", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.filter_by(id=book_id).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({}), 204
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route("/persons", methods=["GET"])
def list_persons():
    persons = Person.query.all()
    return jsonify([person.serialize() for person in persons])

@app.route("/persons", methods=["POST"])
def add_person():
    name = request.json.get("name")
    mail = request.json.get("mail")
    person = Person(name=name, mail=mail)
    db.session.add(person)
    db.session.commit()
    return jsonify(person.serialize()), 201

@app.route("/persons/int:person_id", methods=["GET"])
def get_person(person_id):
    person = Person.query.filter_by(id=person_id).first()
    if person:
        return jsonify(person.serialize())
    else:
        return jsonify({"error": "Person not found"}), 404

@app.route("/persons/int:person_id", methods=["PUT"])
def update_person(person_id):
    person = Person.query.filter_by(id=person_id).first()
    if person:
        name = request.json.get("name")
        mail = request.json.get("mail")
        if name:
            person.name = name
        if mail:
            person.mail = mail
        db.session.commit()
        return jsonify(person.serialize())
    else:
        return jsonify({"error": "Person not found"}), 404

@app.route("/persons/int:person_id", methods=["DELETE"])
def delete_person(person_id):
    person = Person.query.filter_by(id=person_id).first()
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({}), 204
    else:
        return jsonify({"error": "Person not found"}), 404

@app.route("/borrow", methods=["PUT"])
def borrow_book():
    book_id = request.json.get("book_id")
    person_id = request.json.get("person_id")
    book = Book.query.filter_by(id=book_id).first()
    person = Person.query.filter_by(id=person_id).first()
    if book and person and not book.borrowed_by:
        book.borrowed_by = person
        db.session.commit()
        return jsonify(book.serialize())
    else:
        return jsonify({"error": "Invalid book_id or person_id or book already borrowed"}), 400

@app.route("/return", methods=["PUT"])
def return_book():
    book_id = request.json.get("book_id")
    book = Book.query.filter_by(id=book_id).first()
    if book and book.borrowed_by:
        book.borrowed_by = None
        db.session.commit()
        return jsonify(book.serialize())
    else:
        return jsonify({"error": "Invalid book_id or book not borrowed"}), 400

@app.route("/serialize", methods=["GET"])
def serialize_book():
    book = Book.query.all()
    return jsonify([book.serialize() for book in books])

if __name__ == '__main__':
    app.run(debug=True)


