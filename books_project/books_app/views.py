from rest_framework import response, status, viewsets
import json
from books_app.components.author_component import AuthorComponent
from books_app.components.book_component import BookComponent
from books_app.components.member_component import MemberComponent
from books_app.components.borrowing_component import BorrowingComponent
from books_app.components.fine_component import FineComponent
from .serializers import BookSchemaSerializer, AuthorSchemaSerializer, MemberSchemaSerializer, FineSchemaSerializer, \
    BorrowingSchemaSerializer
from rest_framework.decorators import action


class BookViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        books = BookComponent.get_books()  # This should return a list
        try:
            serializer = BookSchemaSerializer(many=True)
            return response.Response(serializer.dump(books))
        except Exception as e:
            print("Serializer error:", e)  # Print any serializer errors for debugging
            return response.Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, pk=None):
        book = BookComponent.get_book(book_id=pk)
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
            BookComponent.create_book(title=title, published_year=published_year, genr=genre, isbn=isbn,
                                            author_id=author_id)
            return response.Response({'message': 'Book created successfully.'},
                                     status=201)
        except json.JSONDecodeError:
            return response.Response({'error': 'Invalid JSON'}, status=400)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        BookComponent.delete_book(book_id=pk)
        return response.Response({'message': 'Book deleted successfully.'}, status=204)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        data = json.loads(request.body)
        title = data.get('title')
        published_year = data.get('published_year')
        genre = data.get('genre')
        isbn = data.get('isbn')
        BookComponent.update_book(book_id=pk, title=title, published_year=published_year, genr=genre, isbn=isbn)
        return response.Response({'message': 'Book updated successfully.'}, status=204)


class AuthorViewSet(viewsets.ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        author = AuthorComponent.get_author(author_id=pk)
        serializer = AuthorSchemaSerializer()
        return response.Response(serializer.dump(author))

    def list(self, request, *args, **kwargs):
        authors = AuthorComponent.get_authors()
        serializer = AuthorSchemaSerializer(many=True)
        return response.Response(serializer.dump(authors))

    def create(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)

            name = data.get('name')
            birth_date = data.get('birth_date')
            nationality = data.get('nationality')
            AuthorComponent.create_author(name=name, birth_date=birth_date, nationality=nationality)
            return response.Response({'message': 'Author created successfully.'},
                                     status=201)  # Assuming you have a to_dict method
        except json.JSONDecodeError:
            return response.Response({'error': 'Invalid JSON'}, status=400)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        AuthorComponent.delete_author(author_id=pk)
        return response.Response({'message': 'Author deleted successfully.'}, status=204)


class MemberViewSet(viewsets.ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        member = MemberComponent.get_member(member_id=pk)
        serializer = MemberSchemaSerializer()
        return response.Response(serializer.dump(member))

    def list(self, request, *args, **kwargs):
        members = MemberComponent.get_members()
        serializer = MemberSchemaSerializer(many=True)
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
            MemberComponent.create_member(name=name, email=email, phone_number=phone_number,
                                                address=address, membership_date=membership_date,
                                                membership_status=membership_status)
            return response.Response({'message': 'Member created successfully.'},
                                     status=201)  # Assuming you have a to_dict method
        except json.JSONDecodeError:
            return response.Response({'error': 'Invalid JSON'}, status=400)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        MemberComponent.delete_member(member_id=pk)
        return response.Response({'message': 'Member deleted successfully.'}, status=204)

    def update(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            phone_number = data.get('phone_number')
            address = data.get('address')
            membership_date = data.get('membership_date')
            membership_status = data.get('membership_status')
            MemberComponent.update_member(member_id=pk, name=name, email=email, phone_number=phone_number,
                                          membership_date=membership_date, membership_status=membership_status, address=address)

            return response.Response({'message': 'Member updated successfully.'}, status=204)
        except json.JSONDecodeError:
            return response.Response({'error': 'Invalid JSON'}, status=400)

class BorrowingViewSet(viewsets.ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        borrowing = BorrowingComponent.get_borrow(borrowing_id=pk)
        serializer = BorrowingSchemaSerializer()
        return response.Response(serializer.dump(borrowing))

    def list(self, request, *args, **kwargs):
        borrowings_list = BorrowingComponent.get_borrowings()
        serializer = BorrowingSchemaSerializer(many=True)
        return response.Response(serializer.dump(borrowings_list))

    def create(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            member_id = data.get('member_id')
            book_id = data.get('book_id')
            borrow_date = data.get('borrow_date')
            BorrowingComponent.create_borrow(borrow_date=borrow_date, book_id=book_id, member_id=member_id)
            return response.Response({'message': 'borrowing created successfully.'}, status=201)
        except json.JSONDecodeError:
            return response.Response({'error': 'Invalid JSON'}, status=400)

    def update(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            data = json.loads(request.body)
            return_date = data.get('return_date')
            BorrowingComponent.update_borrow(borrowing_id=pk, return_date=return_date)
            return response.Response({'message': 'borrowing updated successfully.'}, status=204)

        except json.JSONDecodeError:
            return response.Response({'error': 'Invalid borrow id'}, status=400)


class FineViewSet(viewsets.ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        fine = FineComponent.get_fine(fine_id=pk)
        serializer = FineSchemaSerializer()
        return response.Response(serializer.dump(fine))

    def list(self, request, *args, **kwargs):
        member_id = kwargs.get('member_pk')
        fines_list = FineComponent.get_member_fines(member_id=member_id)
        serializer = FineSchemaSerializer(many=True)
        return response.Response(serializer.dump(fines_list))

    @action(detail=True, methods=['post'])
    def edit(self, request, borrowing_pk=None, pk=None):
        data = json.loads(request.body)
        fine_id = pk
        fine_amount = data.get('fine_amount')
        fine_status = data.get('fine_status')
        FineComponent.update_fine(fine_amount=fine_amount, fine_id=fine_id, fine_status=fine_status)
        return response.Response({'message': 'fine updated successfully.'}, status=204)
