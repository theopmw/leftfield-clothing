from django.contrib import admin
from .models import Product, SubCategory, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'subcategory',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'category',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
