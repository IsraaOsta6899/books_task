from typing import List

from books_app.models import Book
from books_app.repositories.book_repository import BookRepository
from rest_framework.exceptions import NotFound, ValidationError
from books_app.repositories.author_repository import AuthorRepository

class BookComponent:

    @staticmethod
    def create_book(title: str, published_year: int, genr: str, isbn: str, author_id: int):
        exists = BookRepository.check_isbn_exist(isbn)
        author = AuthorRepository.get_author(author_id=author_id)
        if not author:
            raise NotFound("author not found", code=404)
        elif not title:
            raise ValidationError(detail="title is required", code=400)
        elif exists:
            raise ValidationError(detail="isbn is already exists", code=400)
        BookRepository.create_book(title=title, published_year=published_year,
                                   genr=genr, isbn=isbn, author=author)

    @staticmethod
    def update_book(book_id: int, title: str, published_year: int, genr: str, isbn: str, author_id: int,
                    **kwargs):
        book_data = {
            'id': book_id,
            'title': title,
            'published_year': published_year,
            'genre': genr,
            'isbn': isbn,
        }

        book_data.update(kwargs)
        author = AuthorRepository.get_author(author_id=author_id)
        if not author:
            raise NotFound("author not found", code=404)
        else:
            book_data.update(kwargs)  # add author obj

        book = BookRepository.get_book(book_id=book_id)
        if book is None:
            raise NotFound("book not found", code=404)
        elif title == "":
            raise ValidationError(detail="title is required or isbn is already exists", code=400)
        elif BookRepository.check_isbn_exist(isbn):
            raise ValidationError(detail="title is required or isbn is already exists", code=400)

        BookRepository.update_book(book_id=book_id, data=book_data, commit=True)

    @staticmethod
    def get_book(book_id: int) -> Book:
        book = BookRepository.get_book(book_id=book_id)
        if book is None:
            raise NotFound("book not found", code=404)
        return book

    @staticmethod
    def get_books() -> List[Book]:
        books = BookRepository.get_books()
        return books

    @staticmethod
    def delete_book(book_id: int):
        book = BookRepository.get_book(book_id=book_id)
        if book is None:
            raise NotFound("book not found", code=404)
        BookRepository.delete_book(book_id=book_id, commit=True)
