from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
import stripe

from bag.contexts import bag_contents
from .forms import OrderForm


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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
