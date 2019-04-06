

from django.test import TestCase
from common.test import TestCaseWithInfo


class TestInfo(TestCaseWithInfo):
	def test_get_board(self):
		resp = self.client.get('/board',args={})
		print(resp)
#		self.assertEqual(resp.json()['status'],0)
