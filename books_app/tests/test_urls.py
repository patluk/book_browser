from django.test import SimpleTestCase
from django.urls import reverse, resolve
from books_app import views


class TestUrls(SimpleTestCase):

    def test_book_list_url_resolves(self):
        url = reverse("book-list")
        print(resolve(url))
        self.assertEquals(resolve(url).func, views.all_books)

    def test_book_add_url_resolves(self):
        url = reverse("book-add")
        print(resolve(url))
        self.assertEquals(resolve(url).func, views.add_book)

    def test_book_detail_url_resolves(self):
        url = reverse("book-detail", args=['id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, views.book_detail)

    def test_book_update_url_resolves(self):
        url = reverse("book-update", args=['id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, views.update_book)

    def test_book_delete_url_resolves(self):
        url = reverse("book-delete", args=['id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, views.delete_book)
