from books_app.models import Member, Book, Borrowing

class BorrowingRepository:

    def __init__(self):
        print("this is BorrowingRepository class")

    def create_borrowing(self, book_pk, member_pk, borrow_date, due_date):
        list_of_borrowing = list(Borrowing.objects.filter(book__id = book_pk))
        can_borrow = True
        for item in list_of_borrowing:
            if item.return_date is None:
                can_borrow = False
                break
            
        if can_borrow:
            borrow = Borrowing()
            borrow.due_date = due_date
            borrow.borrow_date = borrow_date
            book = Book.objects.get(pk = book_pk)
            member = Member.objects.get(pk=member_pk)
            borrow.book = book
            borrow.member = member
            borrow.save()

    def update_borrow(self, pk, book_pk, member_pk, borrow_date, due_date, return_date):
        borrow = Borrowing.objects.get(pk = pk)
        borrow.due_date = due_date
        borrow.borrow_date = borrow_date
        book = Book.objects.get(pk = book_pk)
        member = Member.objects.get(pk=member_pk)
        borrow.book = book
        borrow.member = member
        borrow.save()

    def get_borrow(self, pk):
         obj = Borrowing.objects.get(pk=pk)
         return obj

    def get_list_of_borrowing(self):
        objects = Borrowing.objects.all()
        return objects
