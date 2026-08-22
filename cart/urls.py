from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart, checkout, checkout_whatsapp, my_orders

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view/', view_cart, name='view_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('checkout/whatsapp/', checkout_whatsapp, name='checkout_whatsapp'),
    path('orders/', my_orders, name='my_orders'),
]
