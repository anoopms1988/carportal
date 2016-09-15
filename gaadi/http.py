from __future__ import absolute_import
from rest_framework import status as HttpStatus
from rest_framework.response import Response
from django.http import JsonResponse


class HttpHandler():
    @staticmethod
    def json_response_wrapper(data, message, status, native=False):
        content = {
            'response_code': status,
            'message': message,
            'data': data
        }
        if native:
            return JsonResponse(content, status=HttpStatus.HTTP_200_OK)
        else:
            return Response(content, status=status)

