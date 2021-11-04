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
    }

    return render(request, template, context)
