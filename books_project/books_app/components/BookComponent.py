from books_app.Reposetories.BookRepository import BookRepository
from books_app.models import Book
class BookComponent:

    def __init__(self):
        self.book_repository = BookRepository()

    def create_book(self, title, published_year, genr, isbn, author_id):
        #  TODO: validate required fields
        self.book_repository.create_book(title, published_year, genr, isbn, author_id)

    def update_book(self, pk, title, published_year, genr, isbn, author_id):
        #  TODO: check if book exists and raise a ResourceException if it doesn't
        self.book_repository.update_book(pk, title, published_year, genr, isbn, author_id)

    def get_book(self, pk):
        book = self.book_repository.get_book(pk)
        return book
    # TODO: rename to get_books
    def get_books_list(self):
        # TODO: rename objects to books
        objects = self.book_repository.get_list_of_book()
        return objects
    
    def delete_book(self, pk):
        self.book_repository.delete_book(pk)

        
