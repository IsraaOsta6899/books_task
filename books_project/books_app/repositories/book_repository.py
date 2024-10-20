from books_app.models import Book, session
from books_app.repositories.author_repository import AuthorRepository


class BookRepository:
    @staticmethod
    def create_book(self, title, published_year, genr, isbn, author, commit=True):
        book = Book(title=title, published_year=published_year,genre=genr, author=author)
        session.add(book)
        if commit:
            session.commit()  

    @staticmethod
    def update_book(self, book_id, data, commit=True):
            book = session.query(Book).\
                filter(Book.id == book_id).\
                update(data, synchronize_session=False)
            if commit:
                session.commit()
            else:   
                session.flush()

    @staticmethod
    def delete_book(self, book_id, commit=True):
        book = session.query(Book).filter(Book.id == book_id).\
            delete()
        if commit:
            session.commit()

    def get_book(self, book_id):
        book = session.query(Book).\
            filter(Book.id == book_id).\
            one_or_none()
        return book
        
    def get_books(self):
        books = session.query(Book).all()
        return books
    
    def check_isbn_exist(self,isbn):
        isbn = session.query(Book).filter(Book.isbn == isbn).first()
        if isbn is None:
            return False
        else:
            return True
