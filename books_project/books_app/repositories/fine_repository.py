from books_app.models import Fine, Borrowing, session, Member
from rest_framework.exceptions import PermissionDenied, NotFound
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import joinedload


class FineRepository:

    def __init__(self):
        print("this is FineRepository class")
    @staticmethod
    def create_fine(self, borrow, fine_amount, fine_status, commit=True):
        fine_instance = Fine(borrow=borrow, fine_amount=fine_amount, fine_status=fine_status)
        session.add(fine_instance)
        if commit:
            session.commit()
        else:
            session.flush()
    @staticmethod
    def update_fine(self, fine_id, data, commit=True):
        fine_instance = session.query(Fine).\
            filter(Fine.id == fine_id).\
            update(data, synchronize_session=False)
        if commit:
            session.commit()
        else:
            session.flush()

    @staticmethod
    def get_fine(self, fine_id):
        fine = session.query(Fine).filter(Fine.id == fine_id).one_or_none()
        return fine

    @staticmethod
    def get_member_fines(self, member_id):
        member_fines = session.query(Fine).options(joinedload(Fine.borrow)).filter(Borrowing.member_id == member_id). all()
        return member_fines
