from books_app.Reposetories.BookRepository import BookRepository
from rest_framework.exceptions import NotFound, ValidationError

class BookComponent:

    def __init__(self):
        self.book_repository = BookRepository()

    def create_book(self, title, published_year, genr, isbn, author_id):
        exists = self.book_repository.check_isbn_exist(isbn)
        if title != "" and not exists:
            self.book_repository.create_book(title, published_year, genr, isbn, author_id)
        else:
            raise ValidationError(detail="title is required or isbn is already exists", code=400)

    def update_book(self, id, title, published_year, genr, isbn, author_id):
        book = self.book_repository.get_book(pk=id)
        if book is None:
            raise NotFound("book not found", code=404)
        else:
            exists = self.book_repository.check_isbn_exist(isbn)
            if title != "" and not exists:
                self.book_repository.update_book(id, title, published_year, genr, isbn, author_id)
            else:
                raise ValidationError(detail="title is required or isbn is already exists", code=400)

    def get_book(self, id):
        book = self.book_repository.get_book(id)
        if book is None:
            raise NotFound("book not found", code=404)
        return book
    
    def get_books_list(self):
        books_list = self.book_repository.get_book_list()
        return books_list
    
    def delete_book(self, id):
        book = self.book_repository.get_book(pk=id)
        if book is None:
            raise NotFound("book not found", code=404)
        else:
            self.book_repository.delete_book(id)

        