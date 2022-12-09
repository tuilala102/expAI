from rest_framework.permissions import BasePermission
from .models import *
class IsOwner(BasePermission):
    """
       Allows access only to owners
    """

    def has_object_permission(self, request, view, obj):
       
        if request.user == obj.datasetowner:
            return True

        return False
class IsOwnerOfObject(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class IsOwnerExp(BasePermission):
    """
       Allows access only to owners
    """

    def has_object_permission(self, request, view, obj):
       
        if request.user == obj.expcreatorid:
            return True

        return False

class IsAdmin(BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        usr = User.objects.get(email=request.user.email)
        print(usr)
        name_group = usr.roleid.rolename
        if name_group == "ADMIN":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        usr = User.objects.get(email=request.user.email)
        print(usr)
        name_group = usr.roleid.rolename
        if name_group == "ADMIN":
            return True
        return False

class IsTeacher(BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        usr = User.objects.get(email=request.user.email)
        print(usr)
        name_group = usr.roleid.rolename
        if name_group == "TEACHER":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        usr = User.objects.get(email=request.user.email)
        print(usr)
        name_group = usr.roleid.rolename
        if name_group == "TEACHER":
            return True
        return False

class IsStudent(BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        usr = User.objects.get(email=request.user.email)
        print(usr)
        name_group = usr.roleid.rolename
        if name_group == "STUDENT":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        usr = User.objects.get(email=request.user.email)
        print(usr)
        name_group = usr.roleid.rolename
        if name_group == "STUDENT":
            return True
        return False