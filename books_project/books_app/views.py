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


# Create your views here.
class BookView(View):

    def get(self, request, pk = None):
        if pk is None:
            # Return all objects if pk is None
            objects = Book.objects.all()
            data = list(objects.values())  # Convert queryset to a list of dictionaries
            print(data)
            return JsonResponse(data, safe=False)  # Return JSON response
        else:
            try:
                obj = Book.objects.get(pk=pk)
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
            author = Author.objects.get(pk=author_id)


            book = Book()
            book.title = title
            book.published_year = published_year
            book.genre = genre
            book.isbn = isbn
            book.author = author
            book.save()
            return JsonResponse({'message': 'Object created successfully.'}, status=201)  # Assuming you have a to_dict method


        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    def delete(self, request, pk):
        if request.method == 'DELETE':
            try:
                book_instance = Book.objects.get(pk = pk)
                book_instance.delete()
                return JsonResponse({'message': 'Object deleted successfully.'}, status=204)
            except Book.DoesNotExist:
                return JsonResponse({'error': 'Invalid book id'}, status=400)

    def put(self, request, pk):
        if request.method == 'PUT':
            try:
                book_instance = Book.objects.get(pk = pk)
                data = json.loads(request.body)
                book_instance.title = data.get('title')
                book_instance.published_year = data.get('published_year')
                book_instance.genre = data.get('genre')
                book_instance.isbn = data.get('isbn')
                book_instance.save()
                return JsonResponse({'message': 'Object updae successfully.'}, status=204)
            except Book.DoesNotExist:
                return JsonResponse({'error': 'Invalid book id'}, status=400)

# Create your views here.
class AuthorView(View):

    def get(self, request, pk = None):
        if pk is None:
            # Return all objects if pk is None
            objects = Author.objects.all()
            data = list(objects.values())  # Convert queryset to a list of dictionaries
            print(data)
            return JsonResponse(data, safe=False)  # Return JSON response
        else:
            try:
                obj = Author.objects.get(pk=pk)
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
            author = Author()
            author.name = name
            author.birth_date = birth_date
            author.nationality= nationality
            author.save()
            return JsonResponse({'message': 'Object created successfully.'}, status=201)  # Assuming you have a to_dict method

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    def delete(self, request, pk):
        if request.method == 'DELETE':
            try:
                author_instance = Author.objects.get(pk = pk)
                author_instance.delete()
                return JsonResponse({'message': 'Object deleted successfully.'}, status=204)
            except Author.DoesNotExist:
                return JsonResponse({'error': 'Invalid author id'}, status=400)


    def put(self, request, pk):
        if request.method == 'PUT':
            try:
                author_instance = Author.objects.get(pk = pk)
                data = json.loads(request.body)
                author_instance.name = data.get('name')
                author_instance.birth_date = data.get('birth_date')
                author_instance.nationality = data.get('nationality')
                author_instance.save()
                return JsonResponse({'message': 'Object updae successfully.'}, status=204)
            except Author.DoesNotExist:
                return JsonResponse({'error': 'Invalid author id'}, status=400)

class MemberView(View):

    def get(self, request, pk = None):
        if pk is None:
            # Return all objects if pk is None
            objects = Member.objects.all()
            data = list(objects.values())  # Convert queryset to a list of dictionaries
            print(data)
            return JsonResponse(data, safe=False)  # Return JSON response
        else:
            obj = Member.objects.get(pk=pk)
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
            member = Member()
            member.name = name
            member.email = email
            member.phone_number = phone_number
            member.address = address
            member.membership_date = membership_date
            member.membership_status = membership_status

            member.save()
            return JsonResponse({'message': 'Object created successfully.'}, status=201)  # Assuming you have a to_dict method

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    def delete(self, request, pk):
        if request.method == 'DELETE':
            member_instance = Member.objects.get(pk = pk)
            member_instance.delete()
            return JsonResponse({'message': 'Object deleted successfully.'}, status=204)


    def put(self, request, pk):
        if request.method == 'PUT':
            try:
                member_instance = Member.objects.get(pk = pk)
                data = json.loads(request.body)
                member_instance.name = data.get('name')
                member_instance.email = data.get('email')
                member_instance.phone_number = data.get('phone_number')
                member_instance.address = data.get('address')
                member_instance.membership_date = data.get('membership_date')
                member_instance.membership_status = data.get('membership_status')
                member_instance.save()
                return JsonResponse({'message': 'Object updae successfully.'}, status=204)
            except Member.DoesNotExist:
                return JsonResponse({'error': 'Invalid member id'}, status=400)


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


