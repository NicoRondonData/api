from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Profile, User
from .permissions import IsAdminUser, IsAdminUserOrSelf
from .serializers import ProfileSerializer, UserCreateSerializer, UserListSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        elif self.action == "list":
            return UserListSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAdminUser]
        elif self.action == "update" or self.action == "partial_update":
            permission_classes = [IsAdminUserOrSelf]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.action == "update" or self.action == "partial_update":
            permission_classes = [IsAdminUserOrSelf]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
