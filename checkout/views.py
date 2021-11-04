from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    # Get bag from the session
    bag = request.session.get('bag', {})
    # If nothing in bag, notify user with error message and
    # and redirect back to products page
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    # Create instance of order form
    order_form = OrderForm()
    # Create the template
    template = 'checkout/checkout.html'
    # Create context containing the order form
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JeyR3ET4xRWCPubfCOSbuYD6nJiUj'
        'f8wFgebja6zzbVJDtRdWeYFhYzX61MVkmTOyFjYfUxLAxgOhZmupYNOuhW0083M6Ur7D',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
