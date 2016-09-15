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
from django.views.decorators.csrf import csrf_exempt


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
            user.is_active = False
            user.save()
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
            return HttpHandler.json_response_wrapper([{'status': True}],
                                                     "Confirmation email is send to the registered email " + to_mail + ". Please check your email",
                                                     status.HTTP_200_OK)
        except Exception as e:
            return HttpHandler.json_response_wrapper([{'status': False}], str(e), status.HTTP_200_OK)

    @csrf_exempt
    def confirm_code(self, request):
        """
        api to check confirmation code
        """
        try:
            data = request.POST
            confirmation_code = data.get('confirmation_code', None)
            try:
                email_confirmation = EmailConfirmation.objects.filter(created__lte=datetime.datetime.now(),
                                                                      created__gt=datetime.datetime.now() - datetime.timedelta(
                                                                          days=3)).filter(
                    token=confirmation_code).get()
                selected_user = email_confirmation.user
            except EmailConfirmation.DoesNotExist:
                email_confirmation = None
            if selected_user.is_active:
                return HttpHandler.json_response_wrapper([{'status': False}], "Already verified", status.HTTP_200_OK,
                                                         True)
            if email_confirmation:
                selected_user.is_active = True
                selected_user.save()
                email_confirmation.email_verfied = True
                email_confirmation.save()
                return HttpHandler.json_response_wrapper([{'status': True}],
                                                         "Confirmation successfully verified.Please login to the system",
                                                         status.HTTP_200_OK, True)
            else:
                return HttpHandler.json_response_wrapper([{'status': False}], "Failure", status.HTTP_200_OK,
                                                         True)
        except Exception as e:
            return HttpHandler.json_response_wrapper([{'status': False}], str(e), status.HTTP_200_OK,
                                                     True)
