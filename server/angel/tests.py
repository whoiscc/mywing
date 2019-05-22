from common.test import TestCaseWithAngel, Client


class TestAngel(TestCaseWithAngel):
    def test_get_info(self):
        resp = self.client.get('/angel', args={'id_list': [self.angel.id]})
        self.assertEqual(resp.json()['status'], 0)
        data = resp.json()['data']
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['nickname'], self.angel.nickname)
<<<<<<< HEAD

    def test_im_token(self):
        self.assertNotEqual(self.angel.im_token, '')
=======
>>>>>>> e73af38a444d573d4f09c4f2f2a0bed14cd671b7
