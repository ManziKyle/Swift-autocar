from django.db import models

# Create your models here.

class Repair(models.Model):
	title = models.CharField(max_length=100)
	discription = models.TextField()
	slug = models.SlugField(unique=True)


	def __str__(self):
		return self.title


class Maintenane(models.Model):
	name = models.CharField(max_length=100 ,null=False,blank=False)
	desc = models.TextField(null=False)
	image = models.ImageField()

	def __str__(self):
		return self.name
	