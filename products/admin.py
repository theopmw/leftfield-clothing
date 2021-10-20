from django.contrib import admin
from .models import Product, SubCategory, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Category)
