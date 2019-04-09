#

from common.test import TestCaseWithAngel, Client
from .models import Board,Score,News
from django.utils import timezone


class TestInfo(TestCaseWithAngel):
    def setUp(self):
        super().setUp()
    
        board=Board.objects.create(id=1,updatedAt=timezone.now())
        score=Score.objects.create(board=board,angel=self.angel)
        news=News.objects.create(id=2)

        self.board = board
        self.score = score
        self.news = news


    def teardown(self):
        self.board.delete()
        self.score.delete()
        self.news.delete()
        del self.board
        del self.score
        del self.news


    def test_get_board_without_id(self):
        resp = self.client.get('/info/board',args={'id_list':[self.board.id]})
        self.assertEqual(resp.json()['status'],0)


    def test_get_board_with_id(self):
        resp = self.client.get('/info/board/1',args={})
        self.assertEqual(resp.json()['status'],0)


    def test_get_news_without_id(self):
        resp = self.client.get('/info/news')
        self.assertEqual(resp.json()['status'],0)


    def test_get_news_with_id(self):
        resp = self.client.get('/info/news/2')
        self.assertEqual(resp.json()['status'],0)
        
