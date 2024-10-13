from books_app.Reposetories.FineRepository import FineRepository
from books_app.models import fine
class FineComponent:

    def __init__(self):
        self.fine_repository = FineRepository()

    def create_fine(self, borrow, fine_amount, fine_status):
        self.fine_repository.create_fine(borrow, fine_amount, fine_status)

    def update_fine(self, borrow_id, fine_id, fine_amount, fine_status):
        # TODO: check if fine exists and it is not paid yet
        self.fine_repository.update_fine(borrow_id, fine_id, fine_amount, fine_status)

    def get_fine(self, pk):
        book = self.fine_repository.get_fine(pk)
        return book
    
    def get_fine_list(self, member_id):
        objects = self.fine_repository.get_list_of_fines_for_member(member_id)
        return objects


        
