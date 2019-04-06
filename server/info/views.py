#

from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from common import ok,error


@require_GET 
def get_board(request,board_id):
	print(request)
	print(board_id)
	return ok()
