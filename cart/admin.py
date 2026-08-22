from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at', 'total')
    inlines = [CartItemInline]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'status', 'total')
    list_filter = ('status', 'created_at', 'user')
    inlines = [OrderItemInline]


admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
