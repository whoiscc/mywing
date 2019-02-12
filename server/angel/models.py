from django.db import models

import uuid


class Angel(models.Model):
    nickname = models.CharField(max_length=16)
    central_key = models.CharField(max_length=64, editable=False, unique=True)
    distribution = models.FloatField()

    def to_dict(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'distribution': self.distribution,
        }


class LoginItem(models.Model):
    angel = models.ForeignKey(Angel, on_delete=models.CASCADE, editable=False)
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    expired_time = models.DateTimeField(editable=False)
