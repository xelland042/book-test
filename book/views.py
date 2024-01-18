from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from book.models import Book, Comment
from book.serializers import CommentSerializer, BookSerializer


class BookListCreateApiView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


class CommentCreateApiView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        book_slug = self.kwargs.get('slug')
        book = Book.objects.get(slug=book_slug)
        serializer.save(book_id=book.id)


class CommentDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
