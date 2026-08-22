from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product, ProductCategory

def category_list(request):
    categories = ProductCategory.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})

def product_detail(request, product_id):
    """View for displaying product details."""
    product = get_object_or_404(Product, id=product_id)
    is_liked = (
        request.user.is_authenticated
        and product.likes.filter(id=request.user.id).exists()
    )
    return render(request, 'products/product_detail.html', {
        'product': product,
        'is_liked': is_liked,
    })

def product_list(request):
    """View for listing products with category filtering, search, and pagination."""
    categories = ProductCategory.objects.all().order_by('name')
    category_filter = request.GET.get('category')
    search_query = request.GET.get('q', '').strip()

    products = Product.objects.select_related('category').prefetch_related('likes')

    if category_filter:
        products = products.filter(category__slug=category_filter)

    if search_query:
        products = products.filter(
            Q(title__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(category__name__icontains=search_query)
        )

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    liked_product_ids = set()
    if request.user.is_authenticated:
        liked_product_ids = set(
            request.user.liked_products.values_list('id', flat=True)
        )

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category_filter,
        'search_query': search_query,
        'liked_product_ids': liked_product_ids,
    }

    return render(request, 'products/product_list.html', context)

@login_required
def like_product(request, product_id):
    """View for liking/unliking a product."""
    product = get_object_or_404(Product, id=product_id)

    if request.user in product.likes.all():
        product.likes.remove(request.user)  # Unlike the product
    else:
        product.likes.add(request.user)  # Like the product

    return redirect('product_detail', product_id=product.id)
