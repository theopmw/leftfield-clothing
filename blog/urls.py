from django.urls import path
from . import views


# Credit: code for blog URLs modified from:
# https://djangocentral.com/building-a-blog-application-with-django/
urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
