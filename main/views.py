import random
import string
from django.shortcuts import render
from customer.models import Customer
from product.models import Product
from purchase.models import Purchase
from store.models import Store
#more models import

# Create your views here.
def IndexView(request):
	customers = Customer.objects.all()
	products = Product.objects.all()
	stores = Store.objects.all()
	purchases = Purchase.objects.all()
	

	context = {"customers": customers, "products": products, "stores": stores, "purchases": purchases}
	return render(request, "main/index.html", context)
	
	
def AboutView(request):
	return render(request, "main/about.html")
	
	
def ray_randomizer(lettersCount, digitsCount):
	sampleStr = ' '.join((random.choice(string.ascii_letters) for i in range(lettersCount)))
	sampleStr += ' '.join((random.choice(string.digits) for i in range(digitsCount)))
	
	sampleList = list(sampleStr)
	random.shuffle(sampleList)
	result = ' '.join(sampleList)
	return result
	
	
def ray_randomiser(length=6):
	landd = string.ascii_letters + string.digits
	return ''.join((random.choice(landd) for i in range(length)))
	
	
