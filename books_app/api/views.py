from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from books_app.models import Book
from books_app.api.serializers import BookSerializer


@api_view(['GET'])
def api_detail_book_view(request, slug):

    try:
        book = Book.Objects.get(slug=slug)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)


@api_view(['GET'])
def api_book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    authors = filters.CharFilter(lookup_expr='icontains')
    language = filters.CharFilter(lookup_expr='iexact')
    date_gt = filters.NumberFilter(field_name='publishedDate', lookup_expr='gt')
    date_lt = filters.NumberFilter(field_name='publishedDate', lookup_expr='lt')


class ApiBooksListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter
