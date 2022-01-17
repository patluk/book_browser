from rest_framework import serializers
from books_app.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "authors", "publishedDate", "ISBN", "pageCount", "thumbnail", "language"]
