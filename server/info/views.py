#

from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from common import ok,error
from .models import Board


@require_GET 
def get_board(request,board_id):
	board=Board.objects.get(id=board_id)
	return ok(board.to_dict())
