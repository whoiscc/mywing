#

from django.utils import timezone
from common.test import TestCaseWithAngel, Client
from .models import Task


class TestTask(TestCaseWithAngel):
    def setUp(self):
        super().setUp()
        task = Task(
            description='this is a kuaidi',
            cost=2.0,
            distribution=1.0,
            status=0,
            createdAt=timezone.now(),
        )
        task.save()
        self.task = task

    def tearDown(self):
        self.task.delete()
        del self.task

    def test_get_info(self):
        resp = self.client.get('/task',args={'id_list': [self.task.id]})
        self.assertEqual(resp.json()['status'],0)
        data = resp.json()['data']


    def test_get_available(self):
        available_list_num=1
        resp = self.client.get('/task/available', args={'max':available_list_num,'reset':False})
        self.assertEqual(resp.json()['status'],0)
        data = resp.json()['data']
        self.assertTrue(len(data)<=available_list_num)


    def test_post_create(self):
        resp = self.client.post('/task/create',args={'description':'this is a waimai','cost':3.0,'distribution':2.5,'createdAt':timezone.now()})
        self.assertEqual(resp.json()['status'],0)
        data = resp.json()['data']


    def test_post_accept(self):
        resp = self.client.post('/task/accept',args={'id':self.task.id,'distribution':1})
        self.assertEqual(resp.json()['status'],0)


    def test_post_finish(self):
        self.task.status=1
        self.task.helper=self.angel.id
        self.task.save()
        resp = self.client.post('/task/finish',args={'id':self.task.id})
        self.assertEqual(resp.json()['status'],0)


    def test_post_confirm(self):
        self.task.status=2
        self.task.owner=self.angel.id
        self.task.save()
        resp = self.client.post('/task/confirm',args={'id':self.task.id})
        self.assertEqual(resp.json()['status'],0)


    def test_post_confirm_failure(self):
        self.task.status=2
        self.task.owner=self.angel.id+1
        self.task.save()
        resp = self.client.post('/task/confirm',args={'id':self.task.id})
        self.assertEqual(resp.json()['status'],1)


    def test_post_cancel(self):
        self.task.status=2
        self.task.owner=self.angel.id
        self.task.save()
        resp = self.client.post('/task/cancel',args={'id':self.task.id})
        self.assertEqual(resp.json()['status'],0)


    def test_get_self(self):
        self.task.status=1
        self.task.owner=self.angel.id
        self.task.save()
        resp = self.client.get('/task/self',args={'inProgress':True})
        self.assertEqual(resp.json()['status'],0)
        # print(resp)
