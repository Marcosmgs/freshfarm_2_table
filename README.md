# FF2T - Fresh Farm 2 Table
### Where Freshness Comes to Your Doorstep

![Am I Responsive](Docs/Readme_images/am_I_responsive.png)

FF2T is a meticulously crafted web application using Django, designed for individuals who prioritize the freshness, authenticity, and sustainability of their food. Whether you're an advocate for locally sourced, organic produce or you're intrigued by the journey from farm to plate, FF2T simplifies your experience.

In a world where convenience often trumps healthy choices, FF2T stands as a beacon for those seeking health and convenience in harmony. Our platform bridges the gap between busy lives and nutritious living, offering you a curated selection of fresh produce delivered straight to your doorstep. Effortless, and eco-conscious!

- - -


## Table Of Contents
* [User Experience (UX)](#user-experience-ux)
  * [User Stories](#user-stories)
  * [Design](#design)
  * [Colour Scheme](#-colour-scheme)
  * [Typography](#-typography)
  * [Imagery](#-imagery)
  * [Wireframes](#-wireframes)
* [Agile Methodology](#agile-methodology)
* [Data Model](#data-model)
* [Features](#features)
  * [Header](#header)
  * [Footer](#footer)
  * [Home Page](#home-page)

- - -

## User Experience (UX)

Fresh Farm 2 Table is a hub for a diverse community sharing a passion for fresh, sustainable, and mindful consumption. Our audience includes health advocates looking for nutrient rich diets, sustainability enthusiasts backing eco friendly farming, Families and Individuals valuing the convenience of doorstep delivery for fresh produce, freeing up time from grocery shopping, local community supporters fostering resilient food systems and culinary explorers experimenting with seasonal delights.

Here, these individuals unite to celebrate quality, health, and eco-friendly choices.

### User Stories

These user stories served as a starting point and can be expanded upon features implementations into the project. They help capture the primary functionalities and actions that users and administrators would expect from our e-commerce application.

**Viewing and Navigation** 

- As a Client, I can View a list of products, So I that can Select and explore the available options easily to meet my needs and preferences.
- As a Client, I can View individual product details, including descriptions, images and prices, So I that can Make informed purchasing decisions by accessing comprehensive information about each product.
- As a Client, I can Quickly identify deals and special offers, such as discounts, promotions, or bundled packages, So that I can Take advantage of saving opportunities by being informed about the latest deals.
- As a Client, I can View the total of my purchases at any time, So that I can Keep track of my expenses and budget effectively by easily accessing the total amount spent on purchases.

**Registration and User accounts**

-	As a Site User, I can Easily register for an account to have a personal account, So that I can Access personalised features and make use of the full functionality of the website.
-	As a Site User, I can Easily log in or log out to access my personal account, So that I can Securely access my account and manage my information and preferences.
-	As a Site User, I can Easily recover my password to access to my account, So that I can Regain access to my account in case I forget or lose my password.
-	As a Site User, I can Receive an email confirmation to verify my account, So that I can Ensure the security and validity of my account and protect against unauthorised access.
-	As a Site User, I can Have a personalised profile, So that I can view my personal order history, order confirmations and save my payment information to save time during the checkout process.
-	As a Site User, I can View and manage a list of my favourite products, So I that can Easily access them for future purchases.

**Sorting and Searching products**

-	As a Client, I can Sort a list of available products, So that I can Identify the best rated products, prices and easily sort products by categories to best meet my preferences and needs.
-	As a Client, I can Sort a specific category of products, So that I can Find the best-rated, best-priced, or alphabetically sorted products within that category.
-	As a Client, I can Sort multiple categories of products simultaneously, So that I can Find the best-priced products across various categories such as “FRESH HARVEST” and “FRESH FARM BOX”.
- As a Client, I can Search for a product by name or description, So that I can Quickly find specific products I'm interested in, saving me time and enhancing the overall shopping experience.
-	As a Client, I can Easily see what I've searched for and the number of results, So that I can Quickly decide on the most suitable options.

**Purchasing and checkout**

- As a Client, I can Easily select the quantity of a product while purchasing it So that I can Ensure I do not mistakenly choose the wrong quantity or product ensuring an accurate order.
- As a Client, I can View the items in my bag to be purchased So that I can Have a clear overview of the items in my bag, allowing me to review my purchase and confirm the total cost.
- As a Client, I can Adjust the quantity of individual items in my bag So that I can Easily make changes to my purchase before checkout, allowing me to fine-tune my purchase.
- As a Client, I can Easily enter my payment information So that I can Check out quickly, saving time and effort.
- As a Client, I can Feel that my personal and payment info are safe and secure So that I can Provide the information needed to make a purchase, ensuring the confidentiality and protection of my sensitive data.
- As a Client, I can View an order confirmation after checkout** So that I can Receive immediate feedback and confirmation of my order, allowing me to review the details and ensure the accuracy of my purchase.
- As a Client, I can Receive an email confirmation after checking out** So that I can Have a documented record of my order, accessible through email, for future reference or any necessary follow-up.

**Admin Stories**

- As an Admin, I can Add new products to the platform, So that I can Ensure that the selection is up-to-date and reflects the available offerings.
- As an Admin, I can Update or Edit products in the platform, So that I can Manage the product catalog effectively.
- As an Admin, I can Remove products from the platform, So that I can Manage the product catalog effectively.

### Design
Fresh Farm 2 Table is rooted in simplicity and friendly UI. Our interface has been meticulously crafted to facilitate seamless navigation, allowing users to effortlessly explore the application and concentrate on what truly matters. With a minimalist and intuitive layout, we've prioritized clarity and ease of use, ensuring that your journey through Fresh Farm 2 Table is both engaging and intuitive. 

Inspired by the exceptional design principles exemplified in projects like the [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) by Code Institute, we've crafted a platform that harmonizes aesthetics with functionality.

#### **-COLOUR SCHEME**

Color theme from Adobe Color

The color scheme of Fresh Farm 2 Table, inspired by the vibrant palette of bananas, has been meticulously choosen to infuse the platform with a sense of freshness, comfort, and organic vibrancy.

![Color Scheme Image](Docs/Readme_images/colour_palet.png)

There are strong contrast between background colors and text throughout our web application, ensuring maximum readability and usability for all users.
 
#### **-TYPOGRAPHY**
 
Google Fonts was used to import the chosen fonts below for use in the application.

CSS rules to specify families

font-family: 'Lato', sans-serif; (main font)

![Font Lato](Docs/Readme_images/font_lato.png)

font-family: 'Open Sans', sans-serif; (secondary font)

![Font Open Sans](Docs/Readme_images/font_open_san.png)

        
#### **-IMAGERY**

The homepage background image used within the site has been chosen from [pexel](https://www.pexels.com) taken by the photographer bellow:

Photo by: 

- [Mikhail Nilov](https://www.pexels.com/@mikhail-nilov/)

The Logo image used within the heading site has been taken from [Freesvg](https://freesvg.org/shopping-basket-vector-illustration)

The product imagery uploaded by the site admin comes from a Dataset from [Kaggle](https://www.kaggle.com)

#### **-WIREFRAMES**

Wireframes were created using [Figma](https://www.figma.com/)

<details>
<summary>Home Page - Desktop & Mobile</summary>

 ![Landing Page Frame](Docs/Readme_images/wireframes/home_page_frame.png))

</details>

<details>
<summary>Product List Page</summary>

 ![Product List View](Docs/Readme_images/wireframes/product_list_view_page_frame.png)

</details>

<details>
<summary>Register My Account Page</summary>

 ![Register Account Frame](Docs/Readme_images/wireframes/register_my_account_page_frame.png)

</details>

<details>
<summary>Login Page</summary>

 ![login_page_frame](Docs/Readme_images/wireframes/login_my_account_page_frame.png)

</details>

<details>
<summary>Logout Page</summary>

 ![logout_page_frame](Docs/Readme_images/wireframes/logout_my_account_page_frame.png)

</details>

<details>
<summary>Product Details View Page</summary>

 ![product details view](Docs/Readme_images/wireframes/product_details_view_page_frame.png)

</details>

<details>
<summary>My Profile Page</summary>

 ![my profile page frame](Docs/Readme_images/wireframes/my_profile_my_account_page_frame.png)

</details>

<details>
<summary>My Favourite Page</summary>

 ![my favourite product](Docs/Readme_images/wireframes/my_favourite_my_account_page_frame.png)

</details>

<details>
<summary>My Shopping Bag Page</summary>

 ![my shopping bag](Docs/Readme_images/wireframes/my_shopping_bag_page_frame.png)

</details>

<details>
<summary>Checkout Secure Page</summary>

 ![checkout page](Docs/Readme_images/wireframes/checkout_secure_page_frame.png)

</details>

<details>
<summary>Checkout Success Page</summary>

 ![checkout success](Docs/Readme_images/wireframes/checkout_success_page_frame.png)

</details>


## Agile Methodology

Github project was used to manage the development process of this project using an agile approach. 
Find the link to the Github project [here](https://github.com/users/Marcosmgs/projects/5/views/1) 

The  FF2T User Stories is documented within the Github project. A Github issue was created for each user stories and allocated to the Project. 
The user stories were moved accordingly the application was been built.  


## Data Model

In the Fresh Farm 2 Table project, the data model utilizes a set of function based views to efficiently manage various aspects of the application functionality. These views serve as the core logic for handling interactions with the data model. Each function view correspond to a specific user action, ensuring a organized structure.

[Django AllAuth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication. 
This powerful authentication system provides a seamless and secure user login and registration process, enhancing the overall user experience.

Category model serves as a fundamental building block, categorizing products and enabling easy navigation. With attributes name and friendly_name, this model ensures a structured representation of product categories, both internally and in the UI.

Product model is at the heart of the application, representing individual items available for purchase.
The is_favorited field, established as a Many-to-Many relationship with the User model, facilitates the tracking of users' favorite products.

UserProfile model extend the built-in User model provided by Django. This model provide an UX convenience by pre filling delivery information and connecting orders to user profiles.

Order model is central to the e-commerce. This model incorporates a unique order identifier generated using UUID, ensuring order differentiation. 
Complementing the Order model, the OrderLineItem model represents individual items within an order. This model calculates the total cost for each line item and adjusts the overall order total accordingly, ensuring accurate billing.

The ER diagram below shows the schemes for each of the models and how they are related.

![ER Diagram Image](Docs/Readme_images/er_model_diagram.png)

Entity relationship diagram was created using [Figma](https://www.figma.com/).


## Features

#### **Header**

**- Deals Banner**
* The banner fixed-top positioning ensures that the message is displayed at the very top of every page.
* By displaying "Free delivery" offer throughout the application, users are consistently reminded of the benefit they can avail.
* Positively influence user behavior, prompting them to add more items to their bag to qualify for the promotion.
![Nav Banner](Docs/Readme_images/features/offer_banner.png)

**- Header Bar**
* The header bar in FF2T provides convenient access to different sections of the web application
* The header bar is responsive and adapts to different screen sizes.
![Non Reg User](Docs/Readme_images/features/non_reg_user_menu.png)
* On smaller displays, such as mobile devices, the header transforms navigation menu into a hamburger menu and turn the search bar into a collapsible navigation menu, ensuring easy navigation and saving valuable screen space.
![Non Reg User small](Docs/Readme_images/features/small_menu_non_login_user.png)
* When user is logged in the header bar features my favourite functionallity for registered users.
* For superusers, the header includes an additional link for product management.
![Reg user small](Docs/Readme_images/features/small_menu_logged_user.png)
* The header begins with the branding element, featuring the application's logo and name
* Users can access their account related actions such as logging in, registering, viewing their profile, and managing their favorite products.
* header provides users with a summary of their shopping bag, including the total amount spend.
![Logged User Menu](Docs/Readme_images/features/logged_user_menu.png)

**- Search Bar**
* The header bar in FF2T provides convenient access to different sections of the web application.
* The search query is related with name and product description to ensure quality results.
![Non Reg User](Docs/Readme_images/features/search_bar.png)

**- Main Navigation Bar**
* Provides users with structured and easy access to all products sections and categories, ensuring efficient navigation and rifined exploration of content.
* By categorizing content and providing dropdown menus, users can easily navigate to the sections of the application that interest them, leading to more focused exploration.
![Main Nav Menu](Docs/Readme_images/features/navigation_menu.png)
* On smaller displays, such as mobile devices, the header transforms navigation menu into a hamburger menu, ensuring easy navigation and saving valuable screen space.
* Home Page link will be displayed in smaller screens to avail a back to landing page option in smaller screens.
![Main Nav Menu](Docs/Readme_images/features/nav_menu_small.png)
