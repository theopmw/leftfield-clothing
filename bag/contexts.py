from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    # Empty list for bag items to live in
    bag_items = []
    # Initialize total and product_count to 0
    total = 0
    product_count = 0
    # Check if there is a bag variable in the session
    # or initalize it to an empty dictionary there isn't
    bag = request.session.get('bag', {})

    # For each item and quantity in bag.items from the current session
    for item_id, quantity in bag.items():
        # Get the product
        product = get_object_or_404(Product, pk=item_id)
        # Add its quantity * price to the total
        total += quantity * product.price
        # Increment product_count by the quantity
        product_count += quantity
        # Add dictionary to list of bag items containing
        # the id, quantity and also the product object (to give access to all
        # other fields of the product, image etc.) when iterating through
        # bag items in the templates
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # Set delivery cost based on total bag contents
    # Calculate delivery if bag contents is not 0
    # and less than FREE_DELIVERY_THRESHOLD
    if total > 0 and total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_PRICE
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    # Calculate delivery if bag contents > FREE_DELIVERY_THRESHOLD
    else:
        delivery = 0
        free_delivery_delta = 0

    # Calculate grand total
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
