from rest_framework import permissions

from .models import User


class IsAdminUser(permissions.BasePermission):
    """Permission class to allow only admin users."""

    def has_permission(self, request, view):
        """
        Check if the user has permission to access the view.

        Args:
            request: The request being made.
            view: The view being accessed.

        Returns:
            bool: True if the user is authenticated; False otherwise.
        """
        if not request.user.is_authenticated:
            return False
        if request.user.role == User.ADMIN:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to access the object.

        Args:
            request: The request being made.
            view: The view being accessed.
            obj: The object being accessed.

        Returns:
            bool: True if the user is an admin or the object is owned by the user; False otherwise.
        """
        if request.user.role == User.ADMIN:
            return True
        return obj == request.user


class IsAdminUserOrSelf(permissions.BasePermission):
    """Permission class to allow admin users or the owner of the object."""

    def has_permission(self, request, view):
        """
        Check if the user has permission to access the view.

        Args:
            request: The request being made.
            view: The view being accessed.

        Returns:
            bool: True if the user is authenticated; False otherwise.
        """
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to access the object.

        Args:
            request: The request being made.
            view: The view being accessed.
            obj: The object being accessed.

        Returns:
            bool: True if the user is an admin or the object is owned by the user; False otherwise.
        """
        if request.user.role == User.ADMIN:
            return True
        return obj == request.user


class IsOwnerOrAdminOrReadOnly(IsAdminUserOrSelf):
    """Permission class to allow owners or admin users to modify objects and read-only access to others."""

    def has_permission(self, request, view):
        """
        Check if the user has permission to access the view.

        Args:
            request: The request being made.
            view: The view being accessed.

        Returns:
            bool: True if the user has read-only access or is an admin/owner; False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return super().has_permission(request, view)
