from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")  # Log in the test user

        # Create some initial Book data
        self.book = Book.objects.create(title="Test Book", author="Test Author", published_year=2022)

        self.list_url = "/api/books/"

    def test_list_books(self):
        # Test retrieving all books
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", str(response.data))

    def test_create_book(self):
        # Test creating a new book
        data = {"title": "New Book", "author": "New Author", "published_year": 2023}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Confirm the book count increases

    def test_update_book(self):
        # Test updating an existing book
        update_url = f"{self.list_url}{self.book.id}/"
        data = {"title": "Updated Title", "author": "Updated Author", "published_year": 2022}
        response = self.client.put(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        # Test deleting a book
        delete_url = f"{self.list_url}{self.book.id}/"
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        # Test filtering books (e.g., by author)
        response = self.client.get(self.list_url, {"author": "Test Author"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_unauthenticated_access(self):
        # Test accessing the API without authentication
        self.client.logout()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
