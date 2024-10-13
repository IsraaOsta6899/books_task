from datetime import datetime
from books_app.Reposetories.BorrowingRepository import BorrowingRepository
from books_app.Reposetories.FineRepository import FineRepository

from books_app.models import Borrowing
class BorrowingComponent:

    def __init__(self):
        self.borrowing_repository = BorrowingRepository()
        self.fine_repository = FineRepository()

    def create_borrow(self, book_pk, member_pk, borrow_date, due_date):
        
        self.borrowing_repository.create_borrowing(book_pk, member_pk, borrow_date, due_date)

    def update_borrow(self, pk, book_pk, member_pk, borrow_date, due_date, return_date):
        self.borrowing_repository.update_borrow(pk, book_pk, member_pk, borrow_date, due_date, return_date)
        borrow_instance = self.get_borrow(pk=pk)
        if borrow_instance.return_date > borrow_instance.due_date:
            # TODO: move to fines component
            # we will add fine 
            return_date_str = borrow_instance.return_date
            due_date_str = borrow_instance.due_date 

            number_of_late = (datetime.strptime(return_date_str, "%Y-%m-%d") - datetime.strptime(due_date_str, "%Y-%m-%d")).days
            fine_amount = number_of_late * 2
            self.fine_repository.create_fine(borrow=borrow_instance, fine_amount=fine_amount ,fine_status="RETURNED")

    def get_borrow(self, pk):
        book = self.borrowing_repository.get_borrow(pk)
        return book
    
    def get_borrowing_list(self):
        objects = self.borrowing_repository.get_list_of_borrowing()
        return objects

        
