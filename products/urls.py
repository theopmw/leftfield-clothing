from django.conf.urls import url
from django.urls import path, re_path
from . import views

# Code urls modified from:
# https://betterprogramming.pub/optimizing-django-admin-6a1187ddbb09 &
# https://stackoverflow.com/questions/47843241/django-admin-how-to-populate-select-options-depending-on-another-select

# app_name = 'products'

urlpatterns = [
    path('', views.all_products, name='products'),
    # Credit to use slug instead of id in url pattern modified from:
    # https://stackoverflow.com/questions/63481787/how-to-display-uniquely-generated-slugs-in-urls
    # Credit for code to build url using
    # slug and product_id parameters modified from:
    # https://wellfire.co/learn/fast-and-beautiful-urls-with-django/
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('<slug:slug>/<int:product_id>/', views.product_detail, name='product_detail'),
    # re_path(r'^getSubcategory/$', views.get_subcategory),
    path('add/', views.add_product, name='add_product'),
    ]
