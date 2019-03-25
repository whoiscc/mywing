from django.db impport models

class Task(models.Model):
	description = models.CharField()
	dstLongitude = model.FloatField(editable=False)//not nesscessary
	dstLatitude = model.FloatField(editable=False)//not nesscessary
	srcLongitude = model.FloatField(editable=False)//not nesscessary
	srcLatitude = model.FloatField(editable=False)//not nesscessary
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
	}
	status = models.IntegerField(choices=status_choices,default=-4)
	owner = models.CharField(max_length=16,editable=False)	
	helper = models.CharField(max_length=16,editable=False)//un nec
	createdAt = models.DateTimeField(editable=False)//un nec
	finishedAt = model.DateTimeField(editable=False)//un nec
	canceledAt = model.DateTimeField(editable=False)//un nec
	
	def to_dict(self):
		return{
			'id':self.id,
			'description':self.description,
			'cost':self.cost,
			'distrbution':self.distrbution,
			'status':self.status,
			'owner':self.owner,
		}	
