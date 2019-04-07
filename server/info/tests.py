#

from common.test import TestCaseWithInfo, Client


class TestInfo(TestCaseWithInfo):
	def test_get_board(self):
		resp = self.client.get('/info/board/1',args={})
		self.assertEqual(resp.json()['status'],0)


	def test_get_news_without_id(self):
		resp = self.client.get('/info/news')
		self.assertEqual(resp.json()['status'],0)


	def test_get_news_with_id(self):
		resp = self.client.get('/info/news/2')
		self.assertEqual(resp.json()['status'],0)
		
