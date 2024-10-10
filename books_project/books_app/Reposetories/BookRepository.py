from books_app.models import Author, Book

class BookRepository:

    def __init__(self):
        print("this is AuthorRepository class")

    def create_book(self, title, published_year, genr, isbn, author_id):
        book = Book()
        book.title = title
        book.published_year = published_year
        book.genre = genr
        book.isbn = isbn
        author = Author.objects.get(pk=author_id)
        book.author = author
        book.save()

    def update_book(self, pk, title, published_year, genr, isbn, author_id):
        book_instance = Book.objects.get(pk = pk)
        # data = json.loads(request.body)
        book_instance.title = title
        book_instance.published_year = published_year
        book_instance.genre = genr
        book_instance.isbn = isbn
        author = Author.objects.get(pk=author_id)
        book_instance.author = author
        book_instance.save()

    def delete_book(self, pk):
        book_instance = Book.objects.get(pk = pk)
        book_instance.delete()

    def get_book(self, pk):
         obj = Book.objects.get(pk=pk)
         return obj

    def get_list_of_book(self):
        objects = Book.objects.all()
        return objects
