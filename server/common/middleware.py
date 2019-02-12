#
import json


def extract_arguments_middleware(get_response):

    def middleware(request):
        if request.method not in ['GET', 'POST']:
            return get_response(request)

        if request.method == 'GET':
            if 'data' in request.GET:
                args = json.loads(request.GET['data'])
            else:
                args = {}
        else:
            args = json.loads(request.body)

        request.args = args
        print(request.args)
        return get_response(request)

    return middleware
