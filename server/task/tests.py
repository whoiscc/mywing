from common.test import TestCaseWithTask, Client


class TestTask(TestCaseWithTask):
	def test_get_info(self):
		resp = self.client.get('/task',args={'id_list': [self.task.id]})
		print(resp.json())
		self.assertEqual(resp.json()['status'],0)
		data = resp.json()['data']
	
	
	def test_get_available(self):
		available_list_num=5
		resp = self.client.get('/task/available', args={'max':available_list_num,'reset':False})
		print(resp.json())
		self.assertEqual(resp.json()['status'],0)
		data = resp.json()['data']
		self.assertTrue(len(data),available_list_num)
		
