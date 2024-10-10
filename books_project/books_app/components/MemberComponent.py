from books_app.Reposetories.MemberRepository import MemberRepository
from books_app.models import Member
class MemberComponent:

    def __init__(self):
        self.member_repository = MemberRepository()

    def create_member(self, name, email, phone_number, address, membership_date, membership_status):
        self.member_repository.create_member( name, email, phone_number, address, membership_date, membership_status)

    def update_member(self, pk, name, email, phone_number, address, membership_date, membership_status):
        self.member_repository.update_member(pk, name, email, phone_number, address, membership_date, membership_status)

    def get_member(self, pk):
        book = self.member_repository.get_member(pk)
        return book
    
    def get_members_list(self):
        objects = self.member_repository.get_list_of_member()
        return objects
    
    def delete_member(self, pk):
        self.member_repository.delete_member(pk)

        
