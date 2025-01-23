# from django.urls import path
# from .views import register_view, superuser_register_view, login_view, logout_view
# from django.contrib.auth.views import LogoutView

# urlpatterns = [
    
#     path('register/', register_view, name='register'),
#     path('superuser-register/', superuser_register_view, name='superuser_register'),
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout')
]