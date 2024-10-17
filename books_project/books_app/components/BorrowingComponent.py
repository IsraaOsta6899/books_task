from datetime import datetime
from books_app.Reposetories.BorrowingRepository import BorrowingRepository
from books_app.Reposetories.FineRepository import FineRepository
from books_app.components.BookComponent import BookComponent
from books_app.components.MemberComponent import MemberComponent
from books_app.components.FineComponent import FineComponent
from rest_framework.exceptions import PermissionDenied, NotFound

class BorrowingComponent:

    def __init__(self):
        self.borrowing_repository = BorrowingRepository()
        self.fine_component = FineComponent()
        self.book_component = BookComponent()
        self.member_component = MemberComponent()

    def create_borrow(self, borrow_date, book_id, member_id):
        try:
            book = self.book_component.get_book(book_id)
            member = self.member_component.get_member(member_id)
            self.borrowing_repository.create_borrowing(borrow_date, book, member)
        except:
            raise Exception("")

    def update_borrow(self, id, return_date):
        borrow = self.borrowing_repository.get_borrow(id=id)
        if borrow is None:
            raise NotFound("")
        else:
            self.borrowing_repository.update_borrow(id, return_date)
            borrow_instance = self.get_borrow(id)
            self.fine_component.create_fine(borrow_instance)

    def get_borrow(self, id):
        borrowing = self.borrowing_repository.get_borrow(id)
        if borrowing is not None:
            return borrowing
        else:
            raise NotFound("borrowing not found")
    
    def get_borrowing_list(self):
        borrowings_list = self.borrowing_repository.get_borrowings()
        return borrowings_list