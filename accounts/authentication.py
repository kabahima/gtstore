from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        if '@' in username:  # Login with email (for superusers)
            user = CustomUser.objects.filter(email=username).first()
        else:  # Login with phone number (for regular users)
            user = CustomUser.objects.filter(phone_number=username).first()

        if user and user.check_password(password):
            return user
        return None
