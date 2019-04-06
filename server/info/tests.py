#

from common.test import TestCaseWithInfo, Client


class TestInfo(TestCaseWithInfo):
	def test_get_board(self):
		resp = self.client.get('/info/board/1',args={})
		self.assertEqual(resp.json()['status'],0)
