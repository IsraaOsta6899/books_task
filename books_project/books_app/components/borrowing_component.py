from datetime import datetime, timedelta
from books_app.repositories.borrowing_repository import BorrowingRepository
from books_app.repositories.book_repository import BookRepository
from books_app.repositories.member_repository import MemberRepository
from books_app.components.fine_component import FineComponent
from rest_framework.exceptions import NotFound

from books_project.constants import DateTimeFormat

class BorrowingComponent:

    def __init__(self):
        self.fine_component = FineComponent()

    def create_borrow(self, borrow_date: str, book_id: int, member_id: int):
        book = BookRepository.get_book(book_id=book_id)
        member = MemberRepository.get_member(member_id=member_id)
        if not book:
            raise NotFound("book not found")
        elif not member:
            raise NotFound("member not found")
        borrowing_date = datetime.strptime(borrow_date, DateTimeFormat.ISO_DATE_FORMAT).date()
        borrowing_due_date = borrowing_date + timedelta(days=7)
        BorrowingRepository.create_borrowing(borrow_date=borrowing_date, due_date=borrowing_due_date, book=book, member=member, commit=True)

    def update_borrow(self, borrowing_id: int, return_date: str):
        date = datetime.strptime(return_date, DateTimeFormat.ISO_DATE_FORMAT).date()
        borrow_data = {
        'id': borrowing_id,
        'return_date': date,
        }
        borrow = BorrowingRepository.get_borrow(id=borrowing_id)
        if borrow is None:
            raise NotFound("borrow not found")
        BorrowingRepository.update_borrow(borrowing_id=borrowing_id, data=borrow_data)
        borrow_instance = self.get_borrow(borrowing_id=borrowing_id)
        self.fine_component.create_fine(borrow_instance=borrow_instance)

    def get_borrow(self, borrowing_id: int):
        borrowing = BorrowingRepository.get_borrow(borrowing_id=borrowing_id)
        if borrowing is None:
            raise NotFound("borrowing not found")
        return borrowing
    
    def get_borrowings(self):
        borrowings = BorrowingRepository.get_borrowings()
        return borrowings