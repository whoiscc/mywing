#

import sys
import os

from django.db import models
from django.utils import timezone
from angel.models import Angel


class BoardItem(models.Model):
    board = models.ForeignKey('Board', on_delete=models.CASADE)
    update = models.ForeignKey('UpdateRecord', on_delete=models.PROTECT)
    angel = models.ForeignKey(Angel, on_delete=models.SET_DEFAULT)
    index = models.IntegerField()
    value = models.CharField(max_length=32)


class UpdateRecord(models.Model):
    time = models.DateTimeField(auto_now=True)


class Board(models.Model):
    name = models.CharField(max_length=32)
    update = models.ForeignKey(UpdateRecord, on_delete=models.PROTECT)


class News(models.Model):
    title = models.CharField(null=True,blank=True,max_length=64)
    author = models.CharField(null=True,blank=True,max_length=64)
    updated_at = models.DateTimeField(null=True,blank=True,editable=False)
    content = models.CharField(null=True,blank=True,max_length=128)

    def to_dict(self):
        return {
            'id':self.id,
            'title':self.title,
            'author':self.author,
            'updatedAt':self.updated_at,
        }
