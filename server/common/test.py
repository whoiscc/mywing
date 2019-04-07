#

from datetime import timedelta
from django.test import Client as TestClient, TestCase
from django.utils import timezone
from json import dumps
from angel.models import Angel, LoginItem
from task.models import Task
from info.models import Board,News


class Client:
    def __init__(self, testcase):
        super().__init__()
        self.token = testcase.token
        self.test_client = TestClient()

    def get(self, url, args=None):
        data = {**(args or {}), 'token': self.token}
        resp = self.test_client.get(
            url, data={'data': dumps(data)}, follow=True)
        return resp

    def post(self, url, args=None, **kwargs):
        resp = self.test_client.post(
            url, data={**(args or {}), 'token': self.token},
            content_type='application/json', follow=True,
        )
        return resp


class TestCaseWithAngel(TestCase):
    def setUp(self):
        super().setUp()
        angel = Angel.create('xjtu|cowsay123456')
        angel.nickname = 'Cowsay'
        angel.distribution = 16.0
        angel.save()
        self.angel = angel
        login_item = LoginItem(
            angel=angel,
            expired_time=timezone.now() + timedelta(days=30)
        )
        login_item.save()
        self.token = login_item.token.hex
        self.client = Client(self)

    def tearDown(self):
        self.angel.delete()
        del self.angel


class TestCaseWithTask(TestCaseWithAngel):
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


class TestCaseWithInfo(TestCaseWithAngel):
	def setUp(self):
		super().setUp()

		angel = Angel.create('xjtu|whoiscc123456')
		angel.nickname = 'whoiscc'
		angel.distribution = 26.0

		board=Board.objects.create(id=1,updatedAt=timezone.now())		
		board.angel.add(angel)
		board.save()

		news=News.objects.create(id=2)
		
		self.board = board
		self.news = news
	def teardown(self):
		self.board.delete()
		del self.board
