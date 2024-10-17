from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemyAutoSchemaOpts,SQLAlchemySchema
from books_app.models import Author, Book, Member, Borrowing, Fine, MembershipStatus, FineStatus
from marshmallow import Schema, ValidationError, fields
from rest_framework import serializers

class BaseModelSchemaOpts(SQLAlchemyAutoSchemaOpts):
    def __init__(self, meta, *args, **kwargs):
        super(BaseModelSchemaOpts, self).__init__(meta, *args, **kwargs)
        self.include_fk = getattr(meta, 'include_fk', True)
        self.include_relationships = getattr(meta, "include_relationships", True)

class BaseModelSchema(SQLAlchemyAutoSchema):
    OPTIONS_CLASS = BaseModelSchemaOpts

class AuthorSchemaSerializer(BaseModelSchema):
    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'birth_date',
            'nationality',
        )


class BookSchemaSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True  # This is important for deserialization
        # Specify the fields you want to serialize
        fields = (
            'id',
            'title',
            'published_year',
            'genre',
            'isbn',
            'author_id',
            'created',
            'updated'
        )
class MembershipStatusField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        # Convert enum to its value for JSON serialization
        if isinstance(value, MembershipStatus):
            return value.value
        return value

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return MembershipStatus(value)
        except ValueError:
            raise ValidationError("Invalid membership status")
            
class MemberSchemaSerializer(SQLAlchemyAutoSchema):   
    membership_status = MembershipStatusField()
    class Meta:
        model = Member
        fields = (
            'id',
            'name',
            'email',
            'phone_number',
            'address',
            'membership_date',
            'membership_status',
        )

class BorrowingSchemaSerializer(SQLAlchemyAutoSchema):

    class Meta:
        model = Borrowing
        fields = (
            'id',
            'borrow_date',
            'due_date',
            'return_date',
            'book_id',
            'member_id',
        )

class FineStatusField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        # Convert enum to its value for JSON serialization
        if isinstance(value, FineStatus):
            return value.value
        return value

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return FineStatus(value)
        except ValueError:
            raise ValidationError("Invalid membership status")
class FineSchemaSerializer(SQLAlchemyAutoSchema):
    borrow = fields.Nested(BorrowingSchemaSerializer)  # Include borrowing details in fine
    fine_status = FineStatusField()
    class Meta:
        model = Fine
        fields = (
            'id',
            'borrow_id',
            'fine_status',
            'fine_amount',
            'borrow'
        )

