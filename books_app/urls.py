from django.urls import path, re_path, include
from . import views
from .models import Book

urlpatterns = [
    path('', views.home, name="home"),
    path('book_list/', views.all_books, name="book-list"),
    path('book_add/', views.add_book, name="book-add"),
    path('book_detail/<book_id>', views.book_detail, name="book-detail"),
    path('book_search/', views.search_book, name="book-search"),
    path('book_update/<book_id>', views.update_book, name="book-update"),
    path('book_delete/<book_id>', views.delete_book, name="book-delete"),
    re_path(r'^book_filter/$', views.book_filter, name="book-filter"),
    path('google_books/', views.google_books, name="google-books"),

    #REST FRAMEWORK URLS
    path('api/', include('books_app.api.urls', 'books-api')),
]
