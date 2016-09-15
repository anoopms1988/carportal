import datetime
import time

from django.shortcuts import render
from rest_framework import status, views
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .models import LoginAttempts, UserProfile, User, EmailConfirmation
from django.utils.crypto import get_random_string
from gaadi.http import HttpHandler


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
            username = data['username']
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email)
            email_confirmation = EmailConfirmation()
            email_confirmation.user = user
            email_confirmation.email_verfied = False
            random_token = get_random_string(8)
            email_confirmation.token = random_token
            ts = time.time()
            current_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            email_confirmation.created = current_time
            email_confirmation.save()
            confirmation_link = "/#/confirm/" + random_token
            to_mail = user.email
            # Email sending logic here
            return HttpHandler.json_response_wrapper([],
                                                     "Confirmation email is send to the registered email " + to_mail + ". Please check your email",
                                                     status.HTTP_200_OK)
        except Exception as e:
            return HttpHandler.json_response_wrapper([], e.message, status.HTTP_200_OK)
