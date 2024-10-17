from books_app.Reposetories.MemberRepository import MemberRepository
from rest_framework.exceptions import PermissionDenied, NotFound

class MemberComponent:

    def __init__(self):
        self.member_repository = MemberRepository()

    def create_member(self, name, email, phone_number, address, membership_date, membership_status):
        self.member_repository.create_member( name, email, phone_number, address, membership_date, membership_status)

    def update_member(self, id, name, email, phone_number, address, membership_date, membership_status):
        member = self.member_repository.get_member(id)
        if member is not None:
            self.member_repository.update_member(id, name, email, phone_number, address, membership_date, membership_status)
        else:
            raise NotFound("member not exists")

    def get_member(self, id):
        member = self.member_repository.get_member(id)
        if member is not None:
            return member
        else:
            raise NotFound("member not exists")

    
    def get_members_list(self):
        objects = self.member_repository.get_list_of_member()
        return objects
    
    def delete_member(self, id):
        member = self.member_repository.get_member(id)
        if member is not None:
            self.member_repository.delete_member(id)
        else:
            raise NotFound("member not exists")
