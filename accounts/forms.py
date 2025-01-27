from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         fields = ['phone_number', 'whatsapp_number', 'password']

class SuperUserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email or Phone Number")


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'phone_number',  'password', 'is_whatsapp_same_as_phone']

    def save(self, commit=True):
        user = super().save(commit=False)
        if user.is_whatsapp_same_as_phone:
            user.whatsapp_number = user.phone_number
        if commit:
            user.save()
        return user

