#

from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from common import ok,error,get_objects_with_id_list
from .models import BoardItem, Board, News
from json import dumps


@require_GET 
def get_board(request,board_id):
    if board_id=='' and 'id_list' not in request.args.keys():
        return ok([board.to_dict() for board in Board.objects.all()])
    elif board_id=='':
        return get_objects_with_id_list(Board, request)
    else:
        return ok(Board.objects.get(id=board_id).to_dict())


@require_GET
def get_news(request,news_id):
    if news_id=='' and 'id_list' not in request.args.keys():
        return ok([news.to_dict() for news in News.objects.all()])
    elif news_id=='':
        return get_objects_with_id_list(News, request)
    else:
        return ok(News.objects.get(id=news_id).to_dict())
