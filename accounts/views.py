from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, SuperUserRegisterForm, LoginForm
from .models import CustomUser
# from django.urls import reverse



def home_view(request):
    return render(request, "home.html")

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
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
            return redirect('login')
    else:
        form = SuperUserRegisterForm()
    return render(request, 'accounts/superuser_register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)  # This will log the user out
    return redirect('login')  # Redirect to the login page after logging out