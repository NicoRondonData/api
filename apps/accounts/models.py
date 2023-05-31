from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 1
    EDITOR = 2
    BLOGGER = 3

    ROLE_CHOICES = (
        (ADMIN, "Admin"),
        (EDITOR, "Editor"),
        (BLOGGER, "Blogger"),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=BLOGGER)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Profile.objects.get_or_create(user=self)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
