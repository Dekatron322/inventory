from django.db import models
from customer.models import Customer
from product.models import Product, SoldProduct
from django.utils import timezone

# Create your models here.
class Purchase(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="")
	products = models.ManyToManyField(SoldProduct, through="PurchaseProductConnector", through_fields=("purchase", "product"),)
	total_price = models.IntegerField(blank=True, null=True)
	total_products = models.IntegerField(blank=True, null=True)
	purchase_id = models.CharField(max_length=150)
	pub_date = models.DateTimeField(default=timezone.now)
	
	
	def __str__(self):
		return self.customer.name
	
	
class PurchaseProductConnector(models.Model):
	purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, default="")
	product = models.ForeignKey(SoldProduct, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)

