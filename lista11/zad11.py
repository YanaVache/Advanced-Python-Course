from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///baza.db', echo=False)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'Book'
    id = Column(Integer, primary_key=True)
    author = Column(String)
    title = Column(String)
    year = Column(String)
    borrowed_by_id = Column(Integer, ForeignKey('Person.id'),nullable = 'True')

class Person(Base):
    __tablename__ = 'Person'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    mail = Column(String)
    borrowed = relationship('Book', backref = 'borrowed_by')

Base.metadata.create_all(engine)

def add_friend():
    Session = sessionmaker(bind = engine)
    session = Session()
    name = input('Enter the name ')
    mail = input('Enter the mail ')
    friend = Person(name = name, mail = mail)
    session.add(friend)
    session.commit()
    session.close()

def add_book():
    Session = sessionmaker(bind = engine)
    session = Session()
    title = input('Enter the title ')
    author = input('Enter the author ')
    year = input('Enther the year ')
    book = Book(title = title, author = author, year = year)
    session.add(book)
    session.commit()
    session.close()

def borrow():
    Session = sessionmaker(bind = engine)
    session = Session()
    person_name = input('Enter the person who is borrowing ')
    book_title = input('Enter the title of the book ')
    person = session.query(Person).filter(Person.name == person_name).first()
    book = session.query(Book).filter(Book.title == book_title).first()
    if person is None or book is None:
        print("There is no such data in the database")
    else:
        if book.borrowed_by is None:
            book.borrowed_by = person
            session.commit()
        else: print("The book is already borrowed")
    session.close()

def return_book():
    Session = sessionmaker(bind = engine)
    session = Session()
    person_name = input('Name the person who is returning the books ')
    person = session.query(Person).filter(Person.name == person_name).first()
    if person is None:
        print("There is no such data in the database")
    else:
        books = person.borrowed
        if not books:
            print("This person does not have a borrowed book")
        else:
            if len(books) > 1:
                book_title = input('Enter the title of the book ')
                book = session.query(Book).filter(Book.title == book_title).first()
            else: book = books[0]
            book.borrowed_by = None
            session.commit()
    session.close()

import sys
command_map = {
           "add_book": add_book,
           "add_friend": add_friend,
           "borrow": borrow,
           "return": return_book}
if sys.argv[1:]:
    try:
        action = command_map[sys.argv[1]]
        action()
    except:
        print("unknown command")