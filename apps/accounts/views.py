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
from .functions import get_similar_names,get_client_ip
from django.contrib.auth import authenticate, login, logout, hashers
from .serializers import UserSerializer


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

    @csrf_exempt
    def username_availability(self, request, format=None):
        """
        api to check username availability and suggest usernames
        """
        data = request.POST
        username = data.get('username', None)
        try:
            account = User.objects.filter(username=username).get()
            similar_strings = [account.first_name, account.last_name]
            suggested_usernames = [name for name in get_similar_names(username, similar_strings)]
        except User.DoesNotExist:
            account = None
        if account:
            return HttpHandler.json_response_wrapper([{
                'available_usernames': suggested_usernames, 'status': False
            }], "Same username already exist", status.HTTP_200_OK, True)
        else:
            return HttpHandler.json_response_wrapper([{'status': True
                                                       }], "Username available", status.HTTP_200_OK, True)

    @csrf_exempt
    def email_availability(self, request):
        """
        api to check email availability
        """
        data = request.POST
        email = data.get('email', None)
        try:
            account = User.objects.filter(email=email).get()
        except User.DoesNotExist:
            account = None
        if account:
            return HttpHandler.json_response_wrapper([{'status': False}], "Same email already exist",
                                                     status.HTTP_200_OK, True)
        else:
            return HttpHandler.json_response_wrapper([{'status': True}], "Email available", status.HTTP_200_OK, True)

@permission_classes((AllowAny,))
class LoginView(views.APIView):
    def post(self, request, format=None):
        """
        api function to make a login using username and password
        """
        try:
            data = request.data
            username = data.get('username', None)
            password = data.get('password', None)
            try:
                existing_account = User.objects.filter(username=username).get()
            except:
                existing_account = None
            if not existing_account:
                return HttpHandler.json_response_wrapper([], "No user exist with given username", status.HTTP_200_OK)
            if username and password:
                user = authenticate(username=username, password=password)
                if user:
                    if user.is_active:
                        login(request, user)
                        account =User.objects.get(id=user.id)
                        serialized = UserSerializer(account)
                        return HttpHandler.json_response_wrapper([{'status': True, "data": serialized.data}], "Success",
                                                                 status.HTTP_200_OK)
                    else:
                        return HttpHandler.json_response_wrapper([{'status': False, "data": []}], "User is not active",
                                                                 status.HTTP_200_OK)
                else:
                    try:
                        account = User.objects.filter(username=username).get()
                    except User.DoesNotExist:
                        account = None
                    if account:
                        ip_address = get_client_ip(request)
                        user_agent = request.META['HTTP_USER_AGENT']
                        login_attempts = LoginAttempts()
                        login_attempts.username = username
                        login_attempts.email = account.email
                        login_attempts.ip_address = ip_address
                        login_attempts.user_agent = user_agent
                        login_attempts.save()
                        failed_count = LoginAttempts.objects.filter(failed_time__lte=datetime.datetime.now(),
                                                                    failed_time__gt=datetime.datetime.now() - datetime.timedelta(
                                                                            minutes=5)).count()
                        if failed_count > 3:
                            to_mail = account.email
                            username = account.username
                            # try:
                            #     EmailHandler.send('login-attempts', to_mail, {'first_name': username})
                            # except Exception as e:
                            #     pass
                    return HttpHandler.json_response_wrapper([], "Invalid password", status.HTTP_200_OK)
        except Exception as e:
            return HttpHandler.json_response_wrapper([], e.message, status.HTTP_200_OK)

class LogoutView(views.APIView):
    def post(self, request, format=None):
        """
        to logout from the system
        """
        logout(request)
        return HttpHandler.json_response_wrapper([], "Successfully logged out from system", status.HTTP_200_OK)