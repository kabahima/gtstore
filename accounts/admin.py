from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser





class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'phone_number', 'whatsapp_number', 'is_staff', 'is_superuser')
    search_fields = ('email', 'phone_number', 'whatsapp_number')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'whatsapp_number', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'whatsapp_number', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.site_header = "GT Furniture  Admin Panel"
admin.site.site_title = "GT Furniture Ug"
admin.site.index_title = "Welcome to MyStore Administration"
# admin.site.register(CustomUser, CustomUserAdmin)
