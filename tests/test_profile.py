from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase

from apps.accounts.serializers import ProfileSerializer

User = get_user_model()


class ProfileViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_profile_retrieve(self):
        response = self.client.get(f"/api/users/profiles/{self.user.profile.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, ProfileSerializer(self.user.profile).data)

    def test_profile_update_unauthorized(self):
        new_bio = "Updated Bio"
        another_user = User.objects.create_user(
            username="anotheruser", password="12345"
        )
        client = APIClient()
        client.force_authenticate(user=another_user)
        response = client.patch(
            f"/api/users/profiles/{self.user.profile.id}/", {"bio": new_bio}
        )
        self.assertEqual(response.status_code, 403)  # Forbidden
