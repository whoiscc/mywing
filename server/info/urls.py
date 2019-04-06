#

from django.urls import path,re_path
from . import views

app_name = 'info'
urlpatterns = [
	path('board',views.get_board, name='board'),
]
