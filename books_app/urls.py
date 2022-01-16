from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('book_list', views.all_books, name="book-list"),
    path('book_add', views.add_book, name="book-add"),
    path('book_detail/<book_id>', views.book_detail, name="book-detail"),
    path('book_search', views.search_book, name="book-search"),
    path('book_update/<book_id>', views.update_book, name="book-update"),
]
