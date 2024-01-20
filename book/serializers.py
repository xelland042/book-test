from rest_framework import serializers
from book.models import Book, Comment


class CommentSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    slug = serializers.ReadOnlyField(read_only=True)
    detail_link = serializers.HyperlinkedIdentityField(
        view_name='book-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Book
        fields = '__all__'
