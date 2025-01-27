from django.urls import path
from .views import product_list, product_detail, like_product, category_list

urlpatterns = [
    path('', product_list, name='product_list'),
    path('categories/', category_list, name='category_list'),  # Ensure this line exists

    path('<int:product_id>/', product_detail, name='product_detail'),
    path('<int:product_id>/like/', like_product, name='like_product'),
]

