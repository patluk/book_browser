from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.http import HttpResponseRedirect
from .filters import BookFilter


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def all_books(request):
    book_list = Book.objects.all().order_by('title')
    return render(request, 'book_list.html', {'book_list': book_list})


def add_book(request):
    submitted = False
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book_add?submitted=True')
    else:
        form = BookForm
        if 'submitted' in request.GET:
            submitted = True
    form = BookForm
    return render(request, 'book_add.html', {'form': form, 'submitted': submitted})


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_detail.html', {'book': book})


def search_book(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(title__icontains=searched)
        return render(request, 'book_search.html', {'searched': searched, 'books': books})
    else:
        return render(request, 'book_search.html', {})


def update_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book-detail', book_id)
    return render(request, 'book_update.html', {'book': book, 'form': form})


def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect('book-list')


def book_filter(request):
    books = Book.objects.all()
    f = BookFilter(request.GET, queryset=books)
    return render(request, 'book_filter.html', {'filter': f})


def get_books(request):
    book_dict = {}
    books = []
    if 'title' in request.GET:
        title = request.GET['title']
        url = 'https://www.googleapis.com/books/v1/volumes?q = %s' % title
        response = requests.get(url)
        data = response.json()
        fetched_books = data['items']

        for i in fetched_books:
            book_dict = {
                'title': book['volumeInfo']['title'],
                'image': book['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in book['volumeInfo'] else "",
                'authors': ", ".join(book['volumeInfo']['authors']) if 'authors' in book['volumeInfo'] else "",
                'publisher': book['volumeInfo']['publisher'] if 'publisher' in book['volumeInfo'] else "",
                'info': book['volumeInfo']['infoLink'],
                'popularity': book['volumeInfo']['ratingsCount'] if 'ratingsCount' in book['volumeInfo'] else 0
            }
            books.append(book_dict)

            #book_data.save()
            #book_list = Book.objects.all().order_by('-id')

    return render(request, 'google_books.html', {"book_list": book_list})