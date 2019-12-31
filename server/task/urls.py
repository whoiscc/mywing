from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
	path('create',views.create, name='create'),
	path('accept',views.accept, name='accept'),
	path('finish',views.finish, name='finish'),
	path('confirm',views.confirm, name='confirm'),
	path('cancel',views.cancel, name='cancel'),
	path('available',views.get_task_available, name='available'),
	path('self',views.get_self_task, name='self'),
	path('',views.get_task),
]
