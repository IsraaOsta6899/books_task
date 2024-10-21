from typing import Any, Dict
from books_app.models import Author
from books_app.models import session
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from datetime import date, datetime



class AuthorRepository:

    def __init__(self):
        print("this is AuthorRepository class")

    @staticmethod
    def create_author(name, birth_date: date, nationality: str, commit=True):
        author = Author(name=name, nationality=nationality, birth_date=birth_date)
        session.add(author)

        if commit:
            session.commit()
        else:
            session.flush()

    @staticmethod
    def update_author(author_id: int, data: Dict[str, Any], commit: bool=True):
        query = session.query(Author).\
            filter(Author.id == author_id).\
            update(data, synchronize_session=False)
        if commit:
            session.commit()   
        else:
            session.flush()

    @staticmethod
    def delete_author(author_id: int, commit=True):
        query = session.query(Author).\
            filter(Author.id == author_id).\
            delete()
        if commit:
            session.commit()
        else:
            session.flush()
        
    @staticmethod
    def get_author(author_id: int):
        author = session.query(Author).filter(Author.id == author_id).one_or_none()
        return author
        
    @staticmethod
    def get_authors():
        authors = session.query(Author).all()
        return authors