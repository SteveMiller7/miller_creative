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
  - Navigation Bar with Off Canvas
  - Header
  - Subscribe
  - About
  - Featured Companies
  - Footer and links
  - Featured Work Page
  - Shop
  - Product Detail
  - Shopping Trolley
  - Checkout
  - Checkout Success
  - Login / Register / Lougout / Forgot Email
  - My Profile
  - Product Management
  - Messages
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - Performance testing 
  - Functionality Testing
  - Compatibility Testing
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


[Back to Table of Contents](#table-of-contents)

***

# Technologies Used

## HTML 5
- Structure Language

## CSS
- Styling Language

## Bootstraps
- Frontend frameworks

## Django
- Database framework

## Javascript
- Interactive elements

## Google Fonts
- As a font resource.

## Font Awesome
- Social media icons

## Github
- As a software hosting platform.

## Gitpod
- For code development.

## Heroku
- App Hosting platform

## Postgres
- Database

## Adobe Illustrator
- Logo creation
- PNG and JPEG production
- Wireframes

## Photoshop
- Screens mockup image

## Cloudinary
- Image hosting

## Stripe
- Online payments

## Mailchimp
-Subscriptions and promotions

[Back to Table of Contents](#table-of-contents)

***

## Performance Testing

### Index

![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661806209/Miller%20Creative%20Site/Screenshot_2022-08-29_at_19.50.21_xtmvfb.png)
![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661806209/Miller%20Creative%20Site/Screenshot_2022-08-29_at_19.56.16_rzsl2i.png)
![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661806209/Miller%20Creative%20Site/Screenshot_2022-08-29_at_21.05.51_ioba65.png)
![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661806209/Miller%20Creative%20Site/Screenshot_2022-08-29_at_20.44.59_blsnii.png)
![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661806209/Miller%20Creative%20Site/Screenshot_2022-08-29_at_21.03.28_oqkdn6.png)

Website functionality testing was done using Google Chrome Developer Tools Lighthouse.
Improvements were made after testing the site build upon original completion.
Issues first raised included missing alt attributes on images, missing titles, png image sizes too big so multiple files were changed to webp files.
Originally the test result for performance was 95 but dropped to 93 after all of the improvements I made. 
Signifiacnt improvements were made to Accessability which went from 85 to 100.
SEO also went to 100 from 90.
Best practices rised from 83 to 92.


![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661807767/Miller%20Creative%20Site/Screenshot_2022-08-29_at_22.15.34_jjfxez.png)

### Featured Work

![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661810380/Miller%20Creative%20Site/Screenshot_2022-08-29_at_22.22.16_qjqhd3.png)
![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661810433/Miller%20Creative%20Site/Screenshot_2022-08-29_at_22.22.33_nkole0.png)
![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661810434/Miller%20Creative%20Site/Screenshot_2022-08-29_at_22.25.12_jo1xwn.png)
![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661810434/Miller%20Creative%20Site/Screenshot_2022-08-29_at_22.24.56_chvrw4.png)

The main issues found on the featured work page was the image sizes being uploaded to the featured companies cards. I reformatted them all and 
added them.
I also added titles where needed.
These actions helped bring up the scores.

![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661810434/Miller%20Creative%20Site/Screenshot_2022-08-29_at_22.58.42_tkyrna.png)

### Product Detail

![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661811781/Miller%20Creative%20Site/Screenshot_2022-08-29_at_23.15.23_zn1njr.png)

The same changes were made ti image alts, titls and sizes.

![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661811807/Miller%20Creative%20Site/Screenshot_2022-08-29_at_23.23.10_m50ukf.png)

### Contact Page

![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661812125/Miller%20Creative%20Site/Screenshot_2022-08-29_at_23.28.30_vpbkyi.png)

Again the same changes were made to image size and title

![Lighthouse performance result](https://res.cloudinary.com/millermayhem/image/upload/v1661812239/Miller%20Creative%20Site/Screenshot_2022-08-29_at_23.30.26_v77xsg.png)

## Manual Finctionality Testing

Throughout the build manual function tests were carried out constantly to assess whether buttons, links, admin updates etc all worked. Trial and error got me to the results I was after.

Forms were all tested repeatedly and checked against the admin databse records. 

All shop functions and enquiry forms work well with emails being received where required. 

Stripe payments are all being looged in payments section of their website.

I had some issues when testing.
The site has an off canvas, spinning logo, increment and decrement buttons and messages. I was finding a lot of issues with the version of jQuery I had 
in the scripts. Not all of these would work at the same time. I finally managed to sort it but it took a lot of trial and error. 

When I deployed the site to Heroku the order of my products got jumbled within their respective pages. Originally I have them in order of print quantity
but that all changed in Heroku.

As the developer I thoroughly checked the infrastrcutre and every line of code during the build, when formatting code and when running through the 
code validator. Changes were made where required, when required. All Inputs, links, updates, deletes, edits, navigations, external links, login, 
logout, registers and backend additions were checked against output results and everything worked nicely by the end of the build. All bugs were 
removed and all features work well. Information is passed to the database and everything syncs up and corresponds with each other. 

Admin users can easliy create, edit and delete categories and products in the backend as well as add and remove featured work cards.

As well as testing the deployed application myself on iMac, Macbook, iPad and iPhone, I invited 3 other people to perform functionality testing through whatever whatever digital media they had access to. 
Feedback on UX design, functionality and aesthetics was very positive from the other people testing the site. 

I tested the functionality myself using both knowledge of the code and via the deployed site. I found no functional issues myself but did have some future improvments in mind as detailed a little below.

Future improvements would also include:

- Addition of web design section and sales
- log in with social media
- Addition sales which would be items ready to buy and send. These would include posters, digital artwork, clothing

The main thing I would change about the site is the shop section. When building it i wanted to have it al on a single page
where the user could select various things from drop downs. These would include, paper size, paper thickness, laminate finish, print quantity and laminate finish.
The total would then adjust to suit. I couldnt find a way to do this so I made a decision to do it the wy it is on this site.

## Compaitibility testing

The site was tested on various devices including:
- iPhone
- Macbook Pro
- iMac
- iPad
- I also tested responsiveness on Google Chrome Dev Tools. 

## Code Validation

sites used
- validator.w3.org
- jigsaw.w3.org

### html

Html code was checked using validator.w3.org

There were some issues on index.html as shown below 

![Code validation](https://res.cloudinary.com/millermayhem/image/upload/v1661840097/Miller%20Creative%20Site/Screenshot_2022-08-30_at_07.12.47_cffxid.png)
This issue was removed.

The errors and warnings below are all part of the mail chimp form and scripts within the post load js. I dont want to mess with them in case i cause issues with the funtionality. 
![Code validation](https://res.cloudinary.com/millermayhem/image/upload/v1661843664/Miller%20Creative%20Site/Screenshot_2022-08-30_at_08.13.59_gvrej7.png)

Im finding the same issues being raised with my pages where I've set the background to stay still while my content scrolls within it. Thisn is shown below. The elements are close but its outwith the blocked content.
![Code validation](https://res.cloudinary.com/millermayhem/image/upload/v1661846049/Miller%20Creative%20Site/Screenshot_2022-08-30_at_08.50.46_bfunyp.png)
![Code validation](https://res.cloudinary.com/millermayhem/image/upload/v1661846049/Miller%20Creative%20Site/Screenshot_2022-08-30_at_08.52.40_cuvxhs.png)


### css

css errors flagged are shown below but I dont knoe what they are. Ive searched the site fr animation but i cant see it.
![Code validation](https://res.cloudinary.com/millermayhem/image/upload/v1661844934/Miller%20Creative%20Site/Screenshot_2022-08-30_at_08.33.58_phveel.png)
![Code validation](https://res.cloudinary.com/millermayhem/image/upload/v1661844934/Miller%20Creative%20Site/Screenshot_2022-08-30_at_08.34.12_vvd309.png)

All of the other css is fine when run through jigsaw.w3.org.

[Back to Table of Contents](#table-of-contents)

***

# Deployment

The project is deployed via Heroku. 

I used Gitpod as a development environment where I commited all changes to git version control system. I used push command in Gitpod to save changes into GitHub.

To deploy the project I had to connect my Github respitory to Heroku through the Heroku 'Deploy' page.
All of the necessary config vars were created to allow the application to work.

The site is published at https://miller-creative.herokuapp.com/ 

To run localy:

- Log in to GitHub and click on repository to download (miller_creative)
- select `Code` and click Download the ZIP file.
- after download you can extract the file and use it in your local environment

Alternatively you can Clone or Fork this repository (miller_creative) into your github account.

***

# Credits

Initital creation of the project was done using Code Institute student template: 
- gitpod full template

Ideas and coding guides:
- www.w3schools.com
- Diploma in Software Development (E-commerce Applications) from Code Institute.
- 'Boutique Ado' Walkthrough via Code Institute
- 'Love Running' Walkthrough via Code Institute
- 'Bootstrap Resume' via Code Institute
- Bad_Dog_Portfolio_1 done through Code Institute
- P4-Hannahs_Nails portfolio project dont through Code Institute.
- stackoverflow.com
- geeksforgeeks.org
- pypi.org
- Slack Code Institute community
- Ordinarycoders.com
- Freepik.com
- stock.adobe.com
- tgocreative.co.uk
- w3schools.com
- codepen.io
- mdboostrap.com
- css-tricks.com
- dev.to

## Content

Information for this website was written by myself with reference to
- en.wikipedia.org
- tgocreative.co.uk

## Images, Styling, Frameworks

Licensed and royalty free images were taken from:
- fontawesome.com
- fonts.google.com
- bootstrap.com
- cloudinary.com
- Adobe stock
- Adobe Illustrator
- Adobe Photoshop
- django
- django-crispyforms
- django-allauth
- Stripe
- mailchimp

[Back to Table of Contents](#table-of-contents)
