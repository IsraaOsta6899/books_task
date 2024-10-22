import re
from marshmallow import ValidationError
from sqlalchemy import DateTime, Column, Integer, ForeignKey, String, create_engine, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from constants import FineStatus, MembershipStatus

Base = declarative_base()

def validate_fixed_length():
    print("")
class Parent:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=True)
    updated = Column(DateTime, nullable=True)

class Author(Parent, Base):
    __tablename__ = 'author'
    name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=True)
    nationality = Column(String(100), nullable=True)
    books = relationship('Book', back_populates='author', cascade='all, delete, save-update')

    def __repr__(self):
        return f'Author name is {self.name}'


class Book(Parent, Base):
    __tablename__ = 'book'
    title = Column(String(200), nullable=False)
    published_year = Column(Integer, nullable=False)
    genre = Column(String(100), nullable=True)
    isbn = Column(String(13), nullable=False, unique=True)
    borrowings = relationship("Borrowing", back_populates="book", cascade="all, delete, save-update")

    author_id = Column(Integer, ForeignKey('author.id', ondelete='CASCADE', onupdate='CASCADE'))  # Reference to Parent
    author = relationship('Author', back_populates='books', cascade='all, delete, save-update')
    def __repr__(self):
        return f"<Book(id={self.id}, isbn='{self.isbn}')>"


class Member(Parent, Base):
    __tablename__ = 'member'
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(10), unique=True, nullable=True)
    address = Column(String(50), nullable=True)
    membership_date = Column(DateTime, nullable=True)
    membership_status = Column(MembershipStatus.as_enum(), nullable=False, default=MembershipStatus.ACTIVE)
    borrowings = relationship('Borrowing', back_populates="member", cascade="all, delete, save-update")


class Borrowing(Parent, Base):
    __tablename__ = 'borrowing'
    borrow_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)

    book_id = Column(Integer, ForeignKey("book.id", ondelete="CASCADE", onupdate='CASCADE'))  # Reference to Parent
    member_id = Column(Integer, ForeignKey("member.id", ondelete="CASCADE", onupdate='CASCADE'))  # Reference to Parent

    member = relationship("Member", back_populates="borrowings", cascade="all, delete, save-update")
    book = relationship("Book", back_populates="borrowings", cascade="all, delete, save-update")

    fine = relationship('Fine', back_populates='borrow', cascade="all, delete, save-update")


class Fine(Parent, Base):
    __tablename__ = 'fine'
    fine_amount = Column(Integer, nullable=True)
    fine_status = Column(FineStatus.as_enum(), default=FineStatus.NOTRETURNED)

    borrow_id = Column(Integer, ForeignKey('borrowing.id', ondelete='CASCADE', onupdate='CASCADE'))  # Reference to Parent
    borrow = relationship('Borrowing', back_populates='fine', cascade="all, delete, save-update")


# Database setup
engine = create_engine('sqlite:///taskdb.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables in the database
Base.metadata.create_all(engine)
