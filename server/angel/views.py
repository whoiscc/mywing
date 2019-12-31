#

from django.views.generic import TemplateView
from django.views.decorators.http import require_GET, require_POST
from django.utils import timezone
from common import ok, error, get_objects_with_id_list

import time

from .models import Angel, LoginItem


class LoginView(TemplateView):
    def get(self, request):
        back = request.args['back']
        # TODO: decide redirect URL base on request.args['region']
        return ok({'url': 'https://google.com'})

    def post(self, request):
        ticket = request.args['ticket']
        # TODO: process ticket into central key
        central_key = ticket

        angel, item, created = Angel.login_and_optional_create(central_key)

        return ok({
            'created': created,
            'token': item.token,
            'angel': angel.to_dict(),
        })


@require_POST
def debug_login(request):
    ticket = request.args['ticket']
    if ticket == 'debug-ticket-create-angel':
        now = timezone.now()
        central_key = 'debug-central-key-' + str(time.mktime(now.timetuple()))

        angel, item, created = Angel.login_and_optional_create(central_key)
        assert created

        return ok({
            'created': True,
            'token': item.token,
            'angel': angel.to_dict(),
        })
    else:
        return error('unknown debug ticket')


@require_POST
def logout(request):
    item = LoginItem.objects.get(token=request.args['token'])
    item.delete()
    return ok()


@require_GET
def get_angels(request):
    return get_objects_with_id_list(Angel, request)
