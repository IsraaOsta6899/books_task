from rest_framework import response, status, viewsets
import json
from books_app.components.author_component import AuthorComponent
from books_app.components.book_component import BookComponent
from books_app.components.member_component import MemberComponent
from books_app.components.borrowing_component import BorrowingComponent
from books_app.components.fine_component import FineComponent
from .serializers import BookSchemaSerializer, AuthorSchemaSerializer, MemberSchemaSerializer, FineSchemaSerializer, BorrowingSchemaSerializer
from rest_framework.decorators import action

class BookViewSet(viewsets.ModelViewSet):

    book_component = BookComponent()
    serializer_class = BookSchemaSerializer
    
    def list(self, request, *args, **kwargs):
        books = self.book_component.get_books()  # This should return a list
        try:
            serializer = BookSchemaSerializer(many = True)
            return response.Response(serializer.dump(books))
        except Exception as e:
            print("Serializer error:", e)  # Print any serializer errors for debugging
            return response.Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, pk=None):
        book = self.book_component.get_book(book_id=pk)
        serializer = BookSchemaSerializer()
        return response.Response(serializer.dump(book))

    def create(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            title = data.get('title')
            published_year = data.get('published_year')
            genre = data.get('genre')
            isbn = data.get('isbn')
            author_dict = data.get('author')
            author_id = author_dict.get('id')
            self.book_component.create_book(title=title, published_year=published_year,genr=genre,isbn=isbn,author_id=author_id)
            return response.Response({'message': 'Book created successfully.'}, status=201)  # Assuming you have a to_dict method
        except json.JSONDecodeError:
            return response({'error': 'Invalid JSON'}, status=400)
        
    def destroy(self, request, pk):
        self.book_component.delete_book(book_id=pk)
        return response.Response({'message': 'Book deleted successfully.'}, status=204)

    def update(self, request, pk):
        data = json.loads(request.body)
        title = data.get('title')
        published_year = data.get('published_year')
        genre = data.get('genre')
        isbn = data.get('isbn')
        self.book_component.update_book(book_id=pk, title=title, published_year=published_year, genr=genre, isbn=isbn)
        return response.Response({'message': 'Book updated successfully.'}, status=204)    

class AuthorViewSet(viewsets.ModelViewSet):

    def __init__(self, *args, **kwargs):
        self.author_component = AuthorComponent()  # Ensure this is correct
        self.serializer_class = AuthorSchemaSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        author = self.author_component.get_author(author_id=pk)
        serializer = AuthorSchemaSerializer()
        return response.Response(serializer.dump(author))

    
    def list(self, request, *args, **kwargs):
        authors = self.author_component.get_authors()
        serializer = AuthorSchemaSerializer(many = True)
        return response.Response(serializer.dump(authors))
    
    def create(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)

            name = data.get('name')
            birth_date = data.get('birth_date')
            nationality = data.get('nationality')
            self.author_component.create_author(name=name, birth_date=birth_date, nationality=nationality)
            return response.Response({'message': 'Author created successfully.'}, status=201)  # Assuming you have a to_dict method
        except json.JSONDecodeError:
            return response.Response({'error': 'Invalid JSON'}, status=400)
    
    def destroy(self, request, pk):
        self.author_component.delete_author(author_id=pk)
        return response.Response({'message': 'Author deleted successfully.'}, status=204)

class MemberViewSet(viewsets.ModelViewSet):

    member_component = MemberComponent()

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        member = self.member_component.get_member(member_id=pk)
        serializer = MemberSchemaSerializer()
        return response.Response(serializer.dump(member))

    
    def list(self, request, *args, **kwargs):
        members = self.member_component.get_members()
        serializer = MemberSchemaSerializer(many = True)
        return response.Response(serializer.dump(members))

    def create(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            phone_number = data.get('phone_number')
            address = data.get('address')
            membership_date = data.get('membership_date')
            membership_status = data.get('membership_status')
            self.member_component.create_member(name=name, email=email, phone_number=phone_number,
                                                address=address, membership_date=membership_date,membership_status=membership_status )
            return response.Response({'message': 'Member created successfully.'}, status=201)  # Assuming you have a to_dict method
        except json.JSONDecodeError:
            return response.Response({'error': 'Invalid JSON'}, status=400)

    
    def destroy(self, request, pk):
        self.member_component.delete_member(member_id=pk)
        return response.Response({'message': 'Member deleted successfully.'}, status=204)

    def update(self, request, pk):
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            phone_number = data.get('phone_number')
            address = data.get('address')
            membership_date = data.get('membership_date')
            membership_status = data.get('membership_status')
            self.member_component.update_member(pk, name, email, phone_number, address, membership_date, membership_status)

            return response.Response({'message': 'Member updated successfully.'}, status=204)  
        except json.JSONDecodeError:
            return response.Response({'error': 'Invalid JSON'}, status=400)


class BorrowingViewSet(viewsets.ModelViewSet):
    borrowing_component = BorrowingComponent()

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        borrowing = self.borrowing_component.get_borrow(borrowing_id=pk)
        serializer = BorrowingSchemaSerializer()
        return response.Response(serializer.dump(borrowing))

    
    def list(self, request, *args, **kwargs):
        borrowings_list = self.borrowing_component.get_borrowings()
        serializer = BorrowingSchemaSerializer(many = True)
        return response.Response(serializer.dump(borrowings_list))
    
    def create(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            member_id = data.get('member_id')
            book_id = data.get('book_id')
            borrow_date = data.get('borrow_date')
            self.borrowing_component.create_borrow(borrow_date=borrow_date, book_id=book_id, member_id=member_id)
            return response.Response({'message': 'borrowing created successfully.'}, status=201)
        except json.JSONDecodeError:
            return response.Response({'error': 'Invalid JSON'}, status=400)    
            
    def update(self, request, pk):
        try:
            data = json.loads(request.body)
            return_date = data.get('return_date')
            self.borrowing_component.update_borrow(borrowing_id=pk, return_date=return_date)
            return response.Response({'message': 'borrowing updated successfully.'}, status=204) 

        except json.JSONDecodeError:
            return response.Response({'error': 'Invalid borrow id'}, status=400)

class FineViewSet(viewsets.ModelViewSet):

    fine_component = FineComponent()
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        fine = self.fine_component.get_fine(fine_id=pk)
        serializer = FineSchemaSerializer()
        return response.Response(serializer.dump(fine))

    
    def list(self, request, *args, **kwargs):
        member_id = kwargs.get('member_pk')
        fines_list = self.fine_component.get_fine_list(member_id=member_id)
        serializer = FineSchemaSerializer(many = True)
        return response.Response(serializer.dump(fines_list))

    @action(detail=True, methods=['post'])     
    def edit(self, request,borrowing_pk=None, pk=None):
        data = json.loads(request.body)
        fine_id = pk
        fine_amount = data.get('fine_amount')
        fine_status = data.get('fine_status')
        self.fine_component.update_fine(fine_amount=fine_amount, fine_id=fine_id, fine_status=fine_status)
        return response.Response({'message': 'fine updae successfully.'}, status=204) 

