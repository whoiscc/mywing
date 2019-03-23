from django.db impport models

class Task(models.Model):
	id = models.CharField(max_length=16,unique=True,editable=False)
	description = models.CharField()
	dstLongitude = model.FloatField(editable=False)//not nesscessary
	dstLatitude = model.FloatField(editable=False)//not nesscessary
	srcLongitude = model.FloatField(editable=False)//not nesscessary
	srcLatitude = model.FloatField(editable=False)//not nesscessary
	cost = models.FloatField()
	distrbution = models.FloatField()
	status = dict{
		unpick:0,
		unfinish:1,
		unconfirm:2,
		confirm:3,
		unpick-cancel:-1,
		pick-cancel:-2,
		finish-cancel:-3,
		default:-4
	}
	owner = models.CharField(max_length=16,editable=False)	
	helper = models.CharField(max_length=16,editable=False)//un nec
	createdAt = models.DateTimeField(editable=False)//un nec
	finishedAt = model.DateTimeField(editable=False)//un nec
	canceledAt = model.DateTimeField(editable=False)//un nec
	
