from datetime import datetime
from books_app.repositories.fine_repository import FineRepository
from rest_framework.exceptions import NotFound

class FineComponent:

    def create_fine(self, borrow_instance):
        if borrow_instance.return_date > borrow_instance.due_date:
            return_date_str = borrow_instance.return_date
            due_date_str = borrow_instance.due_date 

            number_of_late = (return_date_str - due_date_str).days
            fine_amount = number_of_late * 2
            FineRepository.create_fine(borrow=borrow_instance, fine_amount=fine_amount ,fine_status="RETURNED")

    def update_fine(self, fine_id: int, fine_amount: int, fine_status: str):
        fine_data = {
        'fine_amount': fine_amount,
        'fine_status': fine_status,
        }
        fine = FineRepository.get_fine(fine_id)
        if fine is None:
            raise NotFound("fine not found")
        FineRepository.update_fine(fine_id=fine_id, data=fine_data)

    def get_fine(self, fine_id: int):
        fine = FineRepository.get_fine(fine_id=fine_id)
        if fine is None:
             raise NotFound("fine not found")
        return fine
    
    def get_fine_list(self, member_id: int):
        member_fines_list = FineRepository.get_member_fines(member_id=member_id)
        return member_fines_list