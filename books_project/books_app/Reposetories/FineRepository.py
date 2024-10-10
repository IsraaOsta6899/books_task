from books_app.models import fine, Borrowing

class FineRepository:

    def __init__(self):
        print("this is FineRepository class")

    def create_fine(self, borrow, fine_amount, fine_status):
        fine_instance = fine()
        fine_instance.borrow = borrow
        fine_instance.fine_amount = fine_amount
        fine_instance.fine_status = fine_status

    def update_fine(self, borrow_id, fine_id, fine_amount, fine_status):
        fine_instance = fine.objects.get(pk = fine_id)
        fine_instance.fine_status = fine_status
        fine_instance.fine_amount = fine_amount
        fine_instance.borrow = Borrowing.objects.get(pk = borrow_id)
        fine_instance.save()

    def get_fine(self, pk):
         obj = fine.objects.get(pk = pk)
         return obj

    def get_list_of_fines_for_member(self, member_id):
        objects = fine.objects.filter(borrow__member__id=member_id).values()
        return objects
