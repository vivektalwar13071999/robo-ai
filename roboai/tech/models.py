from __future__ import unicode_literals
from django.db import models
from django.utils import timezone





class general(models.Model):

	author1 = models.CharField(max_length = 100)
	title1 = models.CharField(max_length = 300)
	text1 = models.TextField()
	image1 = models.FileField()

	


	def __str__(self):
		return self.title1


class robotics(models.Model):

	author2 = models.CharField(max_length = 100)
	title2 = models.CharField(max_length = 300)
	text2 = models.TextField()
	image2 = models.FileField()


	

	def __str__(self):
		return self.title2

class embedded(models.Model):

	author3 = models.CharField(max_length = 100)
	title3 = models.CharField(max_length = 300)
	text3 = models.TextField()
	image3 = models.FileField()

	

	def __str__(self):
		return self.title3

class machine(models.Model):

	author4 = models.CharField(max_length = 100)
	title4 = models.CharField(max_length = 300)
	text4 = models.TextField()
	image4 = models.FileField()
	
	
	


	def __str__(self):
		return self.title4

class imagepro(models.Model):

	author5 = models.CharField(max_length = 100)
	title5 = models.CharField(max_length = 300)
	text5 = models.TextField()
	image5 = models.FileField()

	
	

	def __str__(self):
		return self.title5





