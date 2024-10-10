from django.shortcuts import render
from django.views import View
from books_app.models import Book, Author, Member, Borrowing, fine
from rest_framework import status
from django.http import JsonResponse
from django.middleware.csrf import get_token
import json
from books_app.serializers import BookSerializer, AuthorSerializer, MemberSerializer, BorrowingSerializer, FineSerializer
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from books_app.components.AuthorComponent import AuthorComponent
from books_app.components.BookComponent import BookComponent
from books_app.components.MemberComponent import MemberComponent
from books_app.components.BorrowingComponent import BorrowingComponent
from books_app.components.FineComponent import FineComponent



# Create your views here.
class BookView(View):

    book_component = BookComponent()

    def get(self, request, pk = None):
        if pk is None:
            # Return all objects if pk is None
            objects = self.book_component.get_books_list()
            data = list(objects.values())  # Convert queryset to a list of dictionaries
            return JsonResponse(data, safe=False)  # Return JSON response
        else:
            try:
                obj = self.book_component.get_book(pk)
                serializer = BookSerializer(obj)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            except Book.DoesNotExist:
                return JsonResponse({'error': 'Invalid book id'}, status=400)


    def post(self, request):
        
        try:
            data = json.loads(request.body)
            title = data.get('title')
            published_year = data.get('published_year')
            genre = data.get('genre')
            isbn = data.get('isbn')
            author_dict = data.get('author')
            author_id = author_dict.get('id')
            self.book_component.create_book(title=title, published_year=published_year, genr=genre, isbn=isbn, author_id=author_id)
            return JsonResponse({'message': 'Object created successfully.'}, status=201)  # Assuming you have a to_dict method


        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    def delete(self, request, pk):
        if request.method == 'DELETE':
            try:
                self.book_component.delete_book(pk = pk)
                return JsonResponse({'message': 'Object deleted successfully.'}, status=204)
            except Book.DoesNotExist:
                return JsonResponse({'error': 'Invalid book id'}, status=400)

    def put(self, request, pk):
        if request.method == 'PUT':
            try:
                book_instance = Book.objects.get(pk = pk)
                data = json.loads(request.body)
                title = data.get('title')
                published_year = data.get('published_year')
                genre = data.get('genre')
                isbn = data.get('isbn')

                self.book_component.update_book(pk=pk, title=title, published_year=published_year, genr=genre, isbn=isbn)

                return JsonResponse({'message': 'Object updae successfully.'}, status=204)
            except Book.DoesNotExist:
                return JsonResponse({'error': 'Invalid book id'}, status=400)

# Create your views here.
class AuthorView(View):

    author_component = AuthorComponent()

    def get(self, request, pk = None):
        if pk is None:
            # Return all objects if pk is None
            objects = self.author_component.get_authors_list()
            data = list(objects.values())  # Convert queryset to a list of dictionaries
            
            return JsonResponse(data, safe=False)  # Return JSON response
        else:
            try:
                obj = self.author_component.get_author(pk)
                serializer = AuthorSerializer(obj)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            except Author.DoesNotExist:
                return JsonResponse({'error': 'Invalid author id'}, status=400)


    def post(self, request, *args, **kwargs):
        
        try:
            data = json.loads(request.body)

            name = data.get('name')
            birth_date = data.get('birth_date')
            nationality = data.get('nationality')

            self.author_component.create_author(name, birth_date, nationality)

            return JsonResponse({'message': 'Object created successfully.'}, status=201)  # Assuming you have a to_dict method

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    def delete(self, request, pk):
        if request.method == 'DELETE':
            try:
                self.author_component.delete_author(pk)
                return JsonResponse({'message': 'Object deleted successfully.'}, status=204)
            except Author.DoesNotExist:
                return JsonResponse({'error': 'Invalid author id'}, status=400)
            


    def put(self, request, pk):
        if request.method == 'PUT':
            try:
                data = json.loads(request.body)
                name = data.get('name')
                birth_date = data.get('birth_date')
                nationality = data.get('nationality')
                self.author_component.update_author(pk, name=name, birth_date=birth_date, nationality=nationality)
                return JsonResponse({'message': 'Object updae successfully.'}, status=204)
            except Author.DoesNotExist:
                return JsonResponse({'error': 'Invalid author id'}, status=400)

