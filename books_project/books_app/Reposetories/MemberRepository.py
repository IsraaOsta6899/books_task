from books_app.models import Member

class MemberRepository:

    def __init__(self):
        print("this is Member class")

    def create_member(self, name, email, phone_number, address, membership_date, membership_status):
        member = Member()
        member.name = name
        member.email = email
        member.phone_number = phone_number
        member.address = address
        member.membership_date = membership_date
        member.membership_status = membership_status
        member.save()

    def update_member(self, pk, name, email, phone_number, address, membership_date, membership_status):
        member = Member.objects.get(pk = pk)
        # data = json.loads(request.body)
        member.name = name
        member.email = email
        member.phone_number = phone_number
        member.address = address
        member.membership_date = membership_date
        member.membership_status = membership_status
        member.save()

    def delete_member(self, pk):
        member_instance = Member.objects.get(pk = pk)
        member_instance.delete()

    def get_member(self, pk):
         obj = Member.objects.get(pk=pk)
         return obj

    def get_list_of_member(self):
        objects = Member.objects.all()
        return objects
