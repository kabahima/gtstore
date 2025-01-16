from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, whatsapp_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Users must provide a phone number")
        user = self.model(phone_number=phone_number, whatsapp_number=whatsapp_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, whatsapp_number, email, password=None, **extra_fields):
        """
        Create and return a superuser with email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        user = self.create_user(phone_number, whatsapp_number, password=password, email=email, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)  # For superusers
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    is_whatsapp_same_as_phone = models.BooleanField(default=False)  # New field to control behavior
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Superusers login with email
    REQUIRED_FIELDS = ['phone_number']

    def save(self, *args, **kwargs):
        # If the user selects 'is_whatsapp_same_as_phone', make whatsapp_number the same as phone_number
        if self.is_whatsapp_same_as_phone and self.phone_number:
            self.whatsapp_number = self.phone_number
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email if self.email else self.phone_numberr
    
    class Meta:
        verbose_name_plural = "Users"
