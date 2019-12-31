from django.db import models

from django.utils import timezone

import datetime
import uuid
import requests
import hashlib
import base64

IM_APP_ID = 4623
IM_APP_SECRET = 'RXp5oqw7RG9kowVffbjkig3AlUHbOGCo'
IM_API_ROOT = 'https://api.gobelieve.io'
IM_AUTH_HEADER = {
    'Authorization': 'Basic ' + base64.b64encode(
        (
            str(IM_APP_ID) + ':' +
            hashlib.md5(IM_APP_SECRET.encode()).hexdigest()
        ).encode()
    ).decode(),
}


class Angel(models.Model):
    nickname = models.CharField(max_length=16)
    central_key = models.CharField(max_length=64, editable=False, unique=True)
    distribution = models.FloatField()
    im_token = models.CharField(max_length=64)

    def to_dict(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'distribution': self.distribution,

            'imToken': self.im_token,
        }

    @classmethod
    def login_and_optional_create(cls, central_key):
        created = False
        try:
            angel = cls.objects.get(central_key=central_key)
        except Angel.DoesNotExist:
            created = True
            angel = cls.create(central_key)

        item = LoginItem(angel=angel)
        item.expired_time = timezone.now() + datetime.timedelta(days=30)
        item.save()

        return angel, item, created

    @classmethod
    def create(cls, central_key):
        angel = cls(
            nickname='SuperAwesomeName',
            central_key=central_key,
            distribution=0.0,
            # im_token='unknown',
        )
        angel.save()
        resp = requests.post(IM_API_ROOT + '/auth/grant', json={
            'user_name': angel.nickname, 'uid': angel.id,
        }, headers=IM_AUTH_HEADER)
        if resp.status_code != 200:
            raise Exception('cannot get IM token for user')
        angel.im_token = resp.json()['data']['token']
        angel.save()
        return angel

class LoginItem(models.Model):
    angel = models.ForeignKey(Angel, on_delete=models.CASCADE, editable=False)
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    expired_time = models.DateTimeField(editable=False)
