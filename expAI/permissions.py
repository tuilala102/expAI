from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
       Allows access only to owners
    """

    def has_permission(self, request, view):
       pk = request.GET.get('pk')
       user_meta = UsersMeta.objects.filter(user=request.user, token=pk).first()
       return True if user_meta and user_meta.type == "owner" else False


class IsAdmin(BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        usr = User.objects.get(username=request.user.username)
        print(usr)
        name_group = usr.roleid.name
        if name_group == "ADMIN":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        usr = User.objects.get(username=request.user.username)
        print(usr)
        name_group = usr.roleid.name
        if name_group == "ADMIN":
            return True
        return False

class IsTeacher(BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        usr = User.objects.get(username=request.user.username)
        print(usr)
        name_group = usr.roleid.name
        if name_group == "TEACHER":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        usr = User.objects.get(username=request.user.username)
        print(usr)
        name_group = usr.roleid.name
        if name_group == "TEACHER":
            return True
        return False

class IsStudent(BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        usr = User.objects.get(username=request.user.username)
        print(usr)
        name_group = usr.roleid.name
        if name_group == "STUDENT":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        usr = User.objects.get(username=request.user.username)
        print(usr)
        name_group = usr.roleid.name
        if name_group == "STUDENT":
            return True
        return False