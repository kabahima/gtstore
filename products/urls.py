from django.urls import path
from . import views

urlpatterns = [
    # List of products
    path('', views.product_list, name='product_list'),
    

    # Product detail page
    path('<int:product_id>/', views.product_detail, name='product_detail'),

    # Like a product
    path('<int:product_id>/like/', views.like_product, name='like_product'),
]
