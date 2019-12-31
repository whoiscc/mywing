#

from django.http import JsonResponse
from json import loads
from functools import wraps


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


class ExceptionWithResponse(Exception):
    def __init__(self, response):
        self.response = response


def catch_EWR(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ExceptionWithResponse as ex:
            return ex.response

    return wrapper


class ExpectArgumentException(ExceptionWithResponse):
    def __init__(self, arg_name):
        self.arg_name = arg_name
        super().__init__(error(f'expect argument: {arg_name}'))


def extract(request, *args):
    assert len(args) != 0
    results = []
    for arg_name in args:
        if arg_name not in request.args:
            raise ExpectArgumentException(arg_name)
        results.append(request.args[arg_name])
    if len(results) == 1:
        return results[0]
    else:
        return tuple(results)


class InvalidIDException(ExceptionWithResponse):
    def __init__(self, model_class, invalid_id):
        self.model_class = model_class
        self.invalid_id = invalid_id
        super().__init__(
            error(f'Invalid ID {invalid_id} for model {model_class}'))


def get_object(model_class, pk):
    try:
        return model_class.objects.get(pk=pk)
    except model_class.DoesNotExist:
        raise InvalidIDException(model_class, pk)


@catch_EWR
def get_objects_with_id_list(model_class, request, **kwargs):
    objects = []
    for pk in extract(request, 'id_list'):
        objects.append(get_object(model_class, pk).to_dict(**kwargs))
    return ok(objects)
