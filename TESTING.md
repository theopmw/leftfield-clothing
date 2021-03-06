# Testing

# Leftfield Clothing
![Logo](media/readme_screenshots/logo.png)  
Link to the live site [here](https://leftfield-clothing-theopmw.herokuapp.com/).

- [Testing](#testing)
- [Leftfield Clothing](#leftfield-clothing)
  * [User Stories Testing](#user-stories-testing)
    + [As a User I Would like to:](#as-a-user-i-would-like-to-)
      - [Viewing and Navigation](#viewing-and-navigation)
      - [Registration and User Accounts](#registration-and-user-accounts)
      - [Sorting and Searching](#sorting-and-searching)
      - [Purchasing and Checkout](#purchasing-and-checkout)
      - [Blog](#blog)
    + [As an Admin I Would like to:](#as-an-admin-i-would-like-to-)
      - [Admin and Store Management](#admin-and-store-management)
  * [Manual Testing](#manual-testing)
    + [Navigation menu](#navigation-menu)
    + [Search bar](#search-bar)
    + [Footer](#footer)
    + [Home Page](#home-page)
    + [All Products Page](#all-products-page)
    + [Product Detail Page](#product-detail-page)
    + [Shopping Bag Page](#shopping-bag-page)
    + [Checkout Page](#checkout-page)
    + [Order Success Page](#order-success-page)
    + [Blog Posts Page](#blog-posts-page)
    + [Blog Post Page](#blog-post-page)
    + [Registration/Sign Up Page](#registration-sign-up-page)
    + [Confirm Email Address Page](#confirm-email-address-page)
    + [Sign In Page](#sign-in-page)
    + [Sign Out Page](#sign-out-page)
    + [Add Product Page](#add-product-page)
    + [Edit Product Page](#edit-product-page)
  * [Automated Testing](#automated-testing)
    + [W3C Markup Validation](#w3c-markup-validation)
    + [W3C CSS Validation](#w3c-css-validation)
    + [JSHint](#jshint)
    + [PEP8 Testing](#pep8-testing)
  * [Bugs](#bugs)
    + [Subcategory buttons only displaying on main category page](#subcategory-buttons-only-displaying-on-main-category-page)
    + [Slug field as url path causing add product URL error](#slug-field-as-url-path-causing-add-product-url-error)
    + [Django admin: populating select options depending on another select](#django-admin--populating-select-options-depending-on-another-select)
  * [Known bugs & issues](#known-bugs---issues)
    + [Delivery cost remaining in admin if all line items are removed](#delivery-cost-remaining-in-admin-if-all-line-items-are-removed)
    + [Category/Subcategory filter buttons not working when sorting selector box is used](#category-subcategory-filter-buttons-not-working-when-sorting-selector-box-is-used)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


![Am I responsive image](media/testing_screenshots/am_i_responsive.png)

## User Stories Testing

The user stories are annotated below to describe functionality and highlight the way in which the project fulfils the objectives set out. Relevant screenshots relating to each of the user stories below can be found in the main [README.md](https://github.com/theopmw/leftfield-clothing/blob/main/README.md) file.

### As a User I Would like to:

#### Viewing and Navigation

- **View a list of available products**

    - [x] The All Products nav menu item is clearly visible at the top of the page (or in the navbar toggler/burger menu on mobile and tablet) on all pages of the site and will redirect users to the All Products page.

- **View a specific category of products**

    - [x] The Category nav menu items are clearly visible at the top of the page (or in the navbar toggler/burger menu on mobile and tablet) on all pages of the site and will redirect users to the chosen category page.

- **View a specific subcategory of products**

    - [x] Hovering over a category in the nav menu (or clicking on mobile and tablet devices) will open the subcategory menu for each category.

    - [x] Beneath the page heading stating the category/subcategory is a list of subcategory buttons to allow the user to easily navigate between subcategories of the chosen category.

    - [x] Under each product, the subcategory is displayed as part of the product details, clicking on this will open the chosen subcategory page and display all products belonging to that subcategory.

- **View details of an individual product, including name, price, description, rating, image and sizes if applicable**

    - [x] Clicking any product image will open the specific product detail page which provides users with full details of the product, the ability to select quantities and sizes of the product and a button to add the product to their bag.

    - [x] Confirm that the product slug is correctly displayed in the page URL.

- **Easily review the total of my purchases**

    - [x] The Shopping Bag can be easily navigated to from the top navigation menu and is displayed on all pages of the site on all device sizes. The grand total is clearly displayed at the bottom of the page, following a summary of all items in the bag.

#### Registration and User Accounts

- **Easily register an account**

    - [x] When no user is in session, thye Register menu item is available in the top nav menu (on all devices).

    - [x] The form will check that the email and username are unique and not already registered in the DB. If they aren't unique, and error message will be displayed to the user to inform them that the username/email is already taken and prompt them to enter a new one.

    - [x] The form will check if both passwords match and meet the designated criteria. If they don't, an error message will notify the user and prompt them to enter a new one.

    - [x] If there are no validation errors, the account will be set up and the user will be redirected to the verify your email address page, a Bootstrap toast will notify the user that a confirmation email has been sent to their email address and once confirmed via the link in the email, they will be redirected to sign it to their new account.

    - [x] If the user is already registered, there is a link above the form to redirect them to the Sign In Page.

- **Easily login/logout**

    - [x] The Sign In Page is clearly visible on the navigation menu, when there is no user in session (on all devices).

    - [x] If the user inputs login credentials that do not match with any stored in the DB a message will be dispalyed to notify them that "The username and/or password you specified are not correct."

    - [x]  Once logged in and a registered user is in session, they will have access to the Profile link in the top navigation menu. They will be redirected to the Home Page and a Bootstrap toast will notify them they have been successfully logged in.

    - [x] If the user is does not have an account registered, there is a link above the form to redirect them to the Registration Page.

    - [x] When a registered user is in session, the Logout menu item is displayed in the top navigation menu. When clicked, the user will be redirected to the Sign Out Page and can confirm they wish to sign out. Upon successful logout the user will be redirected to the Home Page and a Bootstrap toast notifies them thay have been successfully logged out.

- **Easily recover my password if I lose access to my account**

    - [x] On the Sign In Page, there is a link to reset password beneath the form. When clicked, the user is redirected to the Password Reset Page where they can enter their email to recieve an email containing a link allowing them to reset their password.

- **Receive an email confirmation on successful registration of an account**

    - [x] On successful registration of account, the user is sent an email to the email address provided in the registration form with a link for them to confirm their email. On clicking this link, they are redirected to the Sign In page. A Bootstrap toast is displayed notifying the user of successful registration and email confirmation.

- **Have a personal user profile to view my order history and save my personal information**

    - [x] When a user is in session, the Profile page is available through the Account menu.

    - [x] The profile page displays the users default delivery information (which is saved if they check the checkbox when placing an order). They are able to update these details on the Profile page. The users order history is also displayed in chronological order. The order numbers act as links to open a confirmation with a full breakdown of the order.

#### Sorting and Searching

- **Sort the list of available products by name, price, brand or rating**

    - [x] From the All Products Page, the Sort Selector Box allows the user to sort all available items in ascending and decending order by name, price, brand or rating.

- **Sort multiple subcategories of products simultaneously across broad categories such as clothing or footwear**

    - [x] From the Category Page, the Sort Selector Box allows the user to sort categories of products in ascending and decending order by name, price, brand or rating.

- **Sort products within a specific subcategory by name, price, brand or rating**

    - [x] From the Subcategory Page, the Sort Selector Box allows the user to sort subcategories of products in ascending and decending order by name, price, brand or rating.

- **Search for a product by name, description or brand**

    - [x] The search bar allows the user to search all available products by name, description or brand.

    - [x] If the user submits an empty search, a Bootstrap toast is displayed to notify them that they haven't entered any search criteria.

- **Easily see what I have searched for and the number of results**

    - [x] If the user submits a successful search, the products that meet the search criteria are displayed. At the top of the page, the number of resuts and search term are displayed for the user, along with a link to return them to the All Products Page.

#### Purchasing and Checkout

- **Easily select the size and quantity of a product when purchasing**

    - [x] On the product detail page there is a Size selector box which displays the correct size type based on the type of product, or is hidden if the product does not have sizes.

    - [x] On the product detail page there is a Quantity selctor box which allows the user to select the quantity of product (range between 1-100).

- **View the items in my bag**

    - [x] The Shopping Bag page displays all prodycts currently in the bag.

    - [x] The user is able to use the quantity selector box to update the quantity of any product in the shopping bag or remove the item entirely.

- **View the total cost of items in my bag**

    - [x] At the bottom of the Shopping Bag page, the grand total of all items is diplayed including the delivery cost if applicable.

- **View the total shipping cost of my order**

    - [x] At the bottom of the Shopping Bag page, the delivery cost is displayed to the user.

    - [x] If the order is less than the free delivery threshold (??50), the user is notified of how much more they njeed to spend to qualify for free shipping.

    - [x] If the order is greater than the free delivery threshold, the delivery cost will be displayed as ??0.00.

- **Adjust the quantity of individual items in my bag**

    - [x] On the Shopping Bag page, the user can easily update or remove items in the shopping bag using the quantity selector and the update and remove buttons.

- **Easily enter my payment information**

    - [x] On the Checkout page, the user can easily enter their details to place an order.

     - [x] If the user has an account, is logged in and enters their details, they can check the checkbox to save the delivery information provided to their profile.

    - [x] If the user has an account, is logged in, and has saved thier details to their profile, the Details and Delivery section of the checkout form will be pre-filled with these saved details. If they enter new details, they can check the checkbox to save these new details to their profile.

    - [x] If there are any validation errors on the form, the user will be notified by an error message relating to the issue.

- **Know that my personal information and payment details are secure**

    - [x] As Stripe is used to handle all payments, their in-built security is applied to all payments made through the site.

- **View an order confirmation after checkout**

    - [x] Upon successful checkout, the user is redirected to a confirmation page outlining all the details of the order and is informed that a confirmation email has been sent to the email address provided in the checkout form.

- **Receive a confirmation email after checkout**

    - [x] Upon successful checkout, the user will be sent a confirmation email containing the details of the order.

#### Blog

- **Easily see a summary of posts**

    - [x] Clicking the Blog link in the main navigation menu opens the Blog Posts Page

    - [x] The Blog Posts page displays all the blog posts as Bootstap cards.

- **Easily open and see the full blog post**

    - [x] Clicking the 'Read More' button (or the post image) on the Blog Posts page opens the individual blog post page with full details of that blog post.

    - [x] Clicking the 'Back to Blog' button redirects the user back to the Blog Posts Page, displaying all blog posts.

    - [x] Check that the blog post slug is correctly displayed in the page URL

### As an Admin I Would like to:

#### Admin and Store Management

Admin users have full access to **CRUD** operations - **C**reate, **R**ead, **U**pdate and **D**elete.

- **Add a product**

    - [x] When logged in as an admin/superuser, the Product Management page is available from the Account menu.

    - [x] From the Product Management page the admin can add a product to the DB by filling out the Add Product form.

    - [x] If there are any validation errors whilst filling out the form, the admin will be notified.

    - [x] On successful form submission, the admin will be redirected to the new products product page.

- **Edit/update a product**

    - [x] From the Products page or an individual Product Detail page, admin users have access to the edit product button.

    - [x] This opens up the Edit Product form. This form is pre-filled with the product details and can be edited/updated by the admin and saved to the DB.

- **Delete a product**

    - [x] From the Products page or an individual Product Detail page, admin users have access to the delete product button.

    - [x] This button will permanently delete a product from the DB.

## Manual Testing

The site has been tested on a wide range of devices and browsers to confirm functionality.

### Navigation menu

- [x] Test all navigation menu items work on all screen sizes.

- [x] Log in and out and check correct navigation menu items are shown in the Account menu.

### Search bar

- [x] Enter a search query using product name, description or brand and ensure correct results are displayed and correct search term and number of results are shown at top of page.

- [x] Enter a blank seach to test error message is displayed.

- [x] Perform search that yields no resuts to test that '0 Products found for "query"' is displayed to the user at the top of the page.

### Footer

- [x] Test footer social links all open in new tab.

- [x] Test email link opens correctly.

### Home Page

- [x] Test image is responsive and displays correctly on all screen sizes.

- [x] Test Shop Now button redirects to All Products page.

### All Products Page

- [x] Confirm page layout is responsive, clear and readable on all screen sizes and devices.

- [x] Confirm number of products text displays correctly.

- [x] Confirm all sort parameters work correctly.

- [x] Confirm clicking on a product image opens the Product Detail page.

- [x] Confirm clicking on a product subcategory tag opens the correct Subcategory page and the category badge selected is set to active (colours are inverted).

- [x] Confirm Back to Top button works correctly.

- [x] (Admin/superuser only): Ensure Edit button launches the Product Management Edit Product page and all form fields are pre-filled.
    - Ensure on confirmation, product details have been successfully updated.

- [x] (Admin/superuser only) Ensure Delete button deletes a product.
    - Confirm product deleted successfully from DB.

### Product Detail Page

- [x] Confirm page layout is responsive, clear and readable on all screen sizes and devices.

- [x] Confirm URLs display correctly with slug value and product id in '/product/slug/id/' format.

- [x] Confirm clicking product image opens the image in a new tab.

- [x] Confirm clicking the subcategory tag opens the relevant Subcategory page.

- [x] Confirm size options are dynamic and are relevant to the specific product category/subcategory.

- [x] Confirm quantity selector works correctly and that the user cannot select a quantity outside of the set range (0-100).

- [x] (Admin/superuser only): Ensure Edit button launches the Product Management Edit Product page and all form fields are pre-filled.
    - Ensure on confirmation, product details have been successfully updated.

- [x] (Admin/superuser only) Ensure Delete button deletes a product.
    - Confirm product deleted successfully from DB.

- [x] Confirm Keep Shopping button returns the user to the All Products Page.

- [x] Confirm the Add To Bag button works correctly, the correct product, size and quantity are added to the bag and the Bootstrap toast launches and contains the correct information.

- [x] If the bag total is below the free delivery threshold, confirm that the Bootstrap toast contains the delivery cost and there is a message to the user notifying them of the amount they need to spend to qualify for free shipping. 

- [x] Confirm success toast is loading Django Humanize correctly to add a comma to large numbers.

- [x] Confirm Bootstrap toast 'Go To Shopping Bag' button redirects the user to the Shopping Bag page.

### Shopping Bag Page

- [x] Confirm page layout is responsive, clear and readable on all screen sizes and devices.

- [x] Confirm shopping bag displays correct items and all details for each product are rendered correctly.

- [x] Confirm 'Your bag is empty' message is displayed when navigating to the Shopping Bag page when empty. 

- [x] If multiple sizes of the same product are added to the shopping bag, confirm they are each on their own line and that the sizes are displayed correctly.

- [x] Confirm quantity selector works correctly and that the user cannot select a quantity outside of the set range (0-100).

- [x] Confirm that update quantity button works correctly and a Bootstrap toast is displayed to notify the user of the updated quantity.

- [x] Confirm that the remove item button works correctly and a Bootstrap toast is displayed to notify the user of the removed item.

- [x] Confirm that each item subtotal is correct and updates accordingly when an item quantity is updated.

- [x] Confirm that the Bag total is correct and updates accordingly.

- [x] Confirm that the delivery cost is correct and updates accordingly.

- [x] If the bag total is below the free delivery threshold, confirm that the delivery total is correct, that it is added to the grand total and that there is a message to the user notifying them of the amount they need to spend to qualify for free shipping. 

- [x] Confirm that the grand total is correct and updates accordingly.

- [x] Confirm Django Humanize is loading correctly on totals fields to add a comma to large numbers.

- [x] Confirm that the Keep Shopping button redirects the user to the All Products Page.

### Checkout Page

- [x] Confirm page layout is responsive, clear and readable on all screen sizes and devices.

- [x] Confirm that form renders correctly and all placeholders are correct.

- [x] If user in session, confirm all fields pre-filled as expected.

- [x] Attempt to submit form with mandatory fields left blank to test tooltips display correctly.

- [x] Test country select box works correctly.

- [x] Attempt to checkout with invalid card number to test error message is displayed.

- [x] Attempt to checkout with invalid expiry date to test error message is displayed.

- [x] Confirm Adjust Bag button redirects uder back to their bag.

- [x] Confirm total to pay is displayed underneath Complete Order button.

- [x] If no user in session, confirm 'Create an account or login to save this information' message is displayed.

- [x] If user in session, confirm 'Save this delivery information to my profile' checkbox is displayed and saves/updates user details when completing an order.

- [x] Confirm Order Summary displays the correct number of items in the users order.

- [x] Confirm Order Summary displays the correct items and details of the order are correct.

- [x] Confirm Order Summary displays the correct totals.

- [x] Confirm Django Humanize is loading correctly on totals fields to add a comma to large numbers.

- [x] Checkout with complete form and confirm loader displays and user is then redirected to Checkout Success page.

- [x] Break form and confirm order is still processed and order is added to users profile, DB and email confirmation is still sent to test Stripe webhooks are working as they should.

### Order Success Page

- [x] Confirm page layout is responsive, clear and readable on all screen sizes and devices.

- [x] Confirm confirmation email is correct.

- [x] Confirm all details are correct and relate to the information provided in the checkout form.

- [x] Confirm Django Humanize is loading correctly on totals fields to add a comma to large numbers.

### Blog Posts Page

- [x] Confirm page layout is responsive, clear and readable on all screen sizes and devices.

- [x] Confirm all post data is diplayed correctly on Bootstrap cards.

- [x] Confirm 'Read More' button and clicking the post image redirects to correct blog post page.

- [x] Confirm blog posts with 'Publish' status are displayed on the live site.

- [x] Confirm blog posts with 'Draft' status are not displayed on the live site but are available to edit and publish in the Django admin panel.

### Blog Post Page

- [x] Confirm page layout is responsive, clear and readable on all screen sizes and devices.

- [x] Confirm all post data is displayed correctly.

- [x] Confirm clicking the post image opens the image in a new tab.

- [x] Confirm 'Back to Blog' button redirects to the main Blog Posts Page.

### Registration/Sign Up Page

- [x] Confirm page layout is responsive, clear and readable on all screen sizes and devices.

- [x] Confirm 'Already have an account? Then please sign in' message is displayed at top of page and link redirects the user to the Sign In page.

- [x] Confirm that form renders correctly and all placeholders are correct.

- [x] Attempt to submit form with mandatory fields left blank to test tooltips display correctly.

- [x] Attempt to register with an email that is already in the DB to confirm error message is displayed to notify user that 'A user is already registered with this e-mail address'.

- [x] Attempt to register with a username that is already in the DB to confirm error message is displayed to notify user that 'A user with that username already exists'.

- [x] Attempt to register with email addresses that don't match to confirm 'You must type the same email each time' message is displayed to the user.

- [x] Attempt to register with passords that don't match to confirm 'You must type the same password each time' message is displayed to the user.

- [x] Click the Back to Login button to confirm it redirects the user back to the Sign In page.

- [x] Register with valid credentials to confirm that the user is redirected to the Verify Your Email Address Page and a Bootstrap toast is displayed notifying the user to check their email.

- [x] Click the link in the verification email to confirm that it redirects the user to the Confirm Email Address page.

### Confirm Email Address Page

- [x] Confirm page layout is responsive, clear and readable on all screen sizes and devices.

- [x] Test that the Confirm button redirects the user to the home page and a Bootstrap toast is displayed notifying the user that thier email has been confirmed.

### Sign In Page

- [x] Confirm page layout is responsive, clear and readable on all screen sizes and devices.

- [x] Confirm 'If you have not created an account yet, then please sign up first.' message is displayed at top of page and link redirects the user to the Sign Up page.

- [x] Enter an incorrect username or password to confirm the 'The username and/or password you specified are not correct' message is displayed.

- [x] Test that the Home button redirects the user to the Home page.

- [x] Enter valid credentials and test that the remember me checkbox works.

- [x] Enter valid credentials and test that the user is redirected to the home page.

### Sign Out Page

- [x] Confirm Cancel button works correctly and redirects user to the Home Page

- [x] Confirm Sign Out button works correctly and redirects user to the Home Page, Bootstrap toast notifies user they have succesfully been logged out and user has been logged out of their account.

### Add Product Page

- [x] Confirm page layout is responsive, clear and readable on all screen sizes and devices.

- [x] Confirm that form renders correctly and all labels and placeholders are correct.

- [x] Attempt to submit form with mandatory fields left blank to test tooltips display correctly.

- [x] Confirm that fields cannot exceed max length values set out in the model.

- [x] Attempt to enter an invalid slug and confirm that 'Enter a valid ???slug??? consisting of letters, numbers, underscores or hyphens' error message is displayed.

- [x] Attempt to enter a slug that is not unique, confirm that 'Product with this Slug already exists' error message is displayed.

- [x] Attempt to add product with invalid price field. Confirm that 'Ensure that there are no more than 6 digits in total' error message is displayed.

- [x] Attempt to enter a price without a decimal. Confirm that 'Ensure that there are no more than 4 digits before the decimal point' error message is displayed.

- [x] Confirm that Category and Subcategory fields display the correct options.

- [x] Confirm Select Image button works as expected and file name is displayed once selected.

- [x] If form fails to submit due to validation errors, confirm Bootstrap error toast is displayed.

- [x] On successful form submission, confirm user is redirected to Product Detail page for the newly added product and Bootstrap toast notifies user that product has been added.

- [x] Check admin to confirm product has been added to DB.

- [x] Check AWS Bucket to confirm product image has been added to media folder.

### Edit Product Page

- [x] Confirm page layout is responsive, clear and readable on all screen sizes and devices.

- [x] Confirm that form renders correctly and all labels and placeholders are correct.

- [x] Attempt to submit form with mandatory fields left blank to test tooltips display correctly.

- [x] Confirm that fields cannot exceed max length values set out in the model.

- [x] Attempt to enter an invalid slug and confirm that 'Enter a valid ???slug??? consisting of letters, numbers, underscores or hyphens' error message is displayed.

- [x] Attempt to enter a slug that is not unique, confirm that 'Product with this Slug already exists' error message is displayed.

- [x] Attempt to add product with invalid price field. Confirm that 'Ensure that there are no more than 6 digits in total' error message is displayed.

- [x] Attempt to enter a price without a decimal. Confirm that 'Ensure that there are no more than 4 digits before the decimal point' error message is displayed.

- [x] Confirm that Category and Subcategory fields display the correct options.

- [x] Confirm Select Image button works as expected and file name is displayed once selected.

- [x] If form fails to submit due to validation errors, confirm Bootstrap error toast is displayed.

- [x] On successful form submission, confirm user is redirected to Product Detail page for the newly upated product and Bootstrap toast notifies user that product has been updated.

- [x] Check admin to confirm product has been updated in DB.

- [x] Check AWS Bucket to confirm product image has been added to media folder.

## Automated Testing

The following automated tools/linters were used to test the project code throughout the development process:

### W3C Markup Validation
(HTML)

* Only warnings/errors displayed by [W3C Markup Validation Service](https://validator.w3.org/) relate to the use of Django template tags throughout .html files.

### W3C CSS Validation
(CSS)

* No errors or warnings were found when the CSS files were tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

### JSHint
(JavaScript)

* [JSHint](https://jshint.com/) was used to JavaScript files, no errors or warnings were found.

### PEP8 Testing
(Python)

* [Autopep8](https://pypi.org/project/autopep8/) was used to help with Python formatting to meet PEP8 compliance guidelines.

[PEP8 Online](http://pep8online.com/) was used to check all python code.

## ??Bugs

### Subcategory buttons only displaying on main category page

Expected  
When one of the subcategory buttons is clicked, the url for that category or subcategory is opened, and the products belonging to that category or subcategory are displayed.

Result  
The buttons were showing when the user selects the category  (eg. ???All Clothing??? / ???All Footwear???) option from the main nav dropdown menu but weren???t once the user then clicks one of the subcategory buttons at the top of the page.

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
    {% elif category.name == "accessories" %}
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
        {% elif subcategory.category.name == "accessories" %}
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

### Slug field as url path causing add product URL error

Expected:  
When navigating to the add product URL, the add product page is displayed.

Testing:  
Navigate to the add product page.

Result:  
A page not found (404) error is displayed.

![Slug fields causing add product page bug error](media/slug_field_bug_error.png)

The 404.html/500.html files were later added to tie in with the site and provide a better UX should their be an error with the site:

![404/500 error page](media/testing_screenshots/404_500_error.png)

This was caused as the product detail URL is set to a slug and the when navigating to products/add URL, add was being interpreted as a slug(string). 

Fix:  
Since a slug is a string and therefore cannot be specified as an integer, the product_id had to be added to the URL so that Django would continue past the product detail URL to retrieve the add product URL. As they are both strings, Django was interpretting the /add as a product. The URL had to be set up to take a slug and an integer as parameters, but in the view use only the integer primary key to access the product. Then the object???s get_absolute_url object inserts both slug and primary key into the URL.

Code snippet for fix:

Set up url to take a slug and integer as parameters - [products/urls.py](products/urls.py):  
```
urlpatterns = [
    path('', views.all_products, name='products'),
    path('<slug:slug>/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    ]
```

In the views use the integer primary key to access the product - [products/views.py](products/views.py):  
```
def get_redirected(queryset_or_class, lookups, validators):
    """
    Calls get_object_or_404 and conditionally builds redirect URL.
    """
    obj = get_object_or_404(queryset_or_class, **lookups)
    for key, value in validators.items():
        if value != getattr(obj, key):
            return obj, obj.get_absolute_url()
    return obj, None


def product_detail(request, slug, product_id):
    """
    View to show individual product details.
    """
    product, product_url = get_redirected(Product, {'pk': product_id}, {'slug': slug})
    if product_url:
        return redirect(product_url)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
```

Add get_absolute_url object to Product model - [products/models.py](products/models.py): 
```
class Product(models.Model):
    """
    Model for Product table
    """
    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug, 'id':self.id})
    # Everything else in model
``` 

Update URL path in template to take product id - [products/templates/products/products.html](products/templates/products/products.html) :
```
<a href="{% url 'product_detail' product.slug product.id %}">
    <img class="card-img-top img-fluid" src="{{ product.image.url }}" alt="{{ product.name }}">
</a>
{% else %}
<a href="{% url 'product_detail' product.slug product.id%}">
    <img class="card-img-top img-fluid" src="{{ MEDIA_URL }}noimage.png" alt="{{ product.name }}">
</a>
```

### Django admin: populating select options depending on another select

Expected:  
The aim was to create a data structure where each product related to a subcategory and each subcategory related to a category. When adding products in the Django admin panel the values available to select in the subcategories dropdown should only be children of the parent category.

Testing:  
Attempt to add a product and check whether subcategory dropdown items are filtering correctly based on the parent category selected in the category dropdown.

Result:  
All subcategories were shown regardless of the selection of category.

![Django admin select box bug](media/testing_screenshots/populate_select_options_depending_on_another_select_bug.png)

Fix:  
To fix this the [views.py](products/views.py) file had to be adapted. The initial source that assisted the development of this feature was modified from an article from [Better Programming](https://betterprogramming.pub/optimizing-django-admin-6a1187ddbb09). In order to achieve the desired result the get sub_category view had to be modified from the original source into the following:
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

NOTES: This feature was later removed as it was causing issues with other product URLs, issue will be fixed and feature will be added back in at a later date.

## ??Known bugs & issues

### Delivery cost remaining in admin if all line items are removed

If products are removed via the admin panel to set the order total at ??0.00, the delivery cost still remains on the order in the admin.

![Delivery cost bug](media/testing_screenshots/delivery_cost_bug.png)

The code that causes this is from the update_total function in the checkout app [models.py](checkout/models.py) file.

The following code snippet from [checkout/models.py](checkout/models.py) illustrates that the bug is caused by the STANDARD_DELIVERY_PRICE being applied to any order total that is below the FREE_DELIVERY_THRESHOLD, even if that total is ??0.00.

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

Since the user is unable to create an order of ??0.00 this should not cause eny errors or issues for the user when placing an order or allow any delivery charges to be made to the users account without making a purchase that is below the free delivery threshold (??50.00) but greater than ??0.00.

### Category/Subcategory filter buttons not working when sorting selector box is used

When on a category or subcategory page, use of the sorting selector box breaks the active category button functionality. Due to time constraints the code cannot be refactored be modified to rectify this problem but will be fixed at a later date. See screenshots below to illustrate the issue:

Active category button functionality when sorting selector box not used:

![Sort selector box, no sorting](media/testing_screenshots/sort_selector_box-bug_1.png)

Active category button functionality when sorting selector box used:

![Sort selector box, with sorting](media/testing_screenshots/sort_selector_box-bug_2.png)
