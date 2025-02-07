from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if request.method == "POST":
        try:
            quantity = int(request.POST.get("quantity", 1))  # Get quantity, default to 1
            if quantity < 1:
                quantity = 1  # Prevent negative or zero quantity
        except ValueError:
            quantity = 1  # Default to 1 if invalid input

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

    return redirect('cart:view_cart')


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/view_cart.html', {'cart': cart})


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart:view_cart')


@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)  # Prevents errors
    cart_items = cart.items.all() # Get all items in the cart

    if cart_items.count() == 0:
        return redirect('cart:view_cart')  # Redirect if cart is empty

    return render(request, 'cart/checkout.html', {'cart': cart, 'cart_items': cart_items})
