from datetime import datetime
from typing import List

from books_app.models import Member
from books_app.repositories.member_repository import MemberRepository
from rest_framework.exceptions import NotFound
from constants import DateTimeFormat

class MemberComponent:
    @staticmethod
    def create_member(name: str, email: str, phone_number: str, address: str,
                       membership_date: str, membership_status: str):
        MemberRepository.create_member( name, email, phone_number, address, membership_date, membership_status)

    @staticmethod
    def update_member(member_id: int, name: str, email: str, phone_number: str,
                       address: str, membership_date: str, membership_status: str):
        member_date = datetime.strptime(membership_date, DateTimeFormat.ISO_DATE_FORMAT).date()
        member_data = {
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "address": address,
            "membership_date": member_date,
            "membership_status": membership_status
        }
        member = MemberRepository.get_member(member_id=member_id)
        if member is None:
            raise NotFound("member not exists")
        MemberRepository.update_member(member_id=member_id, data=member_data)

    @staticmethod
    def get_member(member_id) -> Member:
        member = MemberRepository.get_member(member_id=member_id)
        if member is None:
            raise NotFound("member not exists")
        return member

    @staticmethod
    def get_members() -> List[Member]:
        members = MemberRepository.get_members()
        return members

    @staticmethod
    def delete_member(member_id):
        member = MemberRepository.get_member(member_id=member_id)
        if member is None:
            raise NotFound("member not exists")
        MemberRepository.delete_member(member_id=member_id)            