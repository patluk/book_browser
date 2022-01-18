from django.urls import path
from books_app.api.views import api_book_list, api_detail_book_view, ApiBooksListView

app_name = 'books_app'

urlpatterns = [
    # path('all/', api_book_list, name="all"),
    # path('<slug>/', api_detail_book_view, name="detail"),
    path('', ApiBooksListView.as_view(), name="all"),
]
