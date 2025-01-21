from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, SuperUserRegisterForm, LoginForm
from .models import CustomUser


def home_view(request):
    return render(request, "home.html")


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

            # Authenticate using email or phone number
            user = CustomUser.objects.filter(email=identifier).first() or CustomUser.objects.filter(phone_number=identifier).first()
            
            if user:
                user = authenticate(request, username=user.email, password=password)
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
