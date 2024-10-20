from datetime import datetime
from books_app.repositories.author_repository import AuthorRepository
from rest_framework.exceptions import PermissionDenied, NotFound

class AuthorComponent:

    def create_author(self, name , birth_date, nationality):
        author_birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()  # Converts string to date object
        AuthorRepository.create_author(name,author_birth_date,nationality)

    def update_author(self, author_id, name, birth_date, nationality):
        author = AuthorRepository.get_author(pk=author_id)

        if author is None:
            raise NotFound("book not found", code=404)
        AuthorRepository.update_author(id, name, birth_date, nationality)

    def get_author(self, author_id):
        author = AuthorRepository.get_author(author_id)
        if author is None:
            raise NotFound("author not found", code=404)
        return author
    
    def get_authors(self):
        authors = AuthorRepository.get_authors()
        return authors
    
    def delete_author(self, author_id):
        author = AuthorRepository.get_author(id=author_id)
        if author is None:
            raise NotFound("author not found", code=404)
        AuthorRepository.delete_author(author_id)

        
