from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from book.views import BookListCreateApiView

User = get_user_model()


class TestBookListCreateApiView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.book_data = {
            'title': 'Test Book',
            'price': '29.99',
            'author': 'Test Author',
            'user': self.user.id,
            'description': 'A test book description',
        }

    def test_create_book(self):
        response = self.client.post('', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_list_books(self):
        response = self.client.get('', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
