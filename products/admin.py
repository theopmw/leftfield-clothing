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
    prepopulated_fields = {'slug': ('name',)}

    ordering = ('sku',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'slug',
        'category',
    )
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
