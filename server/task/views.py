from django.views.generic import TemplateView

import datetime
import time
import sys
import os

from django.views.decorators.http import require_GET, require_POST
from common import ok,error,extract,get_object,get_objects_with_id_list
from .models import Task
from random import sample

# o_path = os.getcwd()
#
# sys.path.append(o_path)
from angel import views


@require_POST
def create(request):
    owner_id=request.angel.id
    task = Task(
        owner=owner_id,
        description=request.args['description'],
        cost=request.args['cost'],
        distribution=request.args['distribution'],
        status=0,
        createdAt=request.args['createdAt'],
    )
    task.save()
    return ok(task.to_dict())


@require_POST
def accept(request):
    task=get_object(Task,request.args['id'])
    if task.status!=0:
        return error('task cannot be accepted')
    task.helper=request.angel.id
    task.save()
    task.distribution=request.args['distribution']
    return _change_task_status(request,1,'helper')


@require_POST
def finish(request):
    return _change_task_status(request,2,'helper')


@require_POST
def confirm(request):
    return _change_task_status(request,3,'owner')


@require_POST
def cancel(request):
    cancel_status_dict={
        0: -1,
        1: -2,
        2: -3,
        }
    next_status=cancel_status_dict[Task.objects.get(pk=request.args['id']).status]
    _change_task_status(request,next_status,'owner')
    return ok()


@require_GET
def get_task_available(request):
    list_num=int(request.args['max'])
    task_list=Task.objects.all()
    if len(task_list)<list_num:
        return error('exceeded request number')
    else:
        return ok([task.to_dict() for task in task_list][:list_num])


@require_GET
def get_self_task(request):
    angel = request.angel.id
    involve_task=[]
    for task in Task.objects.all():
        if task.owner==angel or task.helper==angel:
            if request.args['inProgress']==false or task.status in [0, 1, 2]:
                involve_task.append(task)
    return ok([task.to_dict() for task in involve_task])


@require_GET
def get_task(request):
    return get_objects_with_id_list(Task, request)


def _change_task_status(request,status,from_owner_or_helper):
    task_id=request.args['id']
    task=get_object(Task,task_id)
    if task.status!=status-1:
        return error('task is not in right status')
    angel=request.angel
    if from_owner_or_helper=='owner':
        if task.owner=='':
            return error('owner undesignated')
        elif int(task.owner)!=angel.id:
            return error('unmatched task_owner and angel')
    elif from_owner_or_helper=='helper':
        if task.helper=='':
            return error('helper undesignated')
        elif int(task.helper)!=angel.id:
            return error('unmatched task_helper and angel')
    else:
        return error('neither helper nor owner')
    task.status=status
    task.save()
    return ok({
        'id':task_id,
        'token':request.args['token']
    })
