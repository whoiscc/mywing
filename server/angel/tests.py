from common.test import TestCaseWithAngel, Client
from .models import Angel


class TestAngel(TestCaseWithAngel):
    def test_get_info(self):
        resp = self.client.get('/angel', args={'id_list': [self.angel.id]})
        self.assertEqual(resp.json()['status'], 0)
        data = resp.json()['data']
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['nickname'], self.angel.nickname)


    def test_im_token(self):
        angel = Angel.create('something-central-key')
        angel.save()
        self.assertNotEqual(angel.im_token, '')
