![logo](https://res.cloudinary.com/millermayhem/image/upload/v1661771501/Miller%20Creative%20Site/LOGO_MILLER_REGULAR-01_ycdyph.png)

# Portfolio Project 5 - Miller Creative
***

![mockup](https://res.cloudinary.com/millermayhem/image/upload/v1661777068/Miller%20Creative%20Site/Miller_Screens_mockup_sppssu.png)
##  [Visit the site on Heroku](https://miller-creative.herokuapp.com/)

My website presents Miller Creative Graphic Designer. Based in Auchterarder, Perthshire, Scotland. Users will be 
able to find information on services I offer, make a purchase in the shop, create an account, make an enquiry and sign up to receive updates and offers. 
The site will contain featured work from past jobs which will be refreshed on a regular basis.
Users will be able to amend their account information as required. 

This is a responsive full stack data model web application structured using Django and Bootstraps and featuring authentication and permissions features.  

Contact information can be found on the contact page under the contact form. Links to social media pages are in the footer.
Site navigation is via the off canvas menu as well as nav links at the bottom of each page.

Aesthetically, I wanted it minimal, black and clean. I like the use of opacity boxes for text backgrounds and used full height background images
which look great.

***

# Table of Contents

- [Website Objectives](#website-objectives)
  - New User Benefits
  - Returning User Advantages
- [Website Layout](#website-layout)
- [Wireframes](#wireframes)
- [Aesthetics](#aesthetics)
  - Colour Palette
  - Fonts
  - Images
- [Features](#features)
  - Navigation Bar
  - Header
  - Information Section
  - Thumbnail Images
  - Owner Information
  - Footer
  - inspiration Gallery
  - Prices
  - User Authentication - Register, Login and Logout
  - Make A Booking
  - My Bookings
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - Functionality Testing
  - Compaitibility Testing
  - Performance testing
- [Code Validation](#code-validation)
- [Deployment](#deployment)
- [Credits](#credits)


***

# Website Objectives

The primary function of this website is to promote Miller Creative and boost awareness and sales.
Presentation of essential information such as services, contact details, past work is also a big factor. The business has only been promoted through
social media pages but now a more professional look can be portrayed.
The inclusion of a contact form gives customers an easy way to get in touch. 
I also want to collect web addresses to promote the business with offers and updates.

## New User Benefits

- Obtain information on the business
- Find contact details
- View gallery images of past work
- Access the companies social media sites
- Be introduced to us
- Create an account
- Make online purchses for certain products
- sign up for offers and news
- visit sites of companies we have previously worked for

## Returning User Advantages

- Edit account information
- See the ever changing image gallery updated regulalry by site admin
- Refresh knowledge on the companies services
- Access social media accounts to leave feedback on services
- See previous orders in the account section of the site
- Make further enquiries for services through the contact page
- 

***

# Website Layout

The wireframe layouts were created using Adobe Illustrator. 
It has been desinged to be clean, slick, minimal, professional and as user friendly as possible with the use of simple site navigation links.
Accessibility has been carefully considered with the use of cointrasting colours for borders and font colours. Alt text equivalents for the visually immpared have also been included. 
The site is responsive for all screen sizes and tailored to suit each. The user experince will be smooth and satisfying accros all devices. 

# Wireframes

![wireframe](https://res.cloudinary.com/millermayhem/image/upload/v1661778448/Miller%20Creative%20Site/Miller_WF_Master-01_zwfwpc.png)

# Aesthetics

The overall look of the site was created with the aim of being clean, slick, professional, modern and black.

A black theme was chosen to match the brand styling of the bsuiness. I customised background images with photoshop and used customised mockups throughout 
the site to advertise my work. 

I wanted to add little aesthetically pleasing features to catch the eye so I included a rotating company logo in the top left of the site.
I also included a parallax image in the index page and full background images around the diffefrent pages of the site.

I really like the look of content opacity backgrounds over the top of background images so I have included this throughout.

## Colour Palette
- Black
- White
- Olive Hex #B9BD86

## Fonts
- Open Sans - Google Fonts

## Images

Adobe Stock licensed images were used for some backgrounds around the site.

Custom images made up from my previos work were used for backgrounds, examples and placeholders.

One image that I used in a few places was my compliation of some past logos. I thought this was a good way to display my work as much as possible.

[Back to Table of Contents](#table-of-contents)

***

# Features

The website includes multiple pages

- Home
- Featured work
- Shop
- contact
- Product details
- login/lougout/register
- Shopping trolley
- Checkout
- My account
- Product management

Key features are as follows:

## Navigation Bar with Off Canvas

![features-Navbar](https://res.cloudinary.com/millermayhem/image/upload/v1661781865/Miller%20Creative%20Site/Screenshot_2022-08-29_at_14.57.51_ydfbzi.png)
![features-Navbar-offcanvas](https://res.cloudinary.com/millermayhem/image/upload/v1661781865/Miller%20Creative%20Site/Screenshot_2022-08-29_at_15.01.31_zirf2v.png)
![features-Navbar-offcanvas_logged-in](https://res.cloudinary.com/millermayhem/image/upload/v1661781865/Miller%20Creative%20Site/Screenshot_2022-08-29_at_15.02.00_gnxa6y.png)

The Navigation Bar is located at the top of each page and is consitent in style throughout the site. 

A rotating business logo is placed to the left and will navigate you to the home page when clicked.
The burger icon opens the off canvas content which contains navigation links around the site. 
I decided to keep the nav bar fixed to the top of the viewport

Links to each page are included for easy navigation to:
- Home
- Shop
- Featured Work
- Contact
- Register
- Login

And when authenticated

- Home
- Shop
- Featured Work
- Contact
- Product Management
- My Account
- Lougout

![features-Navbar-account](https://res.cloudinary.com/millermayhem/image/upload/v1661782458/Miller%20Creative%20Site/Screenshot_2022-08-29_at_15.13.52_anhdh4.png)

The 'Account' link appears in the middle of the navbar when the user isnt logged in. When clicked it presents a dropdown list with "Register' and 'Login' options.
The shopping basket appears when the user is logged in as purchase can only be made when registered and logged in.

![features-Navbar-account](https://res.cloudinary.com/millermayhem/image/upload/v1661782458/Miller%20Creative%20Site/Screenshot_2022-08-29_at_15.13.33_zchqka.png)

## Header

![features-header](https://res.cloudinary.com/millermayhem/image/upload/v1661782781/Miller%20Creative%20Site/Screenshot_2022-08-29_at_15.19.07_nargsa.png)

The header consists of a split screen layout with a title, information and a 'SHOP NOW' button on the left and a custom image I created on the right. 
The image showcases another bit of my work.

## Subscribe

![features-subscribe](https://res.cloudinary.com/millermayhem/image/upload/v1661783502/Miller%20Creative%20Site/Screenshot_2022-08-29_at_15.28.47_voutan.png)

The subscribe section features a tag line and uses a mailchimp email form to collect emaill address. Gathered email addresses will be used to promote deals and services.

## About

![features-about](https://res.cloudinary.com/millermayhem/image/upload/v1661783714/Miller%20Creative%20Site/Screenshot_2022-08-29_at_15.34.55_bsko70.png)

Information about the business is found here. It gives a quick overview of what we do.

## Featured Companies

![features-companies](https://res.cloudinary.com/millermayhem/image/upload/v1661784006/Miller%20Creative%20Site/Screenshot_2022-08-29_at_15.39.26_z8dznj.png)

The featured comapnies section gives the user a preview of of some previous work. There is a button whcih takes you to the  fetaured work page.
On larger screens, hovering over the company brings up the name and location of the business on an opacity overlay.
Clicking on these companies will take you to their website or social media page.

![features-contact-parallax](https://res.cloudinary.com/millermayhem/image/upload/v1661784236/Miller%20Creative%20Site/Screenshot_2022-08-29_at_15.43.36_khq7rr.png)

On larger screens the parallax feature is present. Aparently this function isnt compatible on smaller screens so I replaced it with a background image.
The button will take the user to the contact page when clicked. Here they will find a contact form which emails miller creative direct. 
Users will also find the company phone number, email address and business address.

## Footer and page links

![features-footer](https://res.cloudinary.com/millermayhem/image/upload/v1661785062/Miller%20Creative%20Site/Screenshot_2022-08-29_at_15.57.22_gjeogl.png)

At the bottom of each page the user will find links to pages around the site including, home, shop, featured work, contact and account.

The footer is very minimal and only contains the copyright and social media icons. This stripped back style fits in with the clean minimal style of the site.

## Featured work page

![features-featured-work](https://res.cloudinary.com/millermayhem/image/upload/v1661785539/Miller%20Creative%20Site/Screenshot_2022-08-29_at_16.05.16_cn8inl.png)
![features-footer](https://res.cloudinary.com/millermayhem/image/upload/v1661785539/Miller%20Creative%20Site/Screenshot_2022-08-29_at_16.04.44_lsdccc.png)

The 'Featured Work' page showcases some previous work that miller creative have done. The cards are generated in the admin panel and are arranged 
in rows of 3. At the top of the page is a heading on an opacity background box which overlaysa customised image from Adobe Stock.
This page will be kept fresh and new work will be displayed with older work being removed.

## Shop

![features-shop](https://res.cloudinary.com/millermayhem/image/upload/v1661785935/Miller%20Creative%20Site/Screenshot_2022-08-29_at_16.11.52_ujy6ns.png)

The shop page gives the user a some information on the online shop products. When clicked link will take you to the relevant page.

![features-product-quantities](https://res.cloudinary.com/millermayhem/image/upload/v1661787439/Miller%20Creative%20Site/Screenshot_2022-08-29_at_16.37.05_n7oyjc.png)
![features-Flyer-sizes](https://res.cloudinary.com/millermayhem/image/upload/v1661787607/Miller%20Creative%20Site/Screenshot_2022-08-29_at_16.39.52_rjeloh.png)
![features-product-quantities](https://res.cloudinary.com/millermayhem/image/upload/v1661787695/Miller%20Creative%20Site/Screenshot_2022-08-29_at_16.41.19_rqn8gt.png)
on these pages the user will be given the option to choose the print quantitiy they are looking for. Once selected and clicked they will
be led to the product detail page.
For flyers the user will be led to choose the size of flyer they want then on to the quantity.

## Product Detail

![features-product-detail-page](https://res.cloudinary.com/millermayhem/image/upload/v1661788001/Miller%20Creative%20Site/Screenshot_2022-08-29_at_16.43.06_t7guy5.png)
When the user isnt logged in they dont have the option to buy the products and the page will look like above.

![features-product-detail-logged-in](https://res.cloudinary.com/millermayhem/image/upload/v1661788002/Miller%20Creative%20Site/Screenshot_2022-08-29_at_16.44.44_dyfvcf.png)
When the user is logged in the buttons appear to add a quantity and either add to bag, go back to shop or go to bag.

## Shopping Trolley

![features-trolley](https://res.cloudinary.com/millermayhem/image/upload/v1661789376/Miller%20Creative%20Site/Screenshot_2022-08-29_at_17.09.21_f2meoe.png)

All the products added will appear in the shopping trolley. This can be access via the button on the product detail page or from the
top nav.
In here the user will be able to adjust quantities and update the trolley. They will also be able to remove products.
The order total is shown and the user can eother go to the secure checkout or back to the shop. 

## Checkout

![features-checkout](https://res.cloudinary.com/millermayhem/image/upload/v1661789966/Miller%20Creative%20Site/Screenshot_2022-08-29_at_17.19.10_ms5kep.png)
![features-checkout-details](https://res.cloudinary.com/millermayhem/image/upload/v1661789974/Miller%20Creative%20Site/Screenshot_2022-08-29_at_17.18.26_jsbirr.png)

Here the user will be shown the order summary with the total price. No adjustments can be made here. 
To proceed woth the order users will complete the information for name, address, phone number and credit card.
to complete the order the button should be clicked or if they want to adjust the bag then that button should be clicked.

## Checkout Success

![features-checout-success](https://res.cloudinary.com/millermayhem/image/upload/v1661790249/Miller%20Creative%20Site/Screenshot_2022-08-29_at_17.23.54_sb2eke.png)

The checkout success page details the order to the customer and offers a 'Back to shop" button.

## Login / Register / Logout / Forgot Email

![features-login](https://res.cloudinary.com/millermayhem/image/upload/v1661790587/Miller%20Creative%20Site/Screenshot_2022-08-29_at_17.26.58_rivsbd.png)
![features-register](https://res.cloudinary.com/millermayhem/image/upload/v1661790588/Miller%20Creative%20Site/Screenshot_2022-08-29_at_17.27.22_ohwut1.png)
![features-logout](https://res.cloudinary.com/millermayhem/image/upload/v1661790587/Miller%20Creative%20Site/Screenshot_2022-08-29_at_17.26.44_nfa94o.png)
![features-forgot-password](https://res.cloudinary.com/millermayhem/image/upload/v1661790587/Miller%20Creative%20Site/Screenshot_2022-08-29_at_17.27.11_vdgaxm.png)

The authentication pages are part of Allauth. They allow users to login, register for an account, logout and change their password. 
They have been styled to match the site.

When registering the user will be asked to provide an email address, username and password. These will then be used for the log in process.

## My Profile

![features-myprofile](https://res.cloudinary.com/millermayhem/image/upload/v1661792511/Miller%20Creative%20Site/Screenshot_2022-08-29_at_18.00.42_q0nfii.png)

My profile page allows you to store and update your personal information. 
Another key feature of this page is the order history. This shows the user all of their previous orders. These can be clciked on to display the full informtion.

## Product Management

![features-product-management](https://res.cloudinary.com/millermayhem/image/upload/v1661792892/Miller%20Creative%20Site/Screenshot_2022-08-29_at_18.07.09_dg1x2v.png)
![features-product-management](https://res.cloudinary.com/millermayhem/image/upload/v1661792892/Miller%20Creative%20Site/Screenshot_2022-08-29_at_18.07.20_w4phqa.png)

As an admin user the ability to add, edit and remove products is available. 
Products can be added via the product management page. When logged in as a user, edit and delete buttons appear at each product.

![features-edit-delete](https://res.cloudinary.com/millermayhem/image/upload/v1661795361/Miller%20Creative%20Site/Screenshot_2022-08-29_at_18.11.16_cgjndp.png)
![features-edit-delete](https://res.cloudinary.com/millermayhem/image/upload/v1661795361/Miller%20Creative%20Site/Screenshot_2022-08-29_at_18.11.27_yao294.png)

## Messages

The site is set up to display messages when certain actions take place. An example of this is when an item is added to the trolley or when the user signs in. 

When an item is added to the trolley a message appears which gives the user the option to go to the checkout.

![features-messages](https://res.cloudinary.com/millermayhem/image/upload/v1661795941/Miller%20Creative%20Site/Screenshot_2022-08-29_at_18.57.18_aa0ecp.png)
![features-messages](https://res.cloudinary.com/millermayhem/image/upload/v1661795941/Miller%20Creative%20Site/Screenshot_2022-08-29_at_18.56.34_eq4m6z.png)
![features-messages](https://res.cloudinary.com/millermayhem/image/upload/v1661795941/Miller%20Creative%20Site/Screenshot_2022-08-29_at_18.56.09_buzlnn.png)
