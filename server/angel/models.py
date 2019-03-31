from django.db import models

import uuid


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
        except Angel.DoesNotExists:
            created = True
            angel = cls.create()

        item = LoginItem(angel=angel)
        item.expired_time = timezone.now() + datetime.timedelta(days=30)
        item.save()

        return angel, item, created

    @classmethod
    def create(cls):
        angel = cls(
            nickname='SuperAwesomeName',
            central_key=central_key,
            distribution=0.0,
            # TODO: get IM token
            im_token='unknown',
        )
        angel.save()
        return angel

class LoginItem(models.Model):
    angel = models.ForeignKey(Angel, on_delete=models.CASCADE, editable=False)
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    expired_time = models.DateTimeField(editable=False)
