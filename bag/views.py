from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ View to render bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    # Get item quantity from the from on
    # product_detail.html & convert to integer
    quantity = int(request.POST.get('quantity'))
    # Get redirect url from form
    redirect_url = request.POST.get('redirect_url')
    # Check if there is a bag variable in the session
    # or initalize it to an empty dictionary if it doesn't
    bag = request.session.get('bag', {})

    # Update quantity of item in bag if specific item already in bag
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    # If item not already in bag, add item to bag
    else:
        bag[item_id] = quantity

    # Overwrite bag variable in session with updated version
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
