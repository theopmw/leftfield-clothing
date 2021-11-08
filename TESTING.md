## Bugs

- ### Django admin: populating select options depending on another select

Expected:  
The aim was to create a data structure where each product related to a subcategory and each subcategory related to a category. When adding products in the Django admin panel the values available to select in the subcategories dropdown should only be childern of the parent category.

Testing:  
Attempt to add a product and check whether subcategory dropdown items are filtering correctly based on the parent category selected in the category dropdown.

Result:  
All subcategories were shown regardless of the selection of category.

![Django admin select box bug](media/testing_screenshots/populate_select_options_depending_on_another_select_bug.png)

Fix:  
To fix this the views.py file had to be adapted. The initial source that assisted the development of this feature was modified from an article from [Better Programming](https://betterprogramming.pub/optimizing-django-admin-6a1187ddbb09). In order to achieve the desired result the get sub_category view had to be modified from the original source into the following:
```
def get_subcategory(request):
    """
    View to get parent category, filter items in the subcategory field
    dropdown based on the category selected and respond with json data.
    """
    # Get category id from DB based on dropdown selection
    category = request.GET.get('id')
    print("CATEGORY: ", category)
    # Filter sucategories based on the category select box value
    result = list(SubCategory.objects.filter(
        category_id=int(category)).values('category', 'name'))
    print("GET RESULT: ", result)
    return HttpResponse(json.dumps(result), content_type="application/json")
```

The final result can be seen below, only subcategories of the clothing category are available for selection from the subcategoy dropdown when the category dropdown is set to "Clothing".
![Django admin select box fix](media/testing_screenshots/populate_select_options_depending_on_another_select_fix.png)

- ### Subcategory buttons only displaying on main category page

Expected  
When one of the subcategory buttons is clicked, the url for that category or subcategory is opened, and the products belonging to that category or subcategory are displayed.

Result  
The buttons were showing when the user selects the category  (eg. “All Clothing” / “All Footwear”) option from the main nav dropdown menu but weren’t once the user then clicks one of the subcategory buttons at the top of the page.

Screenshot of All Clothing page (with nav buttons displayed):

![Subcategory buttons displaying on category page](media/testing_screenshots/subcategory_buttons_displaying.png)

Screenshot of Shirts page (without nav buttons displayed):

![Subcategory buttons not displaying on subcategory page](media/testing_screenshots/subcategory_buttons_not_dispaying.png)

Testing  
When the user clicks one of the subcategory buttons, the correct page is shown but the buttons for other subcategories were no longer displayed.

Fix  
An additional for loop had to be added to loop over the sub categories and check that the subcategories belonged to the parent category.

Screenshot of Shirts page (with nav buttons displayed):

![Subcategory buttons displaying on subcategory page](media/testing_screenshots/sucbcategory_buttons_displaying_fix.png)

Code snippet with both loops:

```   
{% for category in current_categories %}
    {% if category.name == "clothing" %}
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?category=clothing">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">All Clothing</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=t_shirts">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">T-Shirts</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=shirts">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Shirts</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=sweatshirts_hoodies">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Sweatshirts & Hoodies</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=coats_jackets">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Coats & Jackets</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=jeans_trousers">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Jeans & Trousers</span>
        </a>
    {% elif category.name == "footwear" %}
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?catesgory=footwear">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">All Footwear</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=trainers">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Trainers</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=boots">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Boots</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=shoes">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Shoes</span>
        </a>
    {% elif current_categories is accessories %}
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?category=accessories">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">All Accessories</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=bags">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Bags</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=hats">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Hats</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=socks">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Socks</span>
        </a>
    {% elif current_categories is special_offers %}
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?category=special_offers">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">SPECIAL OFFERS TEST BUTTON</span>
        </a>
    {% endif %}
{% endfor %}
{% for subcategory in current_subcategories %}
    {% if subcategory.category.name == "clothing" %}
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?category=clothing">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">All Clothing</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=t_shirts">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">T-Shirts</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=shirts">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Shirts</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=sweatshirts_hoodies">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Sweatshirts & Hoodies</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=coats_jackets">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Coats & Jackets</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=jeans_trousers">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Jeans & Trousers</span>
        </a>
    {% elif subcategory.category.name == "footwear" %}
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?category=footwear">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">All Footwear</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=trainers">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Trainers</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=boots">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Boots</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=shoes">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Shoes</span>
        </a>
        {% elif current_categories is accessories %}
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?category=accessories">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">All Accessories</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=bags">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Bags</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=hats">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Hats</span>
        </a>
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?subcategory=socks">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">Socks</span>
        </a>
    {% elif current_categories is special_offers %}
        <a class="subcategory-badge text-decoration-none" href="{% url 'products' %}?category=special_offers">
            <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">SPECIAL OFFERS TEST BUTTON</span>
        </a>
    {% endif %}
{% endfor %} 

```

## Known bugs & issues

- ### Delivery cost remaining in admin if all line items are removed

If products are removed via the admin panel to set the order total at £0.00, the delivery cost still remains on the order in the admin.

![Delivery cost bug](media/testing_screenshots/delivery_cost_bug.png)

The code that causes this is from the update_total function in the checkout app [models.py](checkout/models.py) file.

The following code snippet illustrates that the bug is caused by the STANDARD_DELIVERY_PRICE being applied to any order total that is below the FREE_DELIVERY_THRESHOLD, even if that total is £0.00.

```
def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                settings.STANDARD_DELIVERY_PRICE)
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()
```

Since the user is unable to create an order of £0.00 this should not cause eny errors or issues for the user when placing an order or allow any delivery charges to be made to the users account without making a purchase that is below the free delivery threshold (£50.00) but greater than £0.00.