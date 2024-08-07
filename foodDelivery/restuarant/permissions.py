from rest_framework.permissions import BasePermission,SAFE_METHODS
from .models import resAdmin

class IsResAdmin(BasePermission):
    edit_methods = ("PUT", "PATCH","DELETE","POST")

    def has_permission(self, request, view):
        # Allow all users to view dishes
        if request.method in ["GET"]:
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        # Allow viewing of the dish for all authenticated users
        if request.method in ["GET"]:
            return request.user.is_authenticated

        # Check if the user is allowed to edit the dish
        if request.method in self.edit_methods:
            # Get the restaurant associated with the dish
            restaurant = obj.restaurant
            print(obj.restaurant,request.user,"**"*50)
            # Check if the current user is the admin of this restaurant
            try:
                res_admin = resAdmin.objects.get(user=request.user, res=restaurant)
                return True
            except resAdmin.DoesNotExist:
                return False
        return False
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff