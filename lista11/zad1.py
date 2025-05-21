from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, create_engine
from sqlalchemy.orm import validates, relationship, sessionmaker
from sqlalchemy.sql import func
import datetime

engine = create_engine("sqlite:///:memory:", echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = "Book"

    id = Column(Integer, primary_key = True)
    title = Column(String, nullable= False)
    author = Column(String, nullable= False)
    year = Column(Integer)
    wypozyczyl = relationship("Znajomi")


class Znajomi(Base):
    __tablename__ = "Znajomi"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    @validates("email")
    def validate_email(self, key, value):
        assert "@" in value
        return value

    ksiega = Column(Integer, ForeignKey("Book.id"))

    #mieszkaniec = Column(Integer, ForeignKey("Osoba.id"))



Base.metadata.create_all(engine)


Session = sessionmaker(bind = engine)

sesja = Session()

ks1 = Book(title= "Martin Iden", author="Jack London", year=1909)
zn1 = Znajomi(name="Basia", email="basia1223@gmail.com")
zn2 = Znajomi(name="Leszek", email="lechiskrzycki@gmail.com")
ks1.wypozyczyl = [zn1, zn2]
sesja.add_all([zn1, zn2, ks1])



import sys

def dodaj(lista):
    x1 = Book(title=lista[0], author=lista[1], year=int(lista[2]))

def wypozycz(lista):
    os1 = Znajomi(name=lista[0], email=lista[1])
    ks1.wypozyczyl = os1

def oddaj(lista):
    os1 = Znajomi(name=lista[0], email=lista[1])
    a = ks1.wypozyczyl
    for i in range(len(a)):
        if a[i] == os1:
            a[i] = ''


#sys.argv[1] to dodawanie / wypozyczanie / oddawanie ksiazek
#sys.argv[2] to [zmienna, title, author, year]
if sys.argv[1] == "dodaj":
    # sys.argv[2] to [title, author, year]
    dodaj(sys.argv[2])
elif sys.argv[1] == "wypożycz":
    # sys.argv[2] to [name, mail]
    wypozycz(sys.argv[2])
elif sys.argv[1] == "oddaj":
    # sys.argv[2] to [name, mail]
    oddaj(sys.argv[2])


sesja.commit()