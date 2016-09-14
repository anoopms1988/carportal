from django.shortcuts import render
from rest_framework import status, views
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .models import LoginAttempts, UserProfile, User, EmailConfirmation


@permission_classes((AllowAny,))
class RegisterView(views.APIView):
    """
    To register new user
    """

    def post(self, request, format=None):
        try:
            data = request.data
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            username =data['username']
            user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email)
            pass
        except Exception as e:
            pass
