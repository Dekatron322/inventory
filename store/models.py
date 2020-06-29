from django.db import models
from product.models import Product
from django.utils import timezone

# Create your models here.
class Store(models.Model):
	name = models.CharField(max_length=150)
	products = models.ManyToManyField(Product, through="StoreProductConnector", through_fields=("store", "product"),)
	low_qty = models.IntegerField(blank=True, null=True)
	high_qty = models.IntegerField(blank=True, null=True)
	description = models.TextField(default="just a store")
	store_id  = models.CharField(max_length=150)
	pub_date = models.DateTimeField(default=timezone.now)
	
	
	def __str__(self):
		return self.name
	
	
	
class StoreProductConnector(models.Model):
	store = models.ForeignKey(Store, on_delete=models.CASCADE, default="")
	product = models.ForeignKey(Product, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)

