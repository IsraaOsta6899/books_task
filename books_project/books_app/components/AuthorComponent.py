from books_app.Reposetories.AuthorRepository import AuthorRepository
from books_app.models import Author
class AuthorComponent:

    def __init__(self):
        self.author_repository = AuthorRepository()

    def create_author(self, name , birth_date, nationality):
        
        self.author_repository.create_author(name,birth_date,nationality)

    def update_author(self, pk, name, birth_date, nationality):

        self.author_repository.update_author(pk, name, birth_date, nationality)

    def get_author(self, pk):

        author = self.author_repository.get_author(pk)
        return author
    
    def get_authors_list(self):
        objects = self.author_repository.get_list_of_authors()
        return objects
    
    def delete_author(self, pk):
        self.author_repository.delete_author(pk)

        
