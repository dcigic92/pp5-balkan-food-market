from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('rate_product/<int:product_id>/', views.rate_product, name='rate_product'),
    path('remove_rating/<int:product_id>/', views.remove_rating, name='remove_rating'),
]