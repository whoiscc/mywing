from django.db import models

import uuid


class Task(models.Model):
	description = models.CharField(max_length=128)
	dstLongitude = models.FloatField(null=True,blank=True,editable=False)
	dstLatitude = models.FloatField(null=True,blank=True,editable=False)
	srcLongitude = models.FloatField(null=True,blank=True,editable=False)
	srcLatitude = models.FloatField(null=True,blank=True,editable=False)
	cost = models.FloatField()
	distribution = models.FloatField(default=0)
	status_choices = (
		(0,"unpick"),	
		(1,"unfinish"),
		(2,"unconfirm"),
		(3,"confirm"),
		(-1,"unpick-cancel"),
		(-2,"pick-cancel"),
		(-3,"finish-cancel")
	)	
	status = models.IntegerField(choices=status_choices,default=-4)
	owner = models.CharField(max_length=16,editable=False)	
	helper = models.CharField(default='',blank=True,max_length=16,editable=False)
	createdAt = models.DateTimeField(editable=False)
	finishedAt = models.DateTimeField(null=True,blank=True,editable=False)
	canceledAt = models.DateTimeField(null=True,blank=True,editable=False)
	

	def to_dict(self):
		return{
			'id':self.id,
			'description':self.description,
			'cost':self.cost,
			'distribution':self.distribution,
			'status':self.status,
			'owner':self.owner,
			'helper':self.helper,
		}	

