#

from common.test import TestCaseWithTask, Client
from django.utils import timezone


class TestTask(TestCaseWithTask):
	def test_get_info(self):
		resp = self.client.get('/task',args={'id_list': [self.task.id]})
		self.assertEqual(resp.json()['status'],0)
		data = resp.json()['data']
	
	
	def test_get_available(self):
		available_list_num=5
		resp = self.client.get('/task/available', args={'maxNum':available_list_num,'reset':False})	
		self.assertEqual(resp.json()['status'],0)
		data = resp.json()['data']
		self.assertTrue(len(data),available_list_num)
		

	def test_post_create(self):
		resp = self.client.post('/task/create',args={'description':'this is a waimai','cost':3.0,'distribution':2.5,'createdAt':timezone.now()})
		self.assertEqual(resp.json()['status'],0)
		data = resp.json()['data']

	
	def test_post_accept(self):
		resp = self.client.post('/task/accept',args={'id':self.task.id,'distribution':1})
		self.assertEqual(resp.json()['status'],0)


	def test_post_confirm(self):
		resp = self.client.post('/task/confirm',args={'id':self.task.id})
		self.assertEqual(resp.json()['status'],0)
