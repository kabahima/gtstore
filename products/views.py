# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Product, ProductCategory

from django.shortcuts import render



def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def product_list(request):
    # Get all categories to pass to the template for filtering
    categories = ProductCategory.objects.all()
    
    # Get the category filter from the request, if any
    category_filter = request.GET.get('category', '')
    
    if category_filter:
        products = Product.objects.filter(category__name=category_filter)  # Filter by category
    else:
        products = Product.objects.all()  # Get all products if no filter is applied
    
    # Apply pagination
    paginator = Paginator(products, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'products/product_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category_filter,
    })

@login_required
def like_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)  # Unlike the product
    else:
        product.likes.add(request.user)  # Like the product
    return redirect('product_detail', product_id=product.id)
