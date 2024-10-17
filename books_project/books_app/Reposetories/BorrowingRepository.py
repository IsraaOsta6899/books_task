from books_app.models import Member, Book, Borrowing, session
from datetime import datetime, timedelta
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from rest_framework.exceptions import PermissionDenied, NotFound

class BorrowingRepository:

    def __init__(self):
        print("this is BorrowingRepository class")

    def create_borrowing(self, borrow_date, book, member):
        borrow = Borrowing()
        date_obj = datetime.strptime(borrow_date, '%Y-%m-%d').date()  # Converts string to date object
        borrow.borrow_date = date_obj
        borrow.due_date = date_obj + timedelta(days=7)
        borrow.book = book
        borrow.member = member
        session.add(borrow)
        session.commit()

    def update_borrow(self, id, return_date):

        try:
            borrow = session.query(Borrowing).filter(Borrowing.id == id).one_or_none()
            date_obj = datetime.strptime(return_date, '%Y-%m-%d').date()  # Converts string to date object
            borrow.return_date = date_obj
            session.commit()
        except MultipleResultsFound:
            raise MultipleResultsFound("there are more that one borrow")
        
    def get_borrow(self, id):
        try:
            borrow = session.query(Borrowing).filter(Borrowing.id == id).one_or_none()
            return borrow
        except MultipleResultsFound:
            raise MultipleResultsFound("there are more that one borrow")


    def get_borrowings(self):
        borrowings_list = session.query(Borrowing).all()
        return borrowings_list
