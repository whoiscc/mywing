#

import sys
import os

from django.db import models
from django.utils import timezone

o_path = os.getcwd()

sys.path.append(o_path)
from angel.models import Angel


class Info(models.Model):
	angel = models.ManyToManyField(Angel, null=True, blank=True, symmetrical=True)
	title = models.CharField(null=True,blank=True,max_length=64)
	author = models.CharField(null=True,blank=True,max_length=64)
	updateAt = models.DateTimeField(null=True,blank=True,editable=False)
	content = models.CharField(null=True,blank=True,max_length=128)
	value=0

	def to_dict(self):
		return {
			'angel':[{'id':angel.id,'nickname':angel.nickname,'value':self.value} for angel in self.angel_set.all()],
			'updateAt':self.updateAt,
		}
	
