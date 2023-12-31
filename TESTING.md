## Table of Contents
* [Manual Testing](#manual-testing)
  * [Navigation](#navigation)
  * [Index Page](#index-page)
  * [My Profile Page](#my-profile-page)
  * [Product List Page](#product-list-page)
  * [My Favourite Products Page](#my-favourite-products-page)
  * [Products Details Page](#products-details-page)
  * [Shopping Bag Page](#shopping-bag-page)
  * [Checkout Page](#checkout-page)
  * [Checkout Success Page](#checkout-success-page)
  * [Add Product Page](#add-product-page)
  * [Edit Product Page](#edit-product-page)
  * [Delete Product](#delete-product)
  * [Django All Auth Pages](#django-all-auth-pages)
* [Admin panel](#admin-panel-testing)
* [Browser Testing](#browser-testing)
* [Bugs](#bugs)
  * [Fixed Bugs](#fixed-bugs)
  * [Unfixed Bugs](#unfixed-bugs)
* [Code Validation](#code-validation)
  * [W3C HTML VALIDATION](#w3c-html-validation)
  * [Jigsaw CSS VALIDATION](#jigsaw-css-validation)
  * [JSHint JavaScript VALIDATION](#jshint-javascript-validation)
  * [CI Python Linter Python VALIDATION](#ci-python-linter-python-validation)
  * [Lighthouse Reports](#lighthouse-reports)

---


## Manual Testing

### Navigation

| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Home link  | Click on the "Home" link in the navigation bar  | The page should navigate to the home page  | Pass  |
| All Products link | Click on the "Browse All" link in the navigation bar  | The dropdown menu should expand, showing sorting and browsing options  | Pass  |
| Fresh Harvest link  | Click on the "Fresh Harvest" link in the navigation bar  | The dropdown menu should expand, showing subcategories  | Pass  |
| Fresh Farm Box link  | Click on the "Fresh Farm Box" link in the navigation bar  | The dropdown menu should expand, showing subcategories  | Pass  |
| Special Offers link  | 	Click on the "Special Offers" link in the navigation bar  | The dropdown menu should expand, showing special offer categories  | Pass  |
| Search functionality  | Enter a search term in the search bar and press Enter or click "Search"  | Relevant search results should be displayed on the search results page  | Pass  |
| Bag link  | Click on the "Bag" link in the navigation bar  | The page should navigate to the shopping bag page  | Pass  |
| User Account dropdown (authenticated user)  | Click on the user account dropdown in the navigation bar  | The dropdown menu should expand, showing user-related options  | Pass  |
| Register link (unauthenticated user)  | Click on the "Register" link in the user account dropdown  | The page should navigate to the registration page  | Pass  |
| Login link (unauthenticated user)  | Click on the "Login" link in the user account dropdown  | The page should navigate to the login page  | Pass  |
| Product Management link (superuser)  | Click on the "Product Management" link in the user account dropdown  | The page should navigate to the product management page (visible to superusers only)	  | Pass  |
| My Profile link (authenticated user)  | Click on the "My Profile" link in the user account dropdown  | The page should navigate to the user's profile page  | Pass  |
| Logout link (authenticated user)  | Click on the "Logout" link in the user account dropdown  | The user should be logged out and redirected to the logout page  | Pass  |
| My Favourite link (authenticated user)  | Click on the "My Favourite" link in the navigation bar  | The page should navigate to the user's favorite products page  | Pass  |
| Grand Total (Mobile) link  | Click on the cart icon with the grand total in mobile view  | The page should navigate to the shopping cart page  | Pass  |

### Index Page

| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Message  | Check if the main message "Quality & Freshness are here" is displayed  | The main message should be prominently displayed  | Pass  |
| Shop Now Button  | Click on the "Shop Now" button  | The page should navigate to the products page  | Pass  |
| Newsletter Subscription Form  | Enter a valid email address in the email input field and click the "Subscribe" button  | A success message should appear, indicating successful subscription  | Pass  |
| Newsletter Subscription Form - Invalid Email  |  Enter an invalid email address in the email input field and click the "Subscribe" button  | An error message should appear, indicating invalid email format  | Pass  |
| Newsletter Subscription Form - Empty Email  | Submit the form without entering an email address  | An error message should appear, indicating that the email address is required  | Pass  |
| Newsletter Subscription Form - Empty Form  | Submit the form without entering any information  | An error message should appear, indicating that the email address is required  | Pass  |
| Newsletter Subscription Form - Spam Protection  | Ensure that the spam protection input field is left blank  | The form should not be submitted successfully  | Pass  |
| Newsletter Subscription Form - Intuit Mailchimp Badge  | Check if the Intuit Mailchimp badge is displayed and clickable  | The badge should lead to the Intuit Mailchimp website  | Pass  |


### My Profile Page

| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Default Delivery Information Form  | Verify if the default delivery information form is displayed  | The form should be displayed with fields for phone number, street address, postcode, city, and country  | Pass  |
| Default Delivery Information Form - Empty Fields  | Submit the form without entering any information  | An error message should appear for required fields  | Pass  |
| Default Delivery Information Form - Invalid Phone Number  | Enter an invalid phone number format and submit the form  | An error message should appear indicating an invalid phone number format  | Pass  |
| Default Delivery Information Form - Valid Submission  | Enter valid information in all required fields and submit the form  | The form should be submitted successfully and a success message may appear  | Pass  |
| Default Delivery Information Form - Country Field  | Check the country field color before and after selecting a country  | The country field color should be gray before selection and black after selection  | Pass  |
| Order History Table  | Verify if the order history table is displayed  | The table should display order numbers, dates, items, and order totals  | Pass  |
| Order History Table - Order Number Link  | Click on an order number link  | The page should navigate to the order history page for that specific order  | Pass  |
| Order History Table - Order Items  | Verify if the ordered items are displayed correctly  | The items for each order should be listed with their quantities and units  | Pass  |
| Order History Table - Order Total  | Verify if the order total is displayed correctly  | The total cost for each order should be displayed  | Pass  |
| JavaScript Interaction  | Test the JavaScript interaction of the country field  | Change the country selection and verify if the color changes accordingly  | Pass  |


### Product List Page

| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Product List Display  | Access the product list page  | The page should display a list of products with their images, names, prices, and categories  | Pass  |
| Product Sorting  | Test each sorting option in the "Sort by" dropdown  | The products should be sorted according to the selected option (price low-to-high, price high-to-low, name A-Z, name Z-A, category A-Z, category Z-A)  | Pass  |
| Category Filtering  | Click on a category badge  | The page should display products from the selected category only  | Pass  |
| Search Functionality  | Enter a search term and submit the form  | The page should display products matching the search term in their names or descriptions  | Pass  |
| Search Functionality - Empty Query  | Submit the search form without entering any query  | An error message should appear indicating no search criteria provided  | Pass  |
| Favorites Icon  | For a logged-in user, click on the heart icon for a product  | The heart icon should toggle between filled and outlined, indicating adding/removing the product from favorites  | Pass  |
| Favorites Icon - Not Logged In  | Verify the behavior of the favorites icon for a not logged-in user  | The icon should not be interactive, and a login prompt should appear when clicked  | Pass  |
| Product Number  | Verify the pagination controls  | The page should display the correct number of products per page  | Pass  |
| Back to Top Button  | Click on the "Back to Top" button  | The page should scroll to the top  | Pass  |
| Superuser Actions  | Log in as a superuser and check the edit/delete links for a product  | The superuser should see the "Edit" and "Delete" links next to each product  | Pass  |
| Superuser Edit Link  | Click on the "Edit" link for a product  | The superuser should be redirected to the product edit page  | Pass  |
| Superuser Delete Link  | Click on the "Delete" link for a product  | The superuser should be redirected to the product delete confirmation page  | Pass  |
| Responsive Design  | Test the page responsiveness on different devices (desktop, tablet, mobile)  | The page elements should adjust and be displayed correctly on various screen sizes  | Pass  |


### My Favourite Products Page

| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Favorite Products Display  | Access the favorite products page  | The page should display a list of favorite products with their images, names, prices, and categories  | Pass  |
| Remove from Favorites  | Click on the "remove" link for a favorite product  | The product should be removed from the list of favorite products, and the link should change to the "Add to Favorites" link  | Pass  |
| Add to Favorites  | Click on the "My Fav" link for a non-favorite product  | The product should be added to the list of favorite products, and the link should change to the "remove" link  | Pass  |
| Empty Favorites  | Ensure there are no favorite products in the user's session  | A message should be displayed indicating that the favorite products session is empty, along with a "Back to Shopping" button that redirects to the products page  | Pass  |
| Back to Shopping Button  | Click on the "Back to Shopping" button  | The button should redirect the user to the products page  | Pass  |
| Responsive Design  | Test the page's responsiveness on different devices (desktop, tablet, mobile)  | The page elements should adjust and be displayed correctly on various screen sizes  | Pass  |


### Products Details Page

| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Product Details Display  | Access the product details page for a specific product  | The page should display the product's image, name, price, category, description, quantity input, "Add to Bag" button, and "Keep Shopping" button  | Pass  |
| Product Image  | Verify if the product image is displayed correctly  | The product image should be displayed, and it should either show the product image or a default placeholder image  | Pass  |
| Product Name  | Verify if the product name is displayed correctly  | The name of the product should be displayed as specified in the data  | Pass  |
| Product Price and Unity  | Verify if the product price and unity are displayed correctly  | The price per unity of the product should be displayed as specified in the data  | Pass  |
| Product Category  | Verify if the product category is displayed correctly  | If the product has a category, the category should be displayed with its friendly name  | Pass  |
| Edit and Delete (Superuser)  | Check if the "Edit" and "Delete" links are displayed for a superuser  | If the user is a superuser, the "Edit" and "Delete" links should be displayed  | Pass  |
| Edit Link  | Click on the "Edit" link  | The link should redirect the user to the product edit page for the specific product  | Pass  |
| Delete Link  | Click on the "Delete" link  | The link should open a confirmation dialog to delete the product, and upon confirmation, the product should be deleted  | Pass  |
| Product Description  | Verify if the product description is displayed correctly  | The description of the product should be displayed as specified in the data  | Pass  |
| Quantity Input  | Verify if the quantity input is displayed correctly  | The input should be displayed with default value "1" and minimum value "1"  | Pass  |
| Increment Quantity  | Click on the "Increment" button for quantity input  | The value in the quantity input should increase by 1, and the "+" button should be disabled if the value reaches 99  | Pass  |
| Decrement Quantity  | Click on the "Decrement" button for quantity input  | The value in the quantity input should decrease by 1, and the "-" button should be disabled if the value reaches 1  | Pass  |
| Add to Bag  | Click on the "Add to Bag" button  | The product should be added to the user's shopping bag with the selected quantity, and a success message should be displayed  | Pass  |
| My Favorites  | Verify if the "My Favorites" heart icon is displayed correctly  | If the product is favorited by the user, a filled heart icon should be displayed; otherwise, an empty heart icon should be displayed  | Pass  |
| Toggle Favorites  | Click on the "My Favorites" heart icon  | If the product is favorited, it should be removed from the user's favorites; if it's not favorited, it should be added to the user's favorites  | Pass  |
| Keep Shopping Button  | Click on the "Keep Shopping" button  | The button should redirect the user to the products page  | Pass  |
| Responsive Design  | Test the page's responsiveness on different devices (desktop, tablet, mobile)  | The page elements should adjust and be displayed correctly on various screen sizes  | Pass  |


### Shopping Bag Page

| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Shopping Bag Display  | Access the shopping bag page  | The page should display a summary of the products in the bag, including product images, names, prices, quantities, and subtotals. The total price and "Keep Shopping" and "Secure Checkout" buttons should also be displayed.  | Pass  |
| Bag Items Display  | Verify if bag items are displayed correctly  | Each bag item should be displayed with its image, name, SKU, price, unity, quantity input, update button, and remove button.  | Pass  |
| Product Image  | Verify if the product image is displayed correctly  | The product image should be displayed for each bag item. If no image is available, a default placeholder image should be displayed  | Pass  |
| Quantity Input  | Verify if the quantity input is displayed correctly  | The input should display the quantity of each product and allow the user to adjust it.  | Pass  |
| Increment Quantity  | Click on the "Increment" button for quantity input  | The value in the quantity input should increase by 1, and the "+" button should be disabled if the value reaches 99.  | Pass  |
| Decrement Quantity  | Click on the "Decrement" button for quantity input  | The value in the quantity input should decrease by 1, and the "-" button should be disabled if the value reaches 1.  | Pass  |
| Update Quantity  | Click on the "Update" link for a bag item  | The quantity of the bag item should be updated based on the value in the quantity input. The subtotal and total should be recalculated.  | Pass  |
| Remove Item  | Click on the "Remove" link for a bag item  | The bag item should be removed from the bag, and the subtotal and total should be recalculated.  | Pass  |
| Bag Total  | Verify if the bag total is displayed correctly  | The total price of all bag items should be displayed correctly.  | Pass  |
| Keep Shopping Button  | Click on the "Keep Shopping" button  | The button should redirect the user to the products page.  | Pass  |
| Secure Checkout Button  | Click on the "Secure Checkout" button  | The button should redirect the user to the checkout page.  | Pass  |
| Responsive Design  | Test the page's responsiveness on different devices (desktop, tablet, mobile)  | The page elements should adjust and be displayed correctly on various screen sizes.  | Pass  |

### Checkout Page

| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Checkout Page Display  | Access the checkout page  | The page should display a form for user details, an order summary with product images, names, quantities, and subtotals, and a payment section with Stripe card input  | Pass  |
| Order Summary  | Verify if the order summary is displayed correctly  | The order summary should display each bag item with its image, name, quantity, and subtotal. The total, delivery cost, and grand total should also be displayed correctly.  | Pass  |
| Product Image  | Verify if the product image is displayed correctly  | The product image should be displayed for each item. If no image is available, a default placeholder image should be displayed  | Pass  |
| Subtotal Display  | Verify if the subtotal in the order summary is displayed correctly  | The subtotal for each product in the order summary should be calculated and displayed correctly.  | Pass  |
| Order Total Display  | Verify if the order total is displayed correctly  | The order total in the order summary should be calculated and displayed correctly.  | Pass  |
| Delivery Cost Display  | Verify if the delivery cost is displayed correctly  | The delivery cost in the order summary should be calculated and displayed correctly based on the order total.  | Pass  |
| Grand Total Display  | Verify if the grand total is displayed correctly  | The grand total in the order summary should be calculated and displayed correctly as the sum of the order total and delivery cost.  | Pass  |
| User Details Form  | Verify if the user details form is displayed correctly  | The form fields for full name, email, phone number, country, postcode, town/city, and street address should be displayed correctly.  | Pass  |
| Form Autofocus  | Verify if the full name field has autofocus  | The full name field should be focused automatically when the page is loaded.  | Pass  |
| Save Info Checkbox  | Verify if the "Keep this delivery information in my profile" checkbox is displayed correctly  | The checkbox should be displayed, and if the user is authenticated, it should be checked by default. If not authenticated, a message should inform users about creating an account or logging in to save information  | Pass  |
| Stripe Card Element  | Verify if the Stripe card element is displayed correctly  | The Stripe card input field should be displayed for users to input their payment details  | Pass  |
| Complete Order Button  | Click on the "Complete Order" button  | If the form is valid and all required details are provided, the order should be processed, and the user should be redirected to a success page.  | Pass  |
| Form Submission Error  | Submit the form with invalid or missing data  | If any required field is missing or invalid, an error message should be displayed, and the form submission should not be allowed.  | Pass  |
| Adjust Bag Button  | Click on the "Adjust Bag" button  | The button should redirect the user to the shopping bag page.  | Pass  |
| Payment Amount Warning  | Verify if the payment amount warning is displayed correctly  | A warning message should inform users that their card will be charged the correct grand total.  | Pass  |
| Confirmation Email  | Check if a confirmation email is sent  | After a successful order placement, a confirmation email should be sent to the user's provided email address.  | Pass  |


### Checkout Success Page

| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Success Page Display  | Access the checkout success page  | The page should display the order details, thanking the user for their order. It should show the order number, order date, order items, delivering address, billing information, order total, delivery cost, and grand total.  | Pass  |
| Back to Profile Button  | Click on the "Back to Profile" button  | If the order was accessed from the user profile, clicking the button should redirect the user to their profile page.  | Pass  |
| Explore Offers Button  | Click on the "Explore the most recent   | If the order was not placed from the user's profile, clicking the button should redirect the user to the products page with a specific category filter.  | Pass  |


### Add Product Page

| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Accessing the Page  | Log in as a superuser and access the "Add Product" page  | The page should load without errors, displaying the form to add a new product.  | Pass  |
| Form Display  | Verify if the product form is displayed correctly  | The form should include fields for product name, description, category, price, stock, image, and unity.  | Pass  |
| Form Fields  | Verify if all required form fields are present  | All mandatory fields (marked with an asterisk) should be present in the form.  | Pass  |
| Adding a New Product  | Fill out the form with valid information and submit it  | After submitting the form, the user should be redirected to the product detail page of the newly added product, and a success message should be displayed.  | Pass  |
| Form Validation  | Attempt to submit the form with missing or incorrect information  | If any required field is missing or incorrect, an error message should be displayed, and the form should not be submitted.  | Pass  |
| Cancel Button  | Click on the "Cancel" button  | Clicking the "Cancel" button should redirect the user back to the product list page.  | Pass  |
| Adding a Product as a Non-Superuser  | Log in as a non-superuser and access the "Add Product" page  | A message should be displayed informing the user that this action is limited to store owners only. The user should be redirected to the home page.  | Pass  |


### Edit Product Page

| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Accessing the Page  | Log in as a superuser and access the "Edit Product" page  | The page should load without errors, displaying the form to edit the selected product  | Pass  |
| Form Display  | Verify if the product form is displayed correctly  | The form should display fields populated with the existing product's information for editing.  | Pass  |
| Form Fields  | Verify if all required form fields are present  | All mandatory fields should be present in the form, populated with the current product's information.  | Pass  |
| Editing Product  | Make changes to the form and submit it  | After submitting the form, the user should be redirected to the product detail page of the edited product, and a success message should be displayed.  | Pass  |
| Form Validation  | Attempt to submit the form with missing or incorrect information  | If any required field is missing or incorrect, an error message should be displayed, and the form should not be submitted.  | Pass  |
| Cancel Button  | Click on the "Cancel" button  | Clicking the "Cancel" button should redirect the user back to the product list page.  | Pass  |
| Editing a Product as a Non-Superuser  | Log in as a non-superuser and access the "Edit Product" page  | A message should be displayed informing the user that this action is limited to store owners only. The user should be redirected to the home page.  | Pass  |

### Delete Product

| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Accessing Delete  | Log in as a superuser and access the Delete Product option  | The user should be able to access the page without errors. The page should display a confirmation message asking if the user wants to delete the selected product.  | Pass  |
| Confirm Delete  | Click on the Delete button to confirm product deletion  | After clicking the "Delete" button, the product should be deleted from the database. The user should be redirected to the product list page with a success message indicating that the product was deleted.  | Pass  |
| Cancel Deletion  | Click on the Cancel button  | Clicking the Cancel button should redirect the user back to the product detail page of the product, and no changes should be made to the product.  | Pass  |
| Deleting a Product as a Non-Superuser  | Log in as a non-superuser and attempt to access the Delete Product  | A message should be displayed informing the user that this action is limited to store owners only. The user should be redirected to the home page.  | Pass  |


### Django All Auth Pages
| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Sign Up  |  |  |  |
| Log in link  | Click  | Redirect to login page  | Pass  |
| Username field  | Leave empty  | On submit: form won't submit  | Pass  |
| Username field  | Leave empty  | Error message displays  | Pass  |
| Username field  | Insert correct format  | On submit: form submit  | Pass  |
| Username field  | Insert duplicate username  | On submit: form won't submit  | Pass  |
| Username field  | Insert duplicate username  | Error message displays  | Pass  |
| Email field  | Insert incorrect format  | On submit: form won't submit  | Pass  |
| Email field  | Insert incorrect format  | Error message displays  | Pass  |
| Email field  | Insert correct format  | On submit: form submit  | Pass  |
| Email field  | Leave empty  | On submit: form submit  | Pass  |
| Email field  | Insert duplicate email  | On submit: form won't submit  | Pass  |
| Email field  | Insert duplicate email  | Error message displays  | Pass  |
| Password field  | Insert incorrect format  | On submit: form won't submit  | Pass  |
| Password field  | Insert incorrect format  | Error message displays  | Pass  |
| Password field  | Passwords don't match  | On submit: form won't submit  | Pass  |
| Password field  | Passwords don't match  | Error message displays  | Pass  |
| Password field  | Insert correct format  | 	On submit: form submit  | Pass  |
| Sign Up button (form valid)  | Click  | Form submit  | Pass  |
| Sign Up button (form valid)  | Click  | Redirect to home page  | Pass  |
| Sign Up button (form valid)  | Click  | Success message confirming login appears  | Pass  |
| Sign Up button (form valid)  | Click  | Success message fades after 3 seconds  | Pass  |
| Log in  |  |  |  |
| Sign up link  | Click  | 	Redirect to sign up page  | Pass  |
| Username field  | Leave empty  | On submit: form won't submit  | Pass  |
| Username field  | Leave empty  | 	Error message displays  | Pass  |
| Username field  | Insert wrong username  | On submit: form won't submit  | Pass  |
| Username field  | Insert wrong username  | Error message displays  | Pass  |
| Password field  | Leave empty  | On submit: form won't submit  | Pass  |
| Password field  | Leave empty  | Error message displays  | Pass  |
| Password field  | Insert wrong password  | On submit: form won't submit  | Pass  |
| Password field  | Insert wrong password  | Error message displays  | Pass  |
| Login button (form valid)  | Click  | Form submit  | Pass  |
| Login button (form valid)  | Click  | Redirect to home page  | Pass  |
| Login button (form valid)  | Click  | Success message confirming login appears  | Pass  |
| Login button (form valid)  | Click  | Success message fades after 3 seconds  | Pass  |
| Log Out Confirmation  |  |  |  |
| Logout button  | Click  | Content  | Content  |


## Admin Panel Testing
* Products, Category are successfully added in the admin panel.

* Admins have full access to CRUD functionality for all products and categories in the admin panel.

* Admins also have full moderation over the user.

* Django Allauth works successfully and the admins can change users permissions.


## Browser Testing
* The Website was tested on Google Chrome, Firefox, Safari browsers with no issues noted.


## Bugs

### Fixed Bugs

* Herokuapp URL page not displaying on am I responsive frames. Error showing in the mock screens was **recipes-for-me-herokuapp.com refused to connect** this [link](https://code-institute-room.slack.com/archives/C026PTF46F5/p1669748686922019?thread_ts=1669744943.768489&cid=C026PTF46F5) was very helpful to fix the issue.

* Allauth unable to fund templates derectory 
/home/gitpod/.pyenv/versions/3.11.1/bin/python: can't open file '/workspace/boutique_ado/help': [Errno 2] No such file or directory

To find the location of the allauth templates in Django, you can follow these steps:

- Make sure you are in the root directory of your Django project.
- Open a terminal or command prompt in that directory.
- Run the following command to find the location of the allauth templates:

python manage.py shell -i python -c "import allauth; print(allauth.__path__)"

### Unfixed Bugs
No Unfixed Bugs left behind ;)


## Code Validation

### W3C HTML VALIDATION
All html pages have been run through the [W3C HTML Validator](https://validator.w3.org/) and the below results were returned.

**-HTML Checker**
No Errors Found
45 Warnings Most are from Javascript tags which does not affecte the page.

**- add-product.html**
* Erros = None.
![test html](Docs/Readme_images/testing/add_product_page_html.png)

**- bag.html**
* Erros = None.
![test html](Docs/Readme_images/testing/bag_page_html.png)

**- checkout.html**
* Erros = None.
![test html](Docs/Readme_images/testing/checkout_page_html.png)

**- checkout-success.html**
* Erros = None.
![test html](Docs/Readme_images/testing/checkout_success_page_html.png)

**- edit-product.html**
* Erros = None.
![test html](Docs/Readme_images/testing/edit_product_page_html.png)

**- feedback.html**
* Erros = None.
![test html](Docs/Readme_images/testing/feedback_page_html.png)

**- home.html**
* Erros = None.
![test html](Docs/Readme_images/testing/landing_page_html.png)

 **- favourites.html**
* Erros = None.
![test html](Docs/Readme_images/testing/my_favourites_page_html.png)

**- profile.html**
* Erros = None.
![test html](Docs/Readme_images/testing/my_profile_page_html.png)

**- product-details.html**
* Erros = None.
![test html](Docs/Readme_images/testing/product_details_page_html.png)

**- product.html**
* Erros = None.
![test html](Docs/Readme_images/testing/product_page_html.png)

**- registration.html**
* Erros = None.
![test html](Docs/Readme_images/testing/registratio_page_html.png)

**- signin.html**
* Erros = None.
![test html](Docs/Readme_images/testing/sign_in_page_html.png)

**- newsletter.html**
* Erros = None.
![test html](Docs/Readme_images/testing/newsletter_page.png)

**- newsletter.html**
* Erros = None.
![test html](Docs/Readme_images/testing/return_box_page.png)

All pages within the project have undergone thorough validation using an HTML checker to ensure their compliance with standards. 

Overall The validation process yielded positive results and no erros.

## Jigsaw CSS VALIDATION
No errors or warnings are returned when passing the styles.css through the [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/).

![css testing image](Docs/Readme_images/testing/css_checker.png)

## JSHint JavaScript VALIDATION
All the Scripts used in FF2T have been run through the [JSHint Javascript Validator](https://jshint.com/) and they return no errors.

![jshint java testing](Docs/Readme_images/testing/js_testing.png)


## CI Python Linter Python VALIDATION 
All the main Python files were run through the [CI Python Linter Validator](https://pep8ci.herokuapp.com/) with no errors returned.

**- home views.py**
* Erros = None.
![test forms.py](Docs/Readme_images/testing/home_view.png)

**- home urls.py**
* Erros = None.
![test forms.py](Docs/Readme_images/testing/home_urls.png)


**- profile views.py**
* Erros = None.
![test forms.py](Docs/Readme_images/testing/profile_view.png)

**- profile forms.py**
* Erros = None.
![test forms.py](Docs/Readme_images/testing/profile_form.png)

**- profile models.py**
* Erros = None.
![test models.py](Docs/Readme_images/testing/profile_model.png)

**- profile urls.py**
* Erros = None.
![test urls.py](Docs/Readme_images/testing/profile_urls.png)


**- bag context.py**
* Erros = None.
![test forms.py](Docs/Readme_images/testing/bag_context.png)

**- bag urls.py**
* Erros = None.
![test urls.py](Docs/Readme_images/testing/bag_urls.png)

**- bag views.py**
* Erros = None.
![test views.py](Docs/Readme_images/testing/bag_view.png)


**- product forms.py**
* Erros = None.
![test forms.py](Docs/Readme_images/testing/products_form.png)

**- product urls.py**
* Erros = None.
![test urls.py](Docs/Readme_images/testing/products_urls.png)

**- product views.py**
* Erros = None.
![test views.py](Docs/Readme_images/testing/product_view.png)

**- products admin.py**
* Erros = None.
![test forms.py](Docs/Readme_images/testing/products_admin.png)


**- checkout admin.py**
* Erros = None.
![test forms.py](Docs/Readme_images/testing/checkout_admin.png)

**- checkout forms.py**
* Erros = None.
![test forms.py](Docs/Readme_images/testing/checkout_forms.png)

**- chekcout models.py**
* Erros = None.
![test models.py](Docs/Readme_images/testing/checkout_model.png)

**- chekcout urls.py**
* Erros = None.
![test urls.py](Docs/Readme_images/testing/checkout_urls.png)

**- checkout views.py**
* Erros = None.
![test views.py](Docs/Readme_images/testing/checkout_views.png)

**- checkout signals.py**
* Erros = None.
![test forms.py](Docs/Readme_images/testing/checkout_signals.png)


## LIGHTHOUSE REPORTS
FF2T app home page have been tested for Performance, Accessibility, Best Practices and SEO using [Lighthouse Chrome Developer Tool](https://developer.chrome.com/docs/lighthouse/overview/).
The lighthouse scores look very good overall, with some things that could be improved. A future implementation would be to convert all images to the webp format.

**- Home Page**
* Performance = 64
* Accessibility = 89
* Best Practices = 100
* SEO = 100
![lighthouse test](Docs/Readme_images/testing/lighthouse_result.png)

