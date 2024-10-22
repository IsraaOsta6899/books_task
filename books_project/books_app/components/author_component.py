from datetime import datetime

from typing import List

from books_app.models import Author
from books_app.repositories.author_repository import AuthorRepository
from rest_framework.exceptions import NotFound
from constants import DateTimeFormat

class AuthorComponent:

    @staticmethod
    def create_author(name: str, birth_date: str, nationality: str):
        author_birth_date = datetime.strptime(birth_date, DateTimeFormat.ISO_DATE_FORMAT).date()  # Converts string to date object
        AuthorRepository.create_author(name=name, birth_date=author_birth_date, nationality=nationality)

    @staticmethod
    def update_author(author_id: int, name: str, birth_date: str, nationality: str):
        author = AuthorRepository.get_author(author_id=author_id)
        author_birth_date = datetime.strptime(birth_date, DateTimeFormat.ISO_DATE_FORMAT).date()  # Converts string to date object
        author_data = {
            "name": name,
            "birth_date": author_birth_date,
            "nationality": nationality
        }
        if author is None:
            raise NotFound("book not found", code=404)
        AuthorRepository.update_author(author_id=author_id, data=author_data)

    @staticmethod
    def get_author(author_id: int) -> Author:
        author = AuthorRepository.get_author(author_id=author_id)
        if author is None:
            raise NotFound("author not found", code=404)
        return author

    @staticmethod
    def get_authors() -> List[Author]:
        authors = AuthorRepository.get_authors()
        return authors

    @staticmethod
    def delete_author(author_id: int):
        author = AuthorRepository.get_author(author_id=author_id)
        if author is None:
            raise NotFound("author not found", code=404)
        AuthorRepository.delete_author(author_id=author_id)