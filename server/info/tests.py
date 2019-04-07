#

from common.test import TestCaseWithAngel, Client
from .models import Board,News
from django.utils import timezone


class TestInfo(TestCaseWithAngel):
    def setUp(self):
        super().setUp()
    
        board=Board.objects.create(id=1,updatedAt=timezone.now())
        board.angel.add(self.angel)
        board.save()

        news=News.objects.create(id=2)

        self.board = board
        self.news = news


    def teardown(self):
        self.board.delete()
        self.news.delete()
        del self.board
        del self.news


    def test_get_board(self):
        resp = self.client.get('/info/board/1',args={})
        self.assertEqual(resp.json()['status'],0)


    def test_get_news_without_id(self):
        resp = self.client.get('/info/news')
        self.assertEqual(resp.json()['status'],0)


    def test_get_news_with_id(self):
        resp = self.client.get('/info/news/2')
        self.assertEqual(resp.json()['status'],0)
        
