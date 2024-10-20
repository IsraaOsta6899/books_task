from books_app.models import Member, Book, Borrowing, session
from datetime import datetime, timedelta
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from rest_framework.exceptions import PermissionDenied, NotFound

class BorrowingRepository:

    def __init__(self):
        print("this is BorrowingRepository class")

    @staticmethod
    def create_borrowing(self, borrow_date, due_date, book, member, commit=True):
        borrow = Borrowing(borrow_date=borrow_date, due_date=due_date,book=book, member=member)
        session.add(borrow)
        if commit:
            session.commit()
        else:
            session.flush()

    @staticmethod
    def update_borrow(self, borrowing_id, data, commit=True):
        borrow = session.query(Borrowing).\
            filter(Borrowing.id == borrowing_id).\
            update(data, synchronize_session=False)
        if commit:
            session.commit()
        else:
            session.flush()

    @staticmethod
    def get_borrow(self, borrowing_id):
        borrow = session.query(Borrowing).filter(Borrowing.id == borrowing_id).one_or_none()
        return borrow

    @staticmethod
    def get_borrowings(self):
        borrowings = session.query(Borrowing).all()
        return borrowings
