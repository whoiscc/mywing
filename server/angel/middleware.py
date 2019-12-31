#
from django.urls import reverse
from django.http import JsonResponse
from django.utils import timezone
from common import error
from .models import LoginItem


def login_checker_middleware(get_response):
    excluded_path_list = [
        reverse('angel:login'),
        reverse('angel:login-debug'),
    ]

    def middleware(request):
        if request.method not in ['GET', 'POST']:
            return get_response(request)

        if request.path in excluded_path_list:
            return get_response(request)

        if 'token' not in request.args:
            return error('not logged in')

        try:
            item = LoginItem.objects.get(pk=request.args['token'])
        except LoginItem.DoesNotExists:
            return error('invalid token')

        if item.expired_time < timezone.now():
            return error('token expired', code=2)

        request.angel = item.angel
        return get_response(request)

    return middleware
