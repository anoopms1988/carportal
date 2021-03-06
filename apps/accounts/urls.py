from django.conf.urls import url
from .views import RegisterView,LoginView,LogoutView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^confirm/$', RegisterView().confirm_code, name='confirm'),
    url(r'^available/usernames/$', RegisterView().username_availability, name='username_availability'),
    url(r'^email/availability/$', RegisterView().email_availability, name='email_availability'),
    url(r'^login/$',LoginView.as_view(), name='login'),
    url(r'^logout/$',LogoutView.as_view(), name='logout'),
]
