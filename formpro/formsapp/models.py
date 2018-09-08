from django.db import models

class formdata(models.Model):
	usrname=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	
