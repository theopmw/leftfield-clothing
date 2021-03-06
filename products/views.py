from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, SubCategory, Category
from .forms import ProductForm


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
        # Sort products in the dropdown menu
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
            # Filter products that belong to the category
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Check if subcategory exists in request.GET
        if 'subcategory' in request.GET:
            # Get subcategory
            subcategories = request.GET['subcategory'].split(',')
            # Filter products that belong to the subcategory
            products = products.filter(subcategory__name__in=subcategories)
            subcategories = SubCategory.objects.filter(name__in=subcategories)

        # Check if 'q' is in request.GET
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


# Credit for get_redirected view taken from:
# https://wellfire.co/learn/fast-and-beautiful-urls-with-django/
def get_redirected(queryset_or_class, lookups, validators):
    """
    Calls get_object_or_404 and conditionally builds redirect URL
    """
    obj = get_object_or_404(queryset_or_class, **lookups)
    for key, value in validators.items():
        if value != getattr(obj, key):
            return obj, obj.get_absolute_url()
    return obj, None


# Credit view to handle slug instead of id modified from:
# https://stackoverflow.com/questions/63481787/how-to-display-uniquely-generated-slugs-in-urls
# Credit view to build url using slug and product_id parameters modified from:
# https://wellfire.co/learn/fast-and-beautiful-urls-with-django/
def product_detail(request, slug, product_id):
    """
    View to show individual product details.
    """
    product, product_url = get_redirected(
        Product, {'pk': product_id}, {'slug': slug})
    if product_url:
        return redirect(product_url)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    View to add a product to the store.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        # Instantiate a new instance of the product form
        # from request.post and include request .files
        # to capture product image if one exists
        form = ProductForm(request.POST, request.FILES)
        # Check if form is valid
        if form.is_valid():
            # Save it
            product = form.save()
            # Success message
            messages.success(request, f'Product ({product.name}) \
                added successfully.')
            # Redirect back to add product view
            return redirect(reverse(
                'product_detail', args=[product.slug, product.id]))
        # If errors on form
        else:
            # Error message
            messages.error(request, 'Failed to add product, \
            please check form.')
    else:
        # Instatiate empty form
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    View to edit a product.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Pre-fill form
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        # Instantiate a form from request.post and include request .files
        # and set instance to product obtained above
        form = ProductForm(request.POST, request.FILES, instance=product)
        # Check if form is valid
        if form.is_valid():
            # Save it
            form.save()
            # Success message
            messages.success(request, f'Product ({product.name}) \
                 updated successfully')
            # Redirect to the product detail page using product id
            return redirect(reverse(
                'product_detail', args=[product.slug, product.id]))
        else:
            # Error message
            messages.error(request, 'Failed to update product, \
            please check form.')
    else:
        # Instatiate product form using the product
        form = ProductForm(instance=product)
        # Message user
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
