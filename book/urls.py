from django.urls import path
from book.views import BookListCreateApiView, BookDetail, CommentCreateApiView, CommentDetailApiView

urlpatterns = [
    path('', BookListCreateApiView.as_view(), name='book-list-create'),
    path('<slug:slug>/', BookDetail.as_view(), name='book-detail'),
    path('<slug:slug>/addcomment/', CommentCreateApiView.as_view(), name='book-comment'),
    path('comments/<int:pk>/', CommentDetailApiView.as_view(), name='comment-detail')
]
