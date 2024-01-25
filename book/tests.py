from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from book.models import Book

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
        self.book = Book.objects.create(
            title='Existing Book',
            price='19.99',
            author='Existing Author',
            user=self.user,
            description='An existing book description',
        )

    def test_create_book(self):
        response = self.client.post('', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_list_books(self):
        response = self.client.get('', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Existing Book')

    def test_retrieve_book(self):
        response = self.client.get(f'/{self.book.slug}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Existing Book')

    def test_update_book(self):
        updated_data = {'title': 'Updated Book', 'price': '25.99', 'author': 'Updated Author'}
        response = self.client.patch(f'/{self.book.slug}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(slug=self.book.slug).title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(f'/{self.book.slug}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
        self.assertFalse(Book.objects.filter(slug=self.book.slug).exists())
