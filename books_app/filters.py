import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    authors = django_filters.CharFilter(lookup_expr='icontains')
    language = django_filters.CharFilter(lookup_expr='iexact')
    date_gt = django_filters.NumberFilter(field_name='publishedDate', lookup_expr='gt')
    date_lt = django_filters.NumberFilter(field_name='publishedDate', lookup_expr='lt')
