from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.blog.models import Post, Tag
from tests.test_profile import User


class TagViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(
            username="admin",
            email="admin@mail.com",
            password="testpassword",
            role=User.ADMIN,
        )
        self.client.force_authenticate(user=self.admin)

    def test_create_tag_success(self):
        url = "/api/blog/tags/"
        data = {"name": "testtag"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_tag_fail_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = "/api/blog/tags/"
        data = {"name": "testtag"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(
            username="admin",
            email="admin@mail.com",
            password="testpassword",
            role=User.ADMIN,
        )
        self.tag = Tag.objects.create(name="testtag")
        self.client.force_authenticate(user=self.admin)

    def test_create_post_success(self):
        url = "/api/blog/posts/"
        data = {
            "title": "testpost",
            "content": "testcontent",
            "category": "testcategory",
            "tags": [self.tag.id],
            "author": self.admin.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_post_fail_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = "/api/blog/posts/"
        data = {
            "title": "testpost",
            "content": "testcontent",
            "category": "testcategory",
            "tags": [self.tag.id],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(
            username="admin",
            email="admin@mail.com",
            password="testpassword",
            role=User.ADMIN,
        )
        self.post = Post.objects.create(
            title="testpost",
            content="testcontent",
            category="testcategory",
            author=self.admin,
        )
        self.client.force_authenticate(user=self.admin)

    def test_create_comment_success(self):
        url = "/api/blog/comments/"
        data = {"post": self.post.id, "text": "testcomment", "user": self.admin.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_comment_fail_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = "/api/blog/comments/"
        data = {"post": self.post.id, "text": "testcomment"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LikeViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(
            username="admin", email="admin@mail.com", password="testpassword#"
        )
