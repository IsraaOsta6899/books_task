from django.urls import path

from books_app.views import BookView, AuthorView, MemberView, get_csrf_token, BorrowingView, FineView

urlpatterns = [
    path('books', BookView.as_view()),
    path('books/<int:pk>', BookView.as_view()),
    path('authors', AuthorView.as_view()),
    path('authors/<int:pk>', AuthorView.as_view()),
    path('members', MemberView.as_view()),
    path('members/<int:pk>', MemberView.as_view()),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    # path('member/<int:member_pk>/book/<int:book_pk>/bo',BorrowingView.as_view()),
    path('borrowing', BorrowingView.as_view()),
    path('borrowing/<int:pk>', BorrowingView.as_view()),
    path('fines/<int:pk>', FineView.as_view()),
    path('fines', FineView.as_view()),
    path('fines/get_member_fines/<int:member_id>', FineView.as_view()) #members/member_id/fines
]