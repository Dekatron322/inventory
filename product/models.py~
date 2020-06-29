from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=150)
	cost_price = models.IntegerField(blank=False)
	selling_price = models.IntegerField(blank=True, null=True)
	expiry_date = models.CharField(max_length=150)
	product_id = models.CharField(max_length=150)
	pub_date = models.DateTimeField(default=timezone.now)
	
	
	def __str__(self):
		return self.name
		
		
# Create your models here.
class SoldProduct(models.Model):
	name = models.CharField(max_length=150)
	cost_price = models.IntegerField(blank=True, null=True)
	selling_price = models.IntegerField(blank=True, null=True)
	expiry_date = models.CharField(max_length=150)
	product_id = models.CharField(max_length=150)
	pub_date = models.DateTimeField(default=timezone.now)
	
	
	def __str__(self):
		return self.name
