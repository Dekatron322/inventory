from product.models import Product
from store.models import Store, StoreProductConnector
from main.views import ray_randomiser
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Create your views here.
def AddProductView(request):
	if request.method == "POST":
		name = request.POST.get("name")
		cost_price = request.POST.get("cost_price")
		selling_price = request.POST.get("selling_price")
		expiry_date = request.POST.get("expiry_date")
		store_id = request.POST.get("store")
		product_id = ray_randomiser()
		pub_date = timezone.now()
		#return HttpResponse(expiry_date)
		
		if (name == ""):
			return HttpResponse("Error with 'name' field, (Please appropriately fill up all fields)")
		elif  (expiry_date == ""):
			return HttpResponse("Error with 'expiry_date' field, (Please appropriately fill up all fields)")
			
		else: 
			#return HttpResponse(expiry_date) 2020-06-09
		
			product = Product.objects.create(name=name, cost_price=cost_price, selling_price=selling_price, expiry_date=expiry_date, product_id=product_id, pub_date=pub_date)
			product.save()
			
		if store_id == "none":
			pass
			
		else:
			store = get_object_or_404(Store, id=store_id)
			st = StoreProductConnector(store=store, product=product, pub_date=pub_date)
			st.save()
		return HttpResponseRedirect(reverse("product:all_product"))
		
	else:
		stores = Store.objects.order_by("-pub_date")
		context = {"stores": stores}
		return render(request, 'product/add_product.html', context)
		
	
def AllProductView(request):
	#return HttpResponse(timezone.now())
	today_date = str(timezone.now())
	today_date = today_date[0:10]
	products = Product.objects.order_by("-pub_date")

	context = {"products": products, "today_date": today_date}
	return render(request, "product/all_product.html", context)
	
	
	
def DeleteProductView(request, product_id):
	product = Product.objects.get(id=product_id)
	product.delete()
	#post.save()
		
	return HttpResponseRedirect(reverse("product:all_product"))
	
def EditProductView(request, product_id):
	
	if request.method == "POST":
		name = request.POST.get("name")
		cost_price = request.POST.get("cost_price")
		selling_price = request.POST.get("selling_price")
		expiry_date = request.POST.get("expiry_date")
		
		
		
		product = Product.objects.filter(id=product_id)
		product.update(name=name, cost_price=cost_price, selling_price=selling_price, expiry_date=expiry_date)
		#product.save()
		
		return HttpResponseRedirect(reverse("product:all_product"))
		
		
	else:
		product = get_object_or_404(Product, id=product_id)
		context = {"product": product}
		#expiry_date = product.expiry_date
		#return HttpResponse(expiry_date)
		return render(request, 'product/edit_product.html', context)
	
	
