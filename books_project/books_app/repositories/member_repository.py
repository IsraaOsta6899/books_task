from books_app.models import Member, session
from rest_framework.exceptions import PermissionDenied, NotFound
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from datetime import datetime

class MemberRepository:

    @staticmethod
    def create_member(name, email, phone_number, address, membership_date, membership_status, commit=True):
        member = Member(name=name, email=email, phone_number=phone_number,
                        address=address, membership_date=membership_date, 
                        membership_status=membership_status)
        session.add(member)
        if commit:
            session.commit()
        else:
            session.flush()

    @staticmethod
    def update_member(member_id, data, commit=True):
            member = session.query(Member).\
                filter(Member.id == member_id).\
                update(data, synchronize_session=False)
            if commit:
                session.commit()   
            else:
                session.flush()     
        
    @staticmethod
    def delete_member(member_id, commit=True):
        member = session.query(Member).\
            filter(Member.id == member_id).\
            delete()
        if commit:
            session.commit()

    @staticmethod
    def get_member(member_id):
        member = session.query(Member).filter(Member.id == member_id).one_or_none()
        return member

    @staticmethod
    def get_members():
        members = session.query(Member).all()
        return members
