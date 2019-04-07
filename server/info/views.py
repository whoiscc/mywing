#

from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from common import ok,error
from .models import Board,News


@require_GET 
def get_board(request,board_id=None):
	board=Board.objects.get(id=board_id)
	return ok(board.to_dict())


@require_GET
def get_news(request,news_id):
	if(news_id==''):
		return ok([news.to_dict() for news in News.objects.all()])
	else:
		return ok(News.objects.get(id=news_id).to_dict())
