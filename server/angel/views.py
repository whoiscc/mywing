#

from django.views.generic import TemplateView
from django.http.response import JsonResponse


class LoginView(TemplateView):
    def get(self, request):
        if 'token' in request.GET:
            return JsonResponse({'message': 'Logged in!'})
        else:
            return JsonResponse({'message': 'Not logged in!'})

    def post(self, request):
        request.session['angel'] = 'user'
        return JsonResponse({'message': 'ok', 'token': '123456qwerty'})


def logout(request):
    # del request.session['angel']
    return JsonResponse({'message': 'ok'})


def get_angels(request):
    return JsonResponse({'message': 'ok'})
