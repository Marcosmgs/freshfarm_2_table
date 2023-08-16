## Table of Contents
* [Manual Testing](#manual-testing)
  * [Navigation](#navigation)
  * [Index Page](#index-page)
  * [My Profile Page](#my-profile-page)
  * [Product List Page](#product-list-page)
  * [My Favourite Products Page](#my-favourite-products)
  * [Shopping Bag Page](#shopping-bag-page)
  * [Checkout Page](#shopping-bag-page)
  * [Checkout Success Page](#checkout-success-page)
  * [Add Recipe Page](#add-recipe-pagewhen-the-user-is-authenticated)
  * [Edit Recipe](#edit-recipewhen-the-user-is-authenticated)
  * [Delete Recipe](#delete-recipewhen-the-user-is-authenticated)
  * [Django All Auth Pages](#django-all-auth-pages)
  * [Admin panel](#admin-panel)
* [Browser Testing](#browser-testing)
* [Bugs](#bugs)
  * [Fixed Bugs](#fixed-bugs)
  * [Unfixed Bugs](#unfixed-bugs)
* [Code Validation](#code-validation)
  * [W3C HTML VALIDATION](#w3c-html-validation)
  * [Jigsaw CSS VALIDATION](#jigsaw-css-validation)
  * [JSHint JavaScript VALIDATION](#jshint-javascript-validation)
  * [CI Python Linter Python VALIDATION](#ci-python-linter-python-validation)
  * [LIGHTHOUSE REPORTS](#lighthouse-reports)

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






| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Message  | Check  | The  | Pass  |


