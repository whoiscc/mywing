#

from common.test import TestCaseWithAngel, Client
from .models import Board, BoardItem, UpdateRecord, News
from django.utils import timezone


class TestInfo(TestCaseWithAngel):
    def setUp(self):
        super().setUp()
    
        updaterecord=UpdateRecord.objects.create(id=1)
        board=Board.objects.create(name='score_board',update=updaterecord)
        boarditem=BoardItem.objects.create(board=board, update=updaterecord,angel=self.angel, index=1, value='score')
        news=News.objects.create(id=2)

        self.board = board
        self.boarditem = boarditem
        self.news = news


    def teardown(self):
        self.board.delete()
        self.boarditem.delete()
        self.news.delete()
        del self.board
        del self.boarditem
        del self.news


    def test_get_board_without_id(self):
        resp = self.client.get('/info/board',args={'id_list':[self.board.id]})
        #print(resp.json())
        self.assertEqual(resp.json()['status'],0)


    def test_get_board_with_id(self):
        resp = self.client.get('/info/board/1',args={})
        #print(resp.json())
        self.assertEqual(resp.json()['status'],0)


    def test_get_news_without_id(self):
        resp = self.client.get('/info/news')
        self.assertEqual(resp.json()['status'],0)


    def test_get_news_with_id(self):
        resp = self.client.get('/info/news/2')
        self.assertEqual(resp.json()['status'],0)
        
