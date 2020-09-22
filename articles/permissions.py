from rest_framework import permissions


class AuthorPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # Allow get requests for all
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author and request.user.is_authenticated
