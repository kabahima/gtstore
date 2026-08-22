from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        if '@' in username:
            username = username.strip()
            return self.get(email__iexact=username)
        return self.get(phone_number=username)

    def create_user(self, email=None, phone_number=None, password=None, whatsapp_number=None, **extra_fields):
        if not email and not phone_number:
            raise ValueError("Either Email or Phone Number must be set")

        email = self.normalize_email(email) if email else None

        if extra_fields.get('is_superuser') and not whatsapp_number:
            raise ValueError("Superusers must have a WhatsApp number")

        user = self.model(
            email=email,
            phone_number=phone_number,
            whatsapp_number=whatsapp_number,
            **extra_fields
        )
        if password is None:
            raise ValueError("Password must be set")
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number=None, password=None, whatsapp_number=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(
            email=email,
            phone_number=phone_number,
            password=password,
            whatsapp_number=whatsapp_number,
            **extra_fields
        )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)  # Optional email
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    is_whatsapp_same_as_phone = models.BooleanField(default=False)  # New field to control behavior

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['phone_number', 'password']

    def save(self, *args, **kwargs):
        if self.is_whatsapp_same_as_phone and self.phone_number:
            self.whatsapp_number = self.phone_number
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email if self.email else self.phone_number

    class Meta:
        verbose_name_plural = "Users"
