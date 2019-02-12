#

from django.http import JsonResponse


def ok(payload=None):
    return JsonResponse({
        'status': 0, 'message': 'ok',
        **({'data': payload} if payload else {}),
    })


def error(message, code=1):
    return JsonResponse({
        'status': code,
        'message': message,
    })
