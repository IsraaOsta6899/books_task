import re
from marshmallow import ValidationError
from sqlalchemy import DateTime, Table, Column, Integer, ForeignKey, String, create_engine, desc, Table, Date, func, Enum
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as MyEnum
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
def validate_fixed_length():
    print("")
    
class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(100), nullable = False)
    birth_date = Column(Date, nullable = True)
    nationality = Column(String(100), nullable = True)
    books = relationship('Book', back_populates='author', cascade='all, delete, save-update')
    created = Column(DateTime, nullable=True)
    updated = Column(DateTime, nullable=True)

    def __repr__(self):
        return (f'author name is {self.name}')
    
class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String(200), nullable = False)
    published_year = Column(Integer, nullable = False)
    genre = Column(String(100), nullable=True)
    isbn = Column(String(13), nullable = False, unique = True)
    borrowings = relationship("Borrowing", back_populates="book", cascade="all, delete, save-update")
    author_id = Column(ForeignKey('author.id', ondelete='CASCADE', onupdate='CASCADE'))
    author = relationship('Author', back_populates='books', cascade='all, delete, save-update')
    created = Column(DateTime, nullable=True)
    updated = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Book(id={self.id}, isbn='{self.isbn}')>"

class MembershipStatus(MyEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"  

class Member(Base):
    __tablename__ = 'member'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(100), nullable = False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(10), unique=True, nullable=True)
    address = Column(String(50), nullable=True)
    membership_date = Column(DateTime, nullable=True)
    membership_status = Column(Enum(MembershipStatus), nullable=False, default=MembershipStatus.ACTIVE)
    borrowings = relationship('Borrowing', back_populates="member", cascade= "all, delete, save-update")
    created = Column(DateTime, nullable=True)
    updated = Column(DateTime, nullable=True)

class Borrowing(Base):
    __tablename__ = 'borrowing'
    id = Column(Integer, primary_key = True, autoincrement = True)
    borrow_date = Column(Date, nullable=False)
    due_date = Column(Date,  nullable=False)
    return_date = Column(Date, nullable=True)
    book_id = Column(ForeignKey("book.id", ondelete="CASCADE", onupdate='CASCADE'))
    member_id = Column(ForeignKey("member.id", ondelete="CASCADE", onupdate='CASCADE'))
    member = relationship("Member", back_populates="borrowings", cascade="all, delete, save-update")
    book = relationship("Book", back_populates="borrowings", cascade="all, delete, save-update")
    fine = relationship('Fine', back_populates='borrow', cascade="all, delete, save-update")
    created = Column(DateTime, nullable=True)
    updated = Column(DateTime, nullable=True)

class FineStatus(MyEnum):
        RETURNED = 'RETURNED'
        NOTRETURNED = 'NOT-RETURNED'
class Fine(Base):
    __tablename__ = 'fine'
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    fine_amount = Column(Integer, nullable=True)
    fine_status = Column(Enum(FineStatus), default=FineStatus.NOTRETURNED)
    borrow_id = Column(ForeignKey('borrowing.id', ondelete='CASCADE', onupdate='CASCADE'))
    borrow = relationship('Borrowing', back_populates='fine', cascade="all, delete, save-update")
    created = Column(DateTime, nullable=True)
    updated = Column(DateTime, nullable=True)

engine = create_engine('sqlite:///taskdb.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables in the database
Base.metadata.create_all(engine)
