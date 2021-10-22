## Bugs

- ### Django admin: populating select options depending on another select

Expected:  
The aim was to create a data structure where each product related to a subcategory and each subcategory related to a category. When adding products in the Django admin panel. The values available to select in the subcategories dropdown should only be childern of the parent category.

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
