from django.views.generic import TemplateView

import datetime
import time
import sys
import os

from django.views.decorators.http import require_GET, require_POST
from common import ok,error,extract,get_object,get_objects_with_id_list
from .models import Task
from random import sample

o_path = os.getcwd()

sys.path.append(o_path)
from angel import views


@require_POST
def create(request):
	owner_id=views.debug_login()
	task = Task(
		owner=owner_id,
		description=request.args[description],
		cost=request.args[cost],
		token=request.args[token],
		status=0,
	)
	task.save()	
	return ok(task.to_dict())


@require_POST
def accept(request):
	change_task_status(request,1,'helper')


@require_POST
def finish(request):
	change_task_status(request,2,'helper')


@require_POST
def confirm(request):
	change_task_status(request,3,'owner')	


@require_POST
def cancel(request):
	cancel_status_dict={
		'unpick':-1,
		'unfinish':-2,
		'unconfirm':-3,
		}
	next_status=cancel_status_dict(request.args[id].get_object.status)
	change_task_status(request,next_status,'owner')


@require_GET
def get_task_available(request):
	list_num=int(request.args[max])
	task_list=Task.objects.get()
	return ok([task.to_dict() for task in task_list])
	

@require_GET
def get_self_task(request):
	angel_id=get_current_angel_method()
	involve_task=[]
	for task_id in extract(request,'id_list'):
		task=get_object(Task,task_id)
		if task.owner==angel_id or task.helper==angel_id:
			if request.args[inProgress]!=false or task.status==0 or task.status==1 or task.status==2:
				involve_task.append(task)
	return ok([task.to_dict() for task in involve_task])
 

@require_GET
def get_task(request):
	return get_objects_with_id_list(Task, request)


def change_task_status(request,status,from_owner_or_helper):
	task_id=request.args[id]
	task=get_object(Task,task_id)
	if from_owner_or_helper=='owner':
		checked_angel=task.owner
	else:
		checked_angel=task.helper
	if checked_angel==views.debug_login():
		task.set_status(status)
		return ok({
			'id':task_id,
			'token':request.args[token]
		})
	else:
		return error('unmatched task and angel')	
