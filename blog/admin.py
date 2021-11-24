from django.contrib import admin
from .models import Post


# Creit: code for blog admin modified from:
# https://djangocentral.com/building-a-blog-application-with-django/
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
