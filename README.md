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
