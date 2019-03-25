from django.views.generic import TemplateView

import datetime
import time

from common import ok,error,extract,get_object,get_objects_with_id_list
from .models import Task
from random import sample

class TaskView(TemplateView)

@require_POST
def create(request):
	owner_id=get_current_angel_method()//undefined
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
def get_task_available(request,unselect_task_id=extract(request,'id_list')):
	if request.args[reset]:
		unselect_task_id=extract(request,'id_list')
	available_task_id=[]
	if len(unselect_task_id)<request.args[max]:
		available_task_id=unselect_task_id	
	else:
		available_task_id=sample(unselect_task_id,request.args[max])
	for task_id in available_task_id:
		unselect_task_id.remove(task_id)
	return [get_object(Task,id).to_dict() for id in available_id]	

@require_GET
def get_self_task(request)
	angel_id=get_current_angel_method()
	involve_task=[]
	for task_id in extract,'id_list'):
		task=get_object(Task,task_id)
		if task.owner==angel_id or task.helper==angel_id:
		if !request.args[inProgress] or task.status==0 or task.status==1 or task.status==2:
			involve_task.append(task)
	return [task.to_dict() for task in involve_task]
 
@require_GET
def get_task(request):
	return get_objects_with_id_list(Task, request)

def change_task_status(request,status,from_owner_or_helper)
	task_id=request.args[id]
	task=get_object(Task,task_id)
	checked_angel=from_owner_or_helper=='owner'?task.owner:task.helper
	if checked_angel==get_current_angel_method()
		task.set_status(status)
		return ok({
			'id':task_id,
			'token':request.args[token],
		}
	else 
		return error('unmatched task and angel')	
