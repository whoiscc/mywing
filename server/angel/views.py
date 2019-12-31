#

from django.views.generic import TemplateView
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST
from common import ok, error, get_objects_with_id_list

import datetime
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

        created = False
        try:
            angel = Angel.objects.get(central_key=central_key)
        except Angel.DoesNotExists:
            created = True
            angel = Angel(
                nickname='SuperAwesomeName',
                central_key=central_key,
                distribution=0.0,
            )
            angel.save()

        item = LoginItem(angel=angel)
        item.expired_time = timezone.now() + datetime.timedelta(days=30)
        item.save()

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
        angel = Angel(
            nickname='SuperAwesomeName',
            central_key='debug-central-key-' + str(time.mktime(now.timetuple())),
            distribution=0.0,
        )
        angel.save()

        item = LoginItem(angel=angel)
        item.expired_time = now + datetime.timedelta(days=30)
        item.save()

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
