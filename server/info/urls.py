#

from django.urls import path,re_path
from . import views

app_name = 'info'
urlpatterns = [
	re_path(r'^board/(\d*)$',views.get_board, name='board'),
	re_path(r'^news/(\d*)$',views.get_news, name='news'),
]
