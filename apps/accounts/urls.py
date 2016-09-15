from django.conf.urls import url
from .views import RegisterView

urlpatterns = [
    url(r'^register/$',RegisterView.as_view(), name='register'),
    url(r'^confirm/$', RegisterView().confirm_code, name='confirm'),
]
