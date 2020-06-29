from purchase.models import Purchase, PurchaseProductConnector
from customer.models import Customer
from product.models import Product, SoldProduct
from main.views import ray_randomiser
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy


# Create your views here.
def AddPurchaseView(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		phone = request.POST.get("phone")
		products = request.POST.get("products")
		pub_date = timezone.now()
		
		if (name == ""):
			return HttpResponse("Error with 'name' field, (Please appropriately fill up all fields)")
		elif  (email == ""):
			return HttpResponse("Error with 'email' field, (Please appropriately fill up all fields)")
		elif  (phone == ""):
			return HttpResponse("Error with 'phone' field, (Please appropriately fill up all fields)")
		elif  (products == ""):
			return HttpResponse("Error with 'product' field, (Please appropriately fill up all fields)")
		
		else: 
		
			try:
				for item in products.split(","):
					if get_object_or_404(Product, product_id=item):
						pass
			

				customer = Customer.objects.create(name=name, email=email, phone=phone, pub_date=pub_date)
				customer.save()

				purchase_id = ray_randomiser()
				purchase = Purchase.objects.create(customer=customer,purchase_id=purchase_id, pub_date=pub_date)
				purchase.save()
		
				product_list = [] #the one to work with 
				product_list2 = [] #the one to delete
				total_price = 0
				total_products = 0
		
				products = "%s" % (products)
			
				#products = str(products)
				#products =  products.split(",")
		
				#return HttpResponse((products))
				for item in products.split(","):
				#for item in products:
					product = get_object_or_404(Product, product_id=item)
					sold_product = SoldProduct.objects.create(name=product.name, cost_price=product.cost_price, 
					selling_price=product.selling_price, expiry_date=product.expiry_date, product_id=product.product_id,
					pub_date=product.pub_date)
					total_price += product.selling_price
					total_products += 1
					product_list.append(sold_product)
					product_list2.append(product)
			
					#return HttpResponse(str(product))
					#pc = PurchaseProductConnector(purchase=purchase, product=product, pub_date=pub_date)
					#pc.save()

		
				purchase.total_price = total_price
				purchase.total_products = total_products
				purchase.save()
		
				for product in product_list:
					pc = PurchaseProductConnector(purchase=purchase, product=product, pub_date=pub_date)
					pc.save()
		
				#return HttpResponse(str(product_list))
				for product in product_list2:
					pr = Product.objects.get(id=product.id)
					pr.delete()


				return HttpResponseRedirect(reverse("purchase:all_purchase"))
				
			except:
					return HttpResponse("Error with 'products' field, (Incorrect Product id)")
	else:
		return render(request, 'purchase/add_purchase.html')
		
	
def AllPurchaseView(request):
	purchases = Purchase.objects.order_by("-pub_date")

	context = {"purchases": purchases}
	return render(request, "purchase/all_purchase.html", context)
	
	
	
def DeletePurchaseView(request, purchase_id):
	purchase = Purchase.objects.get(id=purchase_id)
	purchase.delete()
	#post.save()
		
	return HttpResponseRedirect(reverse("purchase:all_purchase"))
	
	
def ViewPurchaseView(request, purchase_id):
	if request.method == "POST":
		pass
	
	else:
		purchase = get_object_or_404(Purchase, id=purchase_id)
		products = purchase.products.all()
		#return HttpResponse(products)
		context = {"purchase": purchase, "products": products}
		return render(request, 'purchase/view_purchase.html', context)
	
	
