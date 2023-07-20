from rest_framework.permissions import BasePermission
from .models import User


class IsStandardUser(BasePermission):
    """Allow access to create experience, extras and proyects."""

    def has_permission(self, request, view):

        try:
            user = User.objects.get(
                email=request.user,
                is_recruiter=False
            )
        except User.DoesNotExist:
            return False
        return True