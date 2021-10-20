from django.conf.urls import url
from . import views

# Code urls modified from:
# https://betterprogramming.pub/optimizing-django-admin-6a1187ddbb09 &
# https://stackoverflow.com/questions/47843241/django-admin-how-to-populate-select-options-depending-on-another-select
app_name = 'products'
urlpatterns = [
    url(r'^/getSubcategory/$', views.get_subcategory)
    ]
