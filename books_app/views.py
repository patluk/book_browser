from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def all_books(request):
    book_list = Book.objects.all()
    return render(request, 'book_list.html', {'book_list': book_list})

def add_book(request):
    submitted = False
    if request.method=="POST":
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
        books = Book.objects.filter(title__contains=searched)
        return render(request, 'book_search.html', {'searched':searched, 'books': books})
    else:
        return render(request, 'book_search.html', {})

def update_book(request, book_id):
    submitted = False
    book = Book.objects.get(pk=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book-detail', book_id)
    return render(request, 'book_update.html', {'book': book, 'form': form})

# def update_book(request, book_id):
#     submitted = False
#     book = Book.objects.get(pk=book_id)
#     form = BookForm(request.POST or None, instance=book)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect('/book_update?submitted=True')
#     return render(request, 'book_update.html', {'book': book, 'form': form, 'submitted': submitted})

# def update_book(request, book_id):
#     submitted = False
#     book = Book.objects.get(pk=book_id)
#     if request.method=="POST":
#         form = BookForm(request.POST or None, instance=book)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/book_update?submitted=True')
#     else:
#         form = BookForm(instance=book)
#         if 'submitted' in request.GET:
#             submitted = True
#     form = BookForm(instance=book)
#     return render(request, 'book_update.html', {'book': book, 'form': form, 'submitted': submitted})