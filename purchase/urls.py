from django.urls import path
from . import views

app_name = "purchase"

urlpatterns = [

	path("add-purchase/", views.AddPurchaseView, name="add_purchase"),
	path("all-purchase/", views.AllPurchaseView, name="all_purchase"),
	path("delete-purchase/<int:purchase_id>/", views.DeletePurchaseView, name="delete_purchase"),
	path("view-purchase/<int:purchase_id>/", views.ViewPurchaseView, name="view_purchase"),
	

]
