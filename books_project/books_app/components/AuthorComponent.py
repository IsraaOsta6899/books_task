from books_app.Reposetories.AuthorRepository import AuthorRepository
from rest_framework.exceptions import PermissionDenied, NotFound

class AuthorComponent:

    def __init__(self):
        self.author_repository = AuthorRepository()

    def create_author(self, name , birth_date, nationality):
        
        self.author_repository.create_author(name,birth_date,nationality)

    def update_author(self, id, name, birth_date, nationality):

        author = self.author_repository.get_author(pk=id)
        if author is None:
            raise NotFound("book not found", code=404)
        else:
            self.author_repository.update_author(id, name, birth_date, nationality)

    def get_author(self, id):
        author = self.author_repository.get_author(id)
        if author is None:
            raise NotFound("author not found", code=404)
        return author
    
    def get_authors_list(self):
        authors_list = self.author_repository.get_list_of_authors()
        return authors_list
    
    def delete_author(self, id):
        author = self.author_repository.get_author(id=id)
        if author is None:
            raise NotFound("author not found", code=404)
        else:
            self.author_repository.delete_author(id)

        
