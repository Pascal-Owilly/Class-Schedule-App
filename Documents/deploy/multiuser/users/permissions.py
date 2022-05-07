from rest_framework.permissions import BasePermission



class IsTmUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_tm)


class IsStudentUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_student)

        