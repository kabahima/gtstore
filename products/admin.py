# admin.py
from django.contrib import admin
from .models import Product, ProductCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'slug', 'likes_count')
    search_fields = ('title', 'category__name')
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from title

    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = 'Likes'


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  # Auto-fill slug from name
    list_display = ("name", "slug") 

admin.site.register(Product, ProductAdmin)

