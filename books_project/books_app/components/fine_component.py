from typing import List

from books_app.models import Borrowing, Fine
from books_app.repositories.fine_repository import FineRepository
from rest_framework.exceptions import NotFound

class FineComponent:
    @staticmethod
    def create_fine(borrow_instance: Borrowing):
        if borrow_instance.return_date > borrow_instance.due_date:
            return_date_str = borrow_instance.return_date
            due_date_str = borrow_instance.due_date 

            number_of_late = (return_date_str - due_date_str).days
            fine_amount = number_of_late * 2
            FineRepository.create_fine(borrow=borrow_instance, fine_amount=fine_amount ,fine_status="RETURNED")

    @staticmethod
    def update_fine(fine_id: int, fine_amount: int, fine_status: str):
        fine_data = {
        'fine_amount': fine_amount,
        'fine_status': fine_status,
        }
        fine = FineRepository.get_fine(fine_id)
        if fine is None:
            raise NotFound("fine not found")
        FineRepository.update_fine(fine_id=fine_id, data=fine_data)

    @staticmethod
    def get_fine(fine_id: int):
        fine = FineRepository.get_fine(fine_id=fine_id)
        if fine is None:
             raise NotFound("fine not found")
        return fine

    @staticmethod
    def get_member_fines(member_id: int) -> List[Fine]:
        member_fines = FineRepository.get_member_fines(member_id=member_id)
        return member_fines