from books_app.models import Author
from books_app.models import session
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from datetime import datetime



class AuthorRepository:

    def __init__(self):
        print("this is AuthorRepository class")

    @staticmethod
    def create_author(self, name, birth_date, nationality, commit=True):
        author = Author(name=name, nationality=nationality,birth_date=birth_date )
        session.add(author)

        if commit:
            session.commit()
        else:
            session.flush()

    @staticmethod
    def update_author(self, author_id, data, commit=True):
        query = session.query(Author).\
            filter(Author.id == author_id).\
            update(data, synchronize_session=False)
        if commit:
            session.commit()   
        else:
                session.flush()

    @staticmethod
    def delete_author(self, author_id, commit=True):
        query = session.query(Author).\
            filter(Author.id == author_id).\
            delete()
        if commit:
            session.commit()
        else:
            session.flush()
        
    @staticmethod
    def get_author(self, author_id):
        author = session.query(Author).filter(Author.id == author_id).one_or_none()
        return author
        
    @staticmethod
    def get_authors(self):
        authors = session.query(Author).all()
        return authors