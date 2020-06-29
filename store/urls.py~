from django.urls import path
from . import views

app_name = "store"

urlpatterns = [

	path("add-store/", views.AddStoreView, name="add_store"),
	path("all-store/", views.AllStoreView, name="all_store"),
	path("delete-store/<int:store_id>/", views.DeleteStoreView, name="delete_store"),
	path("edit-store/<int:store_id>/", views.EditStoreView, name="edit_store"),
	

]
