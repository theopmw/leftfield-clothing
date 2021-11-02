from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ View to render bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    # Get the product
    product = Product.objects.get(pk=item_id)
    # Get item quantity from the from
    # product_detail.html & convert to integer
    quantity = int(request.POST.get('quantity'))
    # Get redirect url from form
    redirect_url = request.POST.get('redirect_url')
    # Set size to None
    size = None
    # If size is in request.POST set it equal to that size
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # Check if there is a bag variable in the session
    # or initalize it to an empty dictionary there isn't
    bag = request.session.get('bag', {})

    # Check if product with sizes is being added to bag
    if size:
        # If item is in bag:
        if item_id in list(bag.keys()):
            # Check if another item of the same id and same size already exists
            if size in bag[item_id]['items_by_size'].keys():
                # If it does, increment the quantityfor thath size
                bag[item_id]['items_by_size'][size] += quantity
            else:
                # If it doesn't, set it equal to the quantity
                bag[item_id]['items_by_size'][size] = quantity
        # If item not in bag:
        else:
            # Add as dictionary
            bag[item_id] = {'items_by_size': {size: quantity}}
    # If product has no sizes
    else:
        # Update quantity of item in bag if specific item already in bag
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        # If item not already in bag, add item to bag
        else:
            bag[item_id] = quantity
            # Add message to success object to
            # let users know product added to bag
            messages.success(request, f'Added {product.name} to your bag')

    # Overwrite bag variable in session with updated version
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    # Get item quantity from the from
    # product_detail.html & convert to integer
    quantity = int(request.POST.get('quantity'))
    # Set size to None
    size = None
    # If size is in request.POST set it equal to that size
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # Check if there is a bag variable in the session
    # or initalize it to an empty dictionary there isn't
    bag = request.session.get('bag', {})

    # Adjust products with sizes
    if size:
        # If quantity greater than 0, set the items quantity accordingly
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            # If quantity is 0, remove item with size
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    # Adjust products without sizes
    else:
        # If quantity greater than 0, set the items quantity accordingly
        if quantity > 0:
            bag[item_id] = quantity
        # If quantity is 0, remove item using pop
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            # Delete items with sizes from bag
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        # Delete items without sizes from bag
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
