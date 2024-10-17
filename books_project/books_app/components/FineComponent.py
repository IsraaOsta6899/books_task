from datetime import datetime
from books_app.Reposetories.FineRepository import FineRepository
from rest_framework.exceptions import PermissionDenied, NotFound

class FineComponent:

    def __init__(self):
        self.fine_repository = FineRepository()

    def create_fine(self, borrow_instance):
        if borrow_instance.return_date > borrow_instance.due_date:
            print(type(borrow_instance.return_date))
            # we will add fine 
            return_date_str = borrow_instance.return_date
            due_date_str = borrow_instance.due_date 

            number_of_late = (return_date_str - due_date_str).days
            fine_amount = number_of_late * 2
            self.fine_repository.create_fine(borrow=borrow_instance, fine_amount=fine_amount ,fine_status="RETURNED")

    def update_fine(self, fine_id, fine_amount, fine_status):
        fine = self.fine_repository.get_fine(fine_id)
        if fine is not None:
            self.fine_repository.update_fine(fine_id, fine_amount, fine_status)
        else:
            raise NotFound("fine not found")

    def get_fine(self, id):
        fine = self.fine_repository.get_fine(id)
        if fine is not None:
            return fine
        else:
            raise NotFound("fine not found")

    
    def get_fine_list(self, member_id):
        member_fines_list = self.fine_repository.get_member_fines(member_id)
        return member_fines_list