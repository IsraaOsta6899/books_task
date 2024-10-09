from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_fixed_length(value):
    if len(value) != 13:
        raise ValidationError('This field must be exactly 13 characters long.')

class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)


class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    published_year = models.IntegerField(null=False)
    genre = models.CharField(max_length=255, null=True)
    isbn = models.CharField(max_length=13, unique=True, validators=[validate_fixed_length])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def to_dict(self):
        return {
            "title": self.title,
            "published_year": self.published_year,
            "genre": self.genre,
            "isbn": self.isbn,
            "author": self.author,
        }

class Member(models.Model):

    class MembershipStatus(models.TextChoices):
        ACTIVE = 'AC', 'Active'
        INACTIVE = 'IN', 'Inactive'

    phone_regex = RegexValidator(
        regex=r'^\d{9,10}$',  # Allows 9 to 10 digits only
        message="Phone number must be entered as 9 to 10 digits (e.g., '1234567890')."
    )
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    phone_number = models.CharField(
        max_length=10,
        validators=[
            phone_regex
        ],
        blank=True,  # Set to False if you want to make it required
        null=True    # Set to False if you want to avoid NULL in the database
    )
    address = models.CharField(max_length=255, null=True)
    membership_date = models.DateTimeField(null=True)
    membership_status = models.CharField(
        max_length=2,
        choices=MembershipStatus.choices,
        default=MembershipStatus.ACTIVE,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)

class Borrowing(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, default="")
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    borrow_date = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True)
    return_date = models.DateTimeField(null=True)
    reated = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)

class fine(models.Model):

    class FineStatus(models.TextChoices):
        RETURNED = 'RE', 'RETURNED'
        NOTRETURNED = 'NOT RE', 'NOT RETURNED'

    borrow = models.ForeignKey(Borrowing, on_delete=models.CASCADE)
    fine_amount = models.IntegerField()
    fine_status = models.CharField(
        max_length = 7,
        choices = FineStatus.choices,
        default = FineStatus.NOTRETURNED,
    )
    reated = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)