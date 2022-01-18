from django.test import TestCase, Client
from django.urls import reverse
from books_app.models import Book
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[getattr(self.test1, 'id')])
        self.test1 = Book.objects.create(
            id=100,
            title='Test Title 1',
            authors = 'Test Author',
            publishedDate = '2018-06-20',
            ISBN = '1234567890',
            pageCount = 369,
            thumbnail = "",
            language = "en",
        )


    def test_book_list_GET(self):

        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')



    def test_book_detail_GET(self):

        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_detail.html')

    def test_book_add_POST(self):
        Book.objects.create(
            book=self.test1,
            title='Test Title 2'
        )

        response = self.client.post(self.detail_url)

        self.assertEquals(response.status_code, 302)
