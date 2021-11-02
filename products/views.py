from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
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
    query = None
    categories = None
    subcategories = None
    sort = None
    direction = None

    # Check if request.GET exists
    if request.GET:
        # Check if sort is in request.GET
        if 'sort' in request.GET:
            # If it is set it to sort and sortkey
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                # Rename sortkey to lower_name in event user is sorting by name
                sortkey = 'lower_name'
                # Annotate current list of products with a new field
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                # Check if direction is descending
                if direction == 'desc':
                    # If it is descending add '-' in front of sortkey
                    # using string formatting to reverse order
                    sortkey = f'-{sortkey}'
            # Use order_by model method to sort products
            products = products.order_by(sortkey)

        # Check if category exists in request.GET
        if 'category' in request.GET:
            # Get category
            categories = request.GET['category'].split(',')
            print("CATEGORIES: ", categories)
            # Filter products that belong to the category
            products = products.filter(category__name__in=categories)
            print("PRODUCTS: ", products)
            categories = Category.objects.filter(name__in=categories)

        # Check if subcategory exists in request.GET
        if 'subcategory' in request.GET:
            # Get subcategory
            subcategories = request.GET['subcategory'].split(',')
            print("SUBCATEGORIES: ", subcategories)
            # Filter products that belong to the subcategory
            products = products.filter(subcategory__name__in=subcategories)
            print("PRODUCTS: ", products)
            subcategories = SubCategory.objects.filter(name__in=subcategories)

        # Check if 'q' is in request.GET
        # (text input in the search form is named 'q')
        if 'q' in request.GET:
            query = request.GET['q']
            # If query is blank attach an error message to the request
            # using Django messages and redirect back to the products url
            if not query:
                messages.error(request, "You didn't enter any search critera!")
                return redirect(reverse('products'))

            # If query isn't blank, use Q to generate a search query
            queries = Q(
                name__icontains=query) | Q(
                    brand__icontains=query) | Q(
                        description__icontains=query)
            products = products.filter(queries)

    # Return current sorting methodology to template
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_subcategories': subcategories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


# Credit view to handle slug instead of id modified from:
# https://stackoverflow.com/questions/63481787/how-to-display-uniquely-generated-slugs-in-urls
def product_detail(request, slug=None):
    """
    View to show individual product details.
    """
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
