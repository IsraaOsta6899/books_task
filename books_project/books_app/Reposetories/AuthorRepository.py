from books_app.models import Author

class AuthorRepository:

    def __init__(self):
        print("this is AuthorRepository class")

    def create_author(self, name, birth_date, nationality):
        author = Author()
        author.name = name
        author.birth_date = birth_date
        author.nationality= nationality
        author.save()

    def update_author(self, pk, name, birth_date, nationality):
        author_instance = Author.objects.get(pk = pk)
        # data = json.loads(request.body)
        author_instance.name = name
        author_instance.birth_date = birth_date
        author_instance.nationality = nationality
        author_instance.save()

    def delete_author(self, pk):
        author_instance = Author.objects.get(pk = pk)
        author_instance.delete()

    def get_author(self, pk):
         obj = Author.objects.get(pk=pk)
         return obj

    def get_list_of_authors(self):
        objects = Author.objects.all()
        return objects
