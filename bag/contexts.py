from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    # Empty list for bag items to live in
    bag_items = []
    # Initialize total and product_count to 0
    total = 0
    product_count = 0

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
