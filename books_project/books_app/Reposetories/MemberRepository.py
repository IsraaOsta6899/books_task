from books_app.models import Member, session
from rest_framework.exceptions import PermissionDenied, NotFound
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from datetime import datetime

class MemberRepository:

    def __init__(self):
        print("this is Member class")

    def create_member(self, name, email, phone_number, address, membership_date, membership_status):
        
        member = Member()
        member.name = name
        member.email = email
        member.phone_number = phone_number
        member.address = address
        date_obj = datetime.strptime(membership_date, '%Y-%m-%d').date()  # Converts string to date object
        member.membership_date = date_obj
        member.membership_status = membership_status
        session.add(member)
        session.commit()
        

    def update_member(self, id, name, email, phone_number, address, membership_date, membership_status):
        try:
            member = session.query(Member).filter(Member.id == id).one_or_none()
            if member is not None:
                member.name = name
                member.email = email
                member.phone_number = phone_number
                member.address = address
                date_obj = datetime.strptime(membership_date, '%Y-%m-%d').date()  # Converts string to date object
                member.membership_date = date_obj
                member.membership_status = membership_status
                session.commit()   
        except MultipleResultsFound:
            session.rollback()
            print("Multiple members found with the specified criteria.")
            raise MultipleResultsFound("Multiple members found with the specified criteria.")
        

    def delete_member(self, id):
        member = session.query(Member).filter(Member.id == id).one_or_none()
        session.delete(member)
        session.commit()


    def get_member(self, id):
        try:
            member = session.query(Member).filter(Member.id == id).one_or_none()
            return member
        except MultipleResultsFound:
            print("Multiple Members found with the specified criteria.")
            raise MultipleResultsFound("Multiple members found with the specified criteria.")

    def get_list_of_member(self):
        members_list = session.query(Member).all()
        return members_list