class BorrowingView(View):

    def post(self, request, member_pk, book_pk):
        if request.method == "POST":
            data = json.loads(request.body)
            list_of_borrowing = list(Borrowing.objects.filter(book__id = book_pk))
            can_borrow = True
            for item in list_of_borrowing:
                if item.return_date > data.get('borrow_date') or item.return_date is None:
                    can_borrow = False
                    break
            if can_borrow:
                member = Member.objects.get(pk = member_pk)
                book = Book.objects.get(pk = book_pk)
                borrow_instance = Borrowing()
                borrow_instance.book = book
                borrow_instance.member = member
                borrow_instance.due_date = data.get('due_date')
                borrow_instance.borrow_date = data.get('borrow_date')
                borrow_instance.save()
            else:
                return JsonResponse({'message': 'Book already borrowed'}, status=401)
            
    def get(self, request, pk = None):
        if pk is None:
            # Return all objects if pk is None
            objects = Borrowing.objects.all()
            data = list(objects.values())  # Convert queryset to a list of dictionaries
            print(data)
            return JsonResponse(data, safe=False)  # Return JSON response
        else:
            try:
                obj = Borrowing.objects.get(pk=pk)
                serializer = BorrowingSerializer(obj)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            except Borrowing.DoesNotExist:
                return JsonResponse({'error': 'Invalid borrow id'}, status=400)

    
    def put(self, request, pk):
        if request.method == 'PUT':
            try:
                borrow_instance = Borrowing.objects.get(pk = pk)
                data = json.loads(request.body)
                borrow_instance.due_date = data.get('due_date')
                borrow_instance.return_date = data.get('return_date')
                borrow_instance.borrow_date = data.get('borrow_date')
                # member
                member_dict = data.get('member')
                member_id = member_dict.get("id")

                member = Member.objects.get(pk = member_id)

                #book
                book_dict = data.get('member')
                book_id = book_dict.get("id")
                book = Book.objects.get(pk = book_id)

                borrow_instance.member = member
                borrow_instance.book = book
                borrow_instance.save()
            except Borrowing.DoesNotExist:
                return JsonResponse({'error': 'Invalid borrow id'}, status=400)

class FineView(View):
    def get(self, request, pk = None, member_id = None):
        if member_id is not None:
            user_fines = fine.objects.filter(borrow__member__id=member_id).values()  # Use .values() to get dicts
            return JsonResponse(list(user_fines), safe=False)
        elif pk is None:
            # Return all objects if pk is None
            objects = fine.objects.all()
            data = list(objects.values())  # Convert queryset to a list of dictionaries
            print(data)
            return JsonResponse(data, safe=False)  # Return JSON response
        else:
            try:
                obj = fine.objects.get(pk=pk)
                serializer = FineSerializer(obj)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            except fine.DoesNotExist:
                return JsonResponse({'error': 'Invalid fine id'}, status=400)
    
    def dispatch(self, request, *args, **kwargs):
        # Call the parent dispatch method
        return super().dispatch(request, *args, **kwargs)


@receiver(post_save, sender=Borrowing)
def update_fines_according_to_borrowing(sender, instance, created, **kwargs):
    if instance.return_date > instance.due_date:
        # we will add fine 
        return_date_str = instance.return_date
        due_date_str = instance.due_date 

        number_of_late = (datetime.strptime(return_date_str, "%Y-%m-%d") - datetime.strptime(due_date_str, "%Y-%m-%d")).days
        print(number_of_late)
        fine_amount = number_of_late * 2
        fine_instance = fine()
        fine_instance.borrow = instance
        fine_instance.fine_amount = fine_amount
        fine_instance.fine_status = "RETURNED"
        fine_instance.save()