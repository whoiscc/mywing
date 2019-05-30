#
import json


def extract_arguments_middleware(get_response):

    def middleware(request):
        # 从请求头中获取token
        token = request.META.get('HTTP_X_TOKEN')

        if request.method not in ['GET', 'POST']:
            return get_response(request)

        if request.method == 'GET':
            if 'data' in request.GET:
                args = json.loads(request.GET['data'])
            else:
                args = {}
        else:
            if len(request.body) != 0:
                args = json.loads(request.body)
            else:
                # 空请求体时args强制为空字典
                args = {}
        
        # token不为空时注入token
        if token:
            args['token'] = token

        request.args = args
        return get_response(request)

    return middleware
