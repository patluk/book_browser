from django import forms
from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ("title", "authors", "publishedDate", "ISBN", "pageCount", "thumbnail", "language")
        labels = {
            "title": '',
            "authors": '',
            "publishedDate": '',
            "ISBN": '',
            "pageCount": '',
            "thumbnail": '',
            "language": '',
        }
        widgets = {
            "title":forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book title'}),
            "authors":forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author(s)'}),
            "publishedDate":forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of publishing'}),
            "ISBN":forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN number'}),
            "pageCount":forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Page count'}),
            "thumbnail":forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Thumbnail'}),
            "language":forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Language'})
        }
