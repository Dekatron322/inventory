from django.urls import path
from . import views

app_name = "product"

urlpatterns = [

	path("add-product/", views.AddProductView, name="add_product"),
	path("all-product/", views.AllProductView, name="all_product"),
	path("delete-product/<int:product_id>/", views.DeleteProductView, name="delete_product"),
	path("edit-product/<int:product_id>/", views.EditProductView, name="edit_product"),
	

]
