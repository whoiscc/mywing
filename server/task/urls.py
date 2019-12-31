from django.urls import path
from . import views

urlpatterns = [
	path('create',views.create, name='create'),
	path('accept',views.accept, name='accept'),
	path('finish',views.finish, name='finish'),
	path('confirm',views.confirm, name='confirm'),
	path('cancel',views.cancel, name='cancel'),
	path('available',views.avaiable, name='available'),
	path('self',views.self, name='self'),
]
