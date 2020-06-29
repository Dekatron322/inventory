from store.models import Store
from main.views import ray_randomiser
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Create your views here.
def AddStoreView(request):
	if request.method == "POST":
		name = request.POST.get("name")
		low_qty = request.POST.get("low_qty")
		high_qty = request.POST.get("high_qty")
		description = request.POST.get("description")
		store_id = ray_randomiser()
		pub_date = timezone.now()
		
		if name == "":
			return HttpResponse("Please enter a Store name")
		else:
			store = Store.objects.create(name=name, low_qty=low_qty, high_qty=high_qty, description=description, store_id=store_id, pub_date=pub_date)
			store.save()
			return HttpResponseRedirect(reverse("store:all_store"))
		
	else:
		return render(request, 'store/add_store.html')
		
	
def AllStoreView(request):
	stores = Store.objects.order_by("-pub_date")

	context = {"stores": stores}
	return render(request, "store/all_store.html", context)
	
	
	
def DeleteStoreView(request, store_id):
	store = Store.objects.get(id=store_id)
	store.delete()
	#post.save()
		
	return HttpResponseRedirect(reverse("store:all_store"))
	
	
def EditStoreView(request, store_id):
	if request.method == "POST":
		name = request.POST.get("name")
		low_qty = request.POST.get("low_qty")
		high_qty = request.POST.get("high_qty")
		description = request.POST.get("description")
		
		store = Store.objects.filter(id=store_id)
		store.update(name=name, low_qty=low_qty, high_qty=high_qty, description=description)

	
		return HttpResponseRedirect(reverse("store:all_store"))
		
		
	else:
		store = get_object_or_404(Store, id=store_id)
		context = {"store": store}
		return render(request, 'store/edit_store.html', context)
	
	
