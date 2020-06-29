from django.shortcuts import render
from customer.models import Customer

# Create your views here.
def AddCustomerView(request):
	pass
	
	
def AllCustomerView(request):
	customers = Customer.objects.order_by("-pub_date")

	context = {"customers": customers}
	return render(request, "customer/all_customer.html", context)
	
	
def DeleteCustomerView(request):
	pass
	
def EditCustomerView(request):
	pass
	
	
