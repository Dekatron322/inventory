from django.shortcuts import render
from product.models import Product, SoldProduct
from purchase.models import Purchase
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def AccountView(request):
	if request.method == "POST":
		pass
		
	else:
		products = Product.objects.all()
		sold_products = SoldProduct.objects.all()
		tcost_price = 0
		tselling_price = 0
		for product in sold_products:
			tcost_price += product.cost_price
			tselling_price += product.selling_price

		tprofit =  tselling_price - tcost_price
		#return HttpResponse(tprofit)
		
		context = {"sold_products": sold_products, "products": products, "tcost_price": tcost_price, "tselling_price": tselling_price, "tprofit": tprofit}
		return render(request, 'account/account.html', context)
