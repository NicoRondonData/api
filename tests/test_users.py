from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.accounts.models import User


class UserViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(
            username="admin",
            email="admin@mail.com",
            password="testpassword",
            role=User.ADMIN,
        )
        self.blogger = User.objects.create_user(
            username="blogger",
            email="blogger@mail.com",
            password="testpassword",
            role=User.BLOGGER,
        )
        self.client.force_authenticate(user=self.admin)

    def test_create_user_success(self):
        url = "/api/users/users/"
        data = {
            "username": "testuser2",
            "email": "testuser2@mail.com",
            "password": "testpassword2",
            "role": User.EDITOR,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_fail_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = "/api/users/users/"
        data = {
            "username": "testuser3",
            "email": "testuser3@mail.com",
            "password": "testpassword3",
            "role": User.BLOGGER,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_user_fail_non_admin(self):
        self.client.force_authenticate(user=self.blogger)
        url = "/api/users/users/"
        data = {
            "username": "testuser4",
            "email": "testuser4@mail.com",
            "password": "testpassword4",
            "role": User.BLOGGER,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_user_success(self):
        url = f"/api/users/users/{self.blogger.id}/"
        data = {"username": "blogger_updated"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_fail_non_admin_or_owner(self):
        other_user = User.objects.create_user(
            username="other",
            email="other@mail.com",
            password="testpassword",
            role=User.EDITOR,
        )
        self.client.force_authenticate(user=other_user)
        url = f"/api/users/users/{self.blogger.id}/"
        data = {"username": "blogger_updated_again"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
