#

import sys
import os

from django.db import models
from django.utils import timezone

o_path = os.getcwd()

sys.path.append(o_path)
from angel.models import Angel


class Board(models.Model):
	angel = models.ManyToManyField(Angel, blank=True, symmetrical=True)
	updatedAt = models.DateTimeField(null=True,blank=True,editable=False)
	value = 0

	def to_dict(self):
		return {
			'angel':[{'id':angel.id,'nickname':angel.nickname,'value':self.value} for angel in self.angel.all()],
			'updatedAt':self.updatedAt,
		}
	

class News(models.Model):
	title = models.CharField(null=True,blank=True,max_length=64)
	author = models.CharField(null=True,blank=True,max_length=64)
	updatedAt = models.DateTimeField(null=True,blank=True,editable=False)
	content = models.CharField(null=True,blank=True,max_length=128)
	
	def to_dict(self):
		return {
			'id':self.id,
			'title':self.title,
			'author':self.author,
			'updatedAt':self.updatedAt,
		}
