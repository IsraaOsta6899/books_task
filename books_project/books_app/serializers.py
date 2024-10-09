from rest_framework import serializers
from .models import Book, Author, Member, Borrowing, fine

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields ='__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields ='__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields ='__all__'
class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields ='__all__'
class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = fine
        fields ='__all__'