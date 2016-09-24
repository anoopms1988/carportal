from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from calendar import timegm
from datetime import datetime, timedelta
from .models import User

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class UserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField('get_auth_token')

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'auth_token', 'username',)

    def get_auth_token(self, Account):
        # api_settings.JWT_EXPIRATION_DELTA = timedelta(days=30)
        payload = jwt_payload_handler(Account)
        # Override default token expiration time
        if api_settings.JWT_ALLOW_REFRESH:
            payload['orig_iat'] = timegm(
                datetime.utcnow().utctimetuple()
            )
        return jwt_encode_handler(payload)
