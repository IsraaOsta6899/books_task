from books_app.models import Book, session
from sqlalchemy.exc import MultipleResultsFound
from rest_framework.exceptions import PermissionDenied, NotFound
from books_app.Reposetories.AuthorRepository import AuthorRepository


class BookRepository:
    author_repository = AuthorRepository()
    def __init__(self):
        print("this is AuthorRepository class")

    def create_book(self, title, published_year, genr, isbn, author_id):
        new_book = Book()
        new_book.title = title
        new_book.published_year = published_year
        new_book.genre = genr
        new_book.isbn = isbn

        author = self.author_repository.get_author(id=author_id)

        if author is not None:
            new_book.author = author
            session.add(new_book)
            session.commit()  
            session.close()

        else:
            raise NotFound("author not found")

    def update_book(self, id, title, published_year, genr, isbn, author_id):
        try:
            book = session.query(Book).filter(Book.id == id).one_or_none()
            if book is not None:
                book.title = title
                book.published_year = published_year
                book.genre = genr
                book.isbn = isbn
                session.commit()   
                session.close()

        except MultipleResultsFound:
            session.rollback()
            print("Multiple books found with the specified criteria.")
            raise MultipleResultsFound("Multiple books found with the specified criteria.")
            
        finally:
            # Close the session
            session.close()

    def delete_book(self, id):
        try:
            book = session.query(Book).filter(Book.id == id).one_or_none()
            if book is not None:
                session.delete(book)
                session.commit()
                session.close()
          
        except MultipleResultsFound:
            session.rollback()
            raise MultipleResultsFound("Multiple books found with the specified criteria.")
        except Exception as e:
            session.rollback()  # Rollback for any other errors
            raise Exception("another exception")
        finally:
            # Close the session
            session.close()

    def get_book(self, id):
        try:
            book = session.query(Book).filter(Book.id == id).one_or_none()
            return book
        except MultipleResultsFound:
            print("Multiple books found with the specified criteria.")
            session.rollback()  # Rollback if multiple results were found
            
        except Exception as e:
            print(f"An error occurred: {e}")
            session.rollback()  # Rollback for any other errors
            
        finally:
            # Close the session
            session.close()


    def get_book_list(self):
        books_list = session.query(Book).all()
        return books_list
    
    def check_isbn_exist(self,isbn):
        isbn = session.query(Book).filter_by(isbn=isbn).first()
        if isbn is None:
            return False
        else:
            return True
