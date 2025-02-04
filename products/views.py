from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Product, ProductCategory

def category_list(request):
    categories = ProductCategory.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})

def product_detail(request, product_id):
    """View for displaying product details."""
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def product_list(request):
    """View for listing products with category filtering and pagination."""
    categories = ProductCategory.objects.all()
    category_filter = request.GET.get('category')

    # Filter products by category if selected
    products = Product.objects.all()
    if category_filter:
        products = products.filter(category__slug=category_filter)

    # Apply pagination (10 products per page)
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/product_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category_filter,
    })

@login_required
def like_product(request, product_id):
    """View for liking/unliking a product."""
    product = get_object_or_404(Product, id=product_id)

    if request.user in product.likes.all():
        product.likes.remove(request.user)  # Unlike the product
    else:
        product.likes.add(request.user)  # Like the product

    return redirect('product_detail', product_id=product.id)
