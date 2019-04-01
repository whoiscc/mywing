from django.db import models

class Task(models.Model):
	description = models.CharField()
	dstLongitude = models.FloatField(editable=False)
	dstLatitude = models.FloatField(editable=False)
	srcLongitude = models.FloatField(editable=False)
	srcLatitude = models.FloatField(editable=False)
	cost = models.FloatField()
	distrbution = models.FloatField()
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
	helper = models.CharField(max_length=16,editable=False)
	createdAt = models.DateTimeField(editable=False)
	finishedAt = models.DateTimeField(editable=False)
	canceledAt = models.DateTimeField(editable=False)
	
	def to_dict(self):
		return{
			'id':self.id,
			'description':self.description,
			'cost':self.cost,
			'distrbution':self.distrbution,
			'status':self.status,
			'owner':self.owner,
		}	
