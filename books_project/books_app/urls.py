from django.urls import include, path
from books_app.views import BookViewSet, AuthorViewSet, MemberViewSet, BorrowingViewSet, FineViewSet
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'members', MemberViewSet, basename='member')
router.register(r'borrowings', BorrowingViewSet, basename='borrowing')
members_router = routers.NestedSimpleRouter(router, r'members', lookup='member')
members_router.register(r'fines', FineViewSet, basename='member-fines')
borrowings_router = routers.NestedSimpleRouter(router, r'borrowings', lookup='borrowing')
borrowings_router.register(r'fines', FineViewSet, basename='borrowing-fines')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(borrowings_router.urls)),
    path(r'', include(members_router.urls)),
]

# urlpatterns = [
#     path('fines/<int:pk>', FineView.as_view()),
#     path('fines', FineView.as_view()),
#     path('members/<int:member_id>/fines', FineView.as_view()),
#     path('borrow/<int:borrow_id>/fines/<int:fine_id>', FineView.as_view())
# ]