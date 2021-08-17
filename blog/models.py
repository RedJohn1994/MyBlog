from django.db import models


class Post(models.Model):
	image = models.ImageField(upload_to='event_images/')
	text = models.CharField(max_length=300)
	title = models.CharField(max_length=300)
	date = models.DateTimeField()




# Create your models here.
