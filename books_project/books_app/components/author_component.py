from datetime import datetime
from books_app.repositories.author_repository import AuthorRepository
from rest_framework.exceptions import PermissionDenied, NotFound
from books_project.constants import DateTimeFormat

class AuthorComponent:

    def create_author(self, name: str, birth_date: str, nationality: str):
        author_birth_date = datetime.strptime(birth_date, DateTimeFormat.ISO_DATE_FORMAT).date()  # Converts string to date object
        AuthorRepository.create_author(name=name, birth_date=author_birth_date, nationality=nationality)

    def update_author(self, author_id: int, name: str, birth_date: str, nationality: str):
        author = AuthorRepository.get_author(pk=author_id)
        author_birth_date = datetime.strptime(birth_date, DateTimeFormat.ISO_DATE_FORMAT).date()  # Converts string to date object
        author_data = {
            "name": name,
            "birth_date": author_birth_date,
            "nationality": nationality
        }
        if author is None:
            raise NotFound("book not found", code=404)
        AuthorRepository.update_author(author_id=author_id, data=author_data)

    def get_author(self, author_id: int):
        author = AuthorRepository.get_author(author_id=author_id)
        if author is None:
            raise NotFound("author not found", code=404)
        return author
    
    def get_authors(self):
        authors = AuthorRepository.get_authors()
        return authors
    
    def delete_author(self, author_id: int):
        author = AuthorRepository.get_author(id=author_id)
        if author is None:
            raise NotFound("author not found", code=404)
        AuthorRepository.delete_author(author_id=author_id)