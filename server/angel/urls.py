#

from django.urls import path
from . import views

app_name = 'angel'
urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('login~debug', views.debug_login, name='login-debug'),
    path('logout', views.logout),
    path('', views.get_angels),
]
