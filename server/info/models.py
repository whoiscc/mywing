#

import sys
import os

from django.db import models
from django.utils import timezone
from angel.models import Angel


class BoardItem(models.Model):
    board = models.ForeignKey('Board', on_delete=models.CASCADE)
    update = models.ForeignKey('UpdateRecord', on_delete=models.PROTECT)
    angel = models.ForeignKey(Angel, on_delete=models.DO_NOTHING)
    index = models.IntegerField()
    value = models.CharField(max_length=32)

    def to_dict(self):
        return {
            'update':self.update.time,
            'angel':self.angel.nickname,
            'index':self.index,
            'value':self.value
        }


class UpdateRecord(models.Model):
    time = models.DateTimeField(auto_now=True)


class Board(models.Model):
    name = models.CharField(max_length=32, default='')
    update = models.ForeignKey(UpdateRecord, on_delete=models.PROTECT, default='')
    
    def to_dict(self):
        return {
            'name':self.name,
            'update':self.update.time,
            'boarditems':[item.to_dict() for item in self.boarditem_set.all().order_by('index')]
        }


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
