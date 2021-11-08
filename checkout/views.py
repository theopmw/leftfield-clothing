from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
import stripe
import json

from bag.contexts import bag_contents
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product


@require_POST
def cache_checkout_data(request):
    try:
        # Get payment intent id
        pid = request.POST.get('client_secret').split('_secret')[0]
        # Set up stripe with the secret to modify the payment intent
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        # If error return response with the error message content
        # and a status of 400 for bad request.
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Post method handling:
    # Check if request method is POST
    if request.method == 'POST':
        # Get bag from the session
        bag = request.session.get('bag', {})
        # Put form data into dictionary
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        # If form is valid:
        if order_form.is_valid():
            # Save the form
            order = order_form.save()
            # Iterate through bag items to create each line item
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    # Products without sizes
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    # Products with sizes
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                # If product not found:
                except Product.DoesNotExist:
                    # Error message to notify user
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please contact us for assistance!")
                    )
                    # Delete the empty order
                    order.delete()
                    # Return user to shopping bag page
                    return redirect(reverse('view_bag'))
            # Check if user saved profile info to session
            # and redirect to checkout success page if true
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            # If order form not valid, send message to notify user
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        # Get bag from the session
        bag = request.session.get('bag', {})
        # If nothing in bag, notify user with error message and
        # and redirect back to products page
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        # Get bag contents dictionary
        current_bag = bag_contents(request)
        # Get grand total key from current bag
        total = current_bag['grand_total']
        # Multiply total by 100 and round to zero decimal places
        # as stripe requires the amount to charge as an integer
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Create instance of order form
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    # Create the template
    template = 'checkout/checkout.html'
    # Create context containing the order form
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    # Check if user saved saved info to session
    save_info = request.session.get('save_info')
    # Use order number to get the order created in the
    # checkout view and send back to the template
    order = get_object_or_404(Order, order_number=order_number)
    # Attach success message to notify user of their order number
    # and that email will be sent
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        # Delete users shopping bag from session
        del request.session['bag']

    # Set template and context
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    # Render template
    return render(request, template, context)
