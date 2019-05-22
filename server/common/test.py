#
from datetime import timedelta
from django.test import Client as TestClient, TestCase
from django.utils import timezone
from json import dumps
from angel.models import Angel, LoginItem


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
<<<<<<< HEAD
        angel = Angel.create('xjtu|cowsay123456')
        angel.nickname = 'Cowsay'
        angel.distribution = 16.0
=======
        angel = Angel(
            nickname='Cowsay',
            central_key='xjtu|cowsay123456',
            distribution=16.0
        )
>>>>>>> e73af38a444d573d4f09c4f2f2a0bed14cd671b7
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
