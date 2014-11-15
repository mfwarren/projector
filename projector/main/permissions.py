from rest_framework import permissions

from posts.models import Task


class IsAuthenticatedAndOwnsObject(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            return False

        _id = self.kwargs['pk']

        return Task.objects.filter(id=_id, project_id=request.user).exists()
