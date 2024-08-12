from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import Group, User
from rest_framework import authentication, permissions

from .serializers import userSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.conf import settings
from django.http import HttpResponseRedirect


def email_confirm_redirect(request, key):
    return HttpResponseRedirect(
        f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"
    )


class users(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
