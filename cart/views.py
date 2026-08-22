from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Cart, CartItem, Order, OrderItem
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
    cart_items = cart.items.select_related('product').all()
    return render(request, 'cart/view_cart.html', {
        'cart': cart,
        'cart_items': cart_items,
    })


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart:view_cart')


@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.select_related('product').all()

    if not cart_items:
        return redirect('cart:view_cart')

    return render(request, 'cart/checkout.html', {
        'cart': cart,
        'cart_items': cart_items,
    })


@login_required
def checkout_whatsapp(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.select_related('product').all()

    if not cart_items:
        return redirect('cart:view_cart')

    order = Order.objects.create(user=request.user)

    order_items = [
        OrderItem(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price_at_purchase=item.product.price,
        )
        for item in cart_items
    ]
    OrderItem.objects.bulk_create(order_items)

    cart_items.delete()

    phone = getattr(settings, 'WHATSAPP_ORDER_NUMBER', '')
    if not phone:
        phone = '256700000000'

    message = f"New order #{order.id} from {request.user.get_full_name() or request.user.username}%0A%0A"
    for item in order.items.all():
        message += f"- {item.product.title} x{item.quantity}: UGX {item.total_price()}%0A"
    message += f"%0ATotal: UGX {order.total()}"

    return redirect(f"https://wa.me/{phone}?text={message}")


@login_required
def my_orders(request):
    orders = request.user.orders.all().prefetch_related('items__product')
    return render(request, 'checkout/orders.html', {'orders': orders})
