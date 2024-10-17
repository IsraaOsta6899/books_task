from books_app.models import Author
from books_app.models import session
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from datetime import datetime



class AuthorRepository:

    def __init__(self):
        print("this is AuthorRepository class")

    def create_author(self, name, birth_date, nationality):
        author = Author()
        author.name = name
        date_obj = datetime.strptime(birth_date, '%Y-%m-%d').date()  # Converts string to date object
        author.birth_date = date_obj
        author.nationality= nationality
        session.add(author)
        session.commit()

    def update_author(self, id, name, birth_date, nationality):
        try:
            author = session.query(Author).filter(Author.id == id).one_or_none()
            if author is not None:
                author.name = name
                author.birth_date = birth_date
                author.nationality = nationality
                session.commit()   

        except MultipleResultsFound:
            session.rollback()
            print("Multiple authors found with the specified criteria.")
            raise MultipleResultsFound("Multiple authors found with the specified criteria.")
            

    def delete_author(self, id):
        try:
            author = session.query(Author).filter(Author.id == id).one_or_none()
            if author is not None:
                session.delete(author)
                session.commit()
          
        except MultipleResultsFound:
            session.rollback()
            raise MultipleResultsFound("Multiple authors found with the specified criteria.")
        except Exception as e:
            session.rollback()  # Rollback for any other errors
            raise Exception("another exception")


    def get_author(self, id):
        try:
            author = session.query(Author).filter(Author.id == id).one_or_none()
            return author
        except MultipleResultsFound:
            print("Multiple authors found with the specified criteria.")
            session.rollback()  # Rollback if multiple results were found
            
        except Exception as e:
            print(f"An error occurred: {e}")
            session.rollback()  # Rollback for any other errors
            

    def get_list_of_authors(self):
        authors_list = session.query(Author).all()
        return authors_list