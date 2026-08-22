from django.contrib.auth.backends import ModelBackend
from .models import CustomUser


class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None

        username = username.strip()

        if '@' in username:
            user = CustomUser.objects.filter(email__iexact=username).first()
        else:
            user = CustomUser.objects.filter(phone_number=username).first()

        if user and user.check_password(password):
            return user
        return None
