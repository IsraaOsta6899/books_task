from books_app.models import Fine, Borrowing, session, Member
from rest_framework.exceptions import PermissionDenied, NotFound
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import joinedload


class FineRepository:

    def __init__(self):
        print("this is FineRepository class")

    def create_fine(self, borrow, fine_amount, fine_status):
        fine_instance = Fine()
        fine_instance.borrow = borrow
        fine_instance.fine_amount = fine_amount
        fine_instance.fine_status = fine_status
        session.add(fine_instance)
        session.commit()

    def update_fine(self, id, fine_amount, fine_status):
        try:
            fine_instance = session.query(Fine).filter(Fine.id == id).one_or_none()
            fine_instance.fine_status = fine_status
            fine_instance.fine_amount = fine_amount
            session.commit()
        except MultipleResultsFound:
            raise NotFound("there are more than one fine")

    def get_fine(self, id):
        try:
            fine = session.query(Fine).filter(Fine.id == id).one_or_none()
            return fine
        except MultipleResultsFound:
            raise NotFound("there are more than one fine")

    def get_member_fines(self, member_id):
        fines_list = session.query(Fine).options(joinedload(Fine.borrow)).filter(Borrowing.member_id == member_id). all()
        return fines_list
