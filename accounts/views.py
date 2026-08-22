from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import RegisterForm, SuperUserRegisterForm, LoginForm
from .models import CustomUser
from products.models import Product, ProductCategory


def home_view(request):
    featured_products = Product.objects.select_related('category').order_by('-id')[:4]
    categories = ProductCategory.objects.filter(is_active=True)

    liked_product_ids = set()
    if request.user.is_authenticated:
        liked_product_ids = set(
            request.user.liked_products.values_list('id', flat=True)
        )

    return render(request, "home.html", {
        "featured_products": featured_products,
        "categories": categories,
        "liked_product_ids": liked_product_ids,
    })


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def superuser_register_view(request):
    if request.method == 'POST':
        form = SuperUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = True
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Superuser created successfully!")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SuperUserRegisterForm()

    return render(request, 'accounts/superuser_register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=identifier, password=password)
            if user:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')

            messages.error(request, "Invalid email/phone or password.")

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)  
    messages.success(request, "You have been logged out.")
    return redirect('login')  
