from django.shortcuts import render, get_object_or_404
from .models import Product, SubCategory, Category
from django.http import HttpResponse
import json


# Code for view modified from:
# https://betterprogramming.pub/optimizing-django-admin-6a1187ddbb09 &
# https://stackoverflow.com/questions/47843241/django-admin-how-to-populate-select-options-depending-on-another-select
# def get_subcategory(request):
#     """
#     View to get parent category, filter items in the subcategory field
#     dropdown based on the category selected and respond with json data.
#     """
#     # Get category id from DB based on dropdown selection
#     category = request.GET.get('id')
#     print("CATEGORY: ", category)
#     # Filter subcategories based on the category select box value
#     result = list(SubCategory.objects.filter(
#         category_id=int(category)).values('category', 'name'))
#     print("GET RESULT: ", result)
#     return HttpResponse(json.dumps(result), content_type="application/json")


def all_products(request):
    """
    View to show all products, including sorting and search queries.
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View to show individual product details.
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