class MemberView(View):

    member_component = MemberComponent()
    def get(self, request, pk = None):
        if pk is None:
            # Return all objects if pk is None
            objects = self.member_component.get_members_list()
            data = list(objects.values())  # Convert queryset to a list of dictionaries
            return JsonResponse(data, safe=False)  # Return JSON response
        else:
            obj = self.member_component.get_member(pk)
            serializer = MemberSerializer(obj)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        
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
            return JsonResponse({'message': 'Object created successfully.'}, status=201)  # Assuming you have a to_dict method

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    def delete(self, request, pk):
        if request.method == 'DELETE':
            self.member_component.delete_member(pk=pk)
            return JsonResponse({'message': 'Object deleted successfully.'}, status=204)


    def put(self, request, pk):
        if request.method == 'PUT':
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            phone_number = data.get('phone_number')
            address = data.get('address')
            membership_date = data.get('membership_date')
            membership_status = data.get('membership_status')
            
            self.member_component.update_member(pk, name, email, phone_number, address, membership_date, membership_status)

            return JsonResponse({'message': 'Object updae successfully.'}, status=204)



def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


class BorrowingView(View):
    borrowing_component = BorrowingComponent()
    def post(self, request):
        data = json.loads(request.body)
        member_pk = data.get('member_id')
        book_pk = data.get('book_id')
        due_date = data.get('due_date')
        borrow_date = data.get('borrow_date')
        self.borrowing_component.create_borrow(book_pk, member_pk, borrow_date, due_date)
        return JsonResponse({'message': 'Object created successfully.'}, status=201)

        
            
    def get(self, request, pk = None):
        if pk is None:
            # Return all objects if pk is None
            objects = self.borrowing_component.get_borrowing_list()
            data = list(objects.values())  # Convert queryset to a list of dictionaries
            print(data)
            return JsonResponse(data, safe=False)  # Return JSON response
        else:
            try:
                obj = self.borrowing_component.get_borrow(pk=pk)
                serializer = BorrowingSerializer(obj)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            except Borrowing.DoesNotExist:
                return JsonResponse({'error': 'Invalid borrow id'}, status=400)

    
    def put(self, request, pk):
        if request.method == 'PUT':
            try:
                data = json.loads(request.body)
                due_date = data.get('due_date')
                return_date = data.get('return_date')
                borrow_date = data.get('borrow_date')
                #member
                member_dict = data.get('member')
                member_id = member_dict.get("id")

                #book
                book_dict = data.get('member')
                book_id = book_dict.get("id")

                self.borrowing_component.update_borrow(pk, book_id, member_id, borrow_date, due_date, return_date)
                return JsonResponse({'message': 'Object updae successfully.'}, status=204)

            except Borrowing.DoesNotExist:
                return JsonResponse({'error': 'Invalid borrow id'}, status=400)

class FineView(View):

    fine_component = FineComponent()

    def get(self, request, pk = None, member_id = None):
        if member_id is not None:
            user_fines = self.fine_component.get_fine_list(member_id)
            return JsonResponse(list(user_fines), safe=False)
        else:
            try:
                obj = self.fine_component.get_fine(pk=pk)
                serializer = FineSerializer(obj)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            except fine.DoesNotExist:
                return JsonResponse({'error': 'Invalid fine id'}, status=400)
            
    def put(self, request, borrow_id, fine_id):
        data = json.loads(request.body)
        fine_amount = data.get('fine_amount')
        fine_status = data.get('fine_status')
        if request.method == 'PUT':
            self.fine_component.update_fine(borrow_id, fine_id, fine_amount, fine_status)
    
    def dispatch(self, request, *args, **kwargs):
        # Call the parent dispatch method
        return super().dispatch(request, *args, **kwargs)
