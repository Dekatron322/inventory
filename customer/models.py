from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=150)
	email = models.CharField(max_length=150)
	phone = models.CharField(max_length=150)
	pub_date = models.DateTimeField(default=timezone.now)
	
	
	def __str__(self):
		return self.name
	
