# Fucina Martelli



![logo](https://user-images.githubusercontent.com/80674568/162563738-2ca6e658-b6f9-4120-955d-e92c15347d40.PNG)

### [View live project here](https://fucina-martelli.herokuapp.com/)


## Overview
Fucina Martelli is an imaginary site of a group of blacksmiths specializing in the manufacture and sale of weapons and equipment for the sport of buhurt.

The website is designed to be responsive and accessible on all devices.

---

## Table of Contents

1. [UX](#ux)
- [User Stories](#user-stories)
- [User Centered Design](#user-centered-design)
  - [Strategy](#strategy)
    - [User needs](#user-needs)
  - [Scope](#scope)  
  - [Skeleton and Wireframes](#Skeleton-and-Wireframes)

2. [DESIGN](#design)
- [Color scheme](#color-scheme)
- [Typography](#typography)
- [Imagery](#imagery)
- [Logo](#logo)

3. [DATABASE MODEL](#database-model)
- [Database model features](#database-model-features)

4. [FEATURES](#features)
- [Admin Feature](#Admin-Feature)
- [Design Features](#design-features)
- [Features left to implement](#features-left-to-implement)

5. [TECHNOLOGIES USED](#technologies-used)
- [Syntax](#syntax)
- [Frameworks, Libraries & Programs](#frameworks-libraries-&-programs)

6. [TESTING](#testing)
- [Testing document](TESTING.md)

7. [API](#api)
- [Stripe](#stripe)
- [Gmail for Django](#Gmail-for-Django)

8. [DEPLOYMENT](#deployment)
- [Heroku and Postgres DB](#Heroku-and-Postgres-DB)
- [Amazon Web Services](#amazon-web-services)
- [Github](#github)
  - [Forking the repository](#forking-the-repository)
  - [Creating a Clone](#creating-a-clone)
  
9. [MARKETING AND SEO](#marketing-and-seo)


10. [CREDITS](#credits)





## UX

### **User stories**

 #### As an anonymous user/ first time visitor I want to:
  1. Be able to easily navigate throughout the site to visualise content and contacts.
  2. Check out a specific product, visualise the relative details and price.
  3. Buy the product I want.
  4. choose the material of the product (steel and titanium are allowed in this sport)
  5. In order to be updated about the news of the blacksmiths group also through social media.

 #### As a registered user/frequent visitor I want to (in addition to the anonymous user functionalities):
  5. Be able to log in.
  6. Be able to log out.
  7. Be able to delete my account.  
  8. Be able to update personal details.
  9. Be able view my order history.

 #### As the admin I want to:
  10. Be able to add products to the site.
  11. Be able to update product details (for example put a product in the special offers).
  12. Be able to delete products from the site. 
  13. Have unique access to all features.

  #### As the website owner I want to:
  14. Make the website as accessible and responsive as possible.  
  15. Use reviews to increase customer satisfaction.
  16. Find the best way to allow communication bewteen customers and the organization.
  17. Inform users of any changes to the regulations of this sport
  
---



### **Strategy**

- #### User needs

The main goal of this website is to make order management efficient and to transmit passion in this spor in such a way as to create customer loyalty in order to increase sales too.
Registered users will be able to see their previous orders and their current ones. In addition to that, for register user there is the possibility to review the products.



The steps a new user would ideally take when landing onto the website are the following:
  - Explore the websites landing page, where the information will explain the user the reason to be of the site.
  - see if there is any news on sport
  - buy a product 
  - Log in/out.
  - Check out the links in the footer.

The website needs to enable the **User** to:
  - Easy access the features of the website.
  - Register and log in if further interested.
  - Get in touch with the website owner and/or admin.
  - Give rewiews.

The website needs to enable the **Website owner and/or admin** to:
  - Develop an online presence .
  - Provide an easily navigable website for users.
  - Improve the website thanks to the contacts.
  - Add or delete products from catalougue

---

### **Scope**

- **Features within the design plan :**
  - Minimal but functional and appealing homepage .
  - Navigation links clearly visible on the top of the website.
  - Responsive navigation bar.
  - Only allow registered users to create and manage their own accounts.
  - Only allow registered users to check out their previous orders.
  - Only allow registered users to delete their account.
  - All the user can register in the newsletter or not


---

### Skeleton and Wireframes

#### on mobile:
[fucinaMartelliphone.pdf](https://github.com/latorreandrea/fucina_martelli/files/8456560/fucinaMartelliphone.pdf)

#### on pc/tablet:
[PcFucina.pdf](https://github.com/latorreandrea/fucina_martelli/files/8456562/PcFucina.pdf)

## DESIGN

The design of the website was created to be as simple but at the same time recall the Middle Ages, not to distract the user with too many color schemes and trying to bring the focus onto the products.

### **Color scheme**

The colors used are variations of dark green. this color was chosen because it is the historical color of the medieval militias of northern Italy, the area of origin of the owners of the site
 

### **Typography**

The main font-family for this site is 'Rubik' to allow easy reading of the text to users  only for the logo the chosen font was the 'UnifrakturCook'

### **Imagery**

- Currently using wikipedia images and descriptions with creative commons license
-
---

### **Logo**

- the font used for the logo is Unifraktur (used for its mefievale lines) 
- the images of people in armor, were kindly offered by the Bellatores sports club to which I belong https://www.facebook.com/TeamBellatores/
---

## Database Model

### Database model features

- The website is a data-centric one with html, javascript, css used with the bootstrap (version 5) framework as a frontend.
- The backend consists of Python built with the Django framework with a database of a Postgres for the deployed Heroku version (production).
- [Postgres](https://www.postgresql.org/) is a powerful, open source object-relational database system.
- [SQLLite](https://www.sqlite.org/index.html) database was used for local development. 

- This model contains all fields stored in the database collections with their data type and mimics the structure of what is actually stored in the Postgres database.

[DB Data Structure](https://github.com/latorreandrea/fucina_martelli/files/8456593/fucina.martelli.pdf)
## Features

The website has the following features based on:

1. A user not logged into the site
2. A regular user logged into the site
3. An admin user
The navigation buttons update depending on whether a user is logged in or not, and whether that user is the admin:

 Nav Link              |Not logged in  |Logged in as regular user|Logged in as admin
:-------------         |:------------- |:----------------|:------------- |
Home     |&#9989;        |&#9989;          |&#9989; |
Products           |&#9989;        |&#9989;          |&#9989; |
Product Detail           |&#9989;        |&#9989;          |&#9989; |
Rewiev Product          |&#10060;       |&#9989;          |&#9989; |
Product Management(Add Product)     |&#10060;       |&#10060;         |&#9989; |
Product Management(Edit Product)     |&#10060;       |&#10060;         |&#9989; |
Product Management(Delete Product)     |&#10060;       |&#10060;         |&#9989; |
My Profile             |&#10060;       |&#9989;          |&#9989; |
Order History         |&#10060;       |&#9989;          |&#9989; |
Log out               |&#10060;       |&#9989;          |&#9989; |
Register               |&#9989;        |&#10060;         |&#10060; |
Log in               |&#9989;        |&#10060;         |&#10060; |
Cart |&#9989;        |&#9989;          |&#9989; |
Checkout |&#9989;        |&#9989;          |&#9989; |
Checkout success |&#9989;        |&#9989;          |&#9989; |
Register to newsletter |&#9989;        |&#9989;          |&#9989; |

<br>


<br>

### Design Features
The distinctive design of this site is the medieval background and the use of glassmorphism

### Header
![pc header](https://user-images.githubusercontent.com/80674568/162566658-5bef60ac-3b71-4330-a774-e896055456bf.PNG)

#### Navigation bar on smaller devices:
![navbarmobile1](https://user-images.githubusercontent.com/80674568/162566662-651414fe-95f6-402c-b5f7-17f856e85c03.PNG)
![navmobile](https://user-images.githubusercontent.com/80674568/162566664-788d8a3e-ee28-419a-9eeb-461c23c0454d.PNG)

in addition to directing us to the various product categories from the nav bar, we can intuitively access our profile (if the user is logged in) and our cart
### Search Button
![searcbar](https://user-images.githubusercontent.com/80674568/162566761-e19a3758-abf0-4bf7-b595-c27ba4b91285.PNG)
this search bar allows you to filter products by name and category

#### Footer
![footer](https://user-images.githubusercontent.com/80674568/162567260-ea99bdd6-4a46-4aa0-9796-c1da605bf0cb.PNG)
the footer is divided into 3 parts, one that summarizes the history of Fucina Martelli,
the second contains all the social channels (at the moment only the facebook one is working), and the links to subscribe to the newsletter
the third contains the service policies

## Main Page:

#### Main page carousel:
![carousel](https://user-images.githubusercontent.com/80674568/162566889-0d60f9da-17a1-4417-84f1-fb3dc9e033e2.PNG)
a carousel of three images that takes us to the key points of the site: products, main info on buhurt and contacts and policies

#### main page content:
![maincontent](https://user-images.githubusercontent.com/80674568/162567191-c878cb25-44b2-4066-9044-7be24801c364.PNG)
brief introduction on the sport and services of the hammer workshop to invite users to visit the shop
the accompanying videos taken from the sport's official youtube channels provide a further explanation

## My Account page (only for admins and registered users)
![Myaccountpage](https://user-images.githubusercontent.com/80674568/162567484-20a29a3e-f198-4cdc-9127-ec1a59874832.PNG)
This page is accessed after logging in to the site and proposes actions that are limited based on permissions (basic users will not be able to add products)
this page allows you to view the order history of the registered user.

#### Admin Functionality in the My account page
- Other than through the default Django admin interface, products can be added/created, edited and removed (CRUD) directly from the website when entering with admin credentials. This feature facilitates the management of products thanks to a more friendly and direct user interface. This feature makes things easier for the website owner in case he/she needs to make changes on the products without having to access the Django admin interface.

- Add new product
  -the admin by accessing his user section has the option to create a product

![add product 1/2](https://user-images.githubusercontent.com/80674568/162566241-21b3790c-37f8-4155-bd56-a7eb129c9e8b.jpg)
![add product 2/2](https://user-images.githubusercontent.com/80674568/162566243-017196ea-be8d-445c-b0bb-2d20e8bb93d4.PNG)


#### Admin Functionality in the product description page
- Delete Product
  - admin from the product description tab can delete it
![delete1/2](https://user-images.githubusercontent.com/80674568/162566429-51378ca9-e2bb-42c0-9be6-c1b2dda1a9b5.PNG)
![delete2/2](https://user-images.githubusercontent.com/80674568/162566439-390528f7-36fc-4e97-b555-a8f2f68bda72.PNG)

- Update/Edit product Details
  - the admin from the product description tab can update it
![update1/2](https://user-images.githubusercontent.com/80674568/162566429-51378ca9-e2bb-42c0-9be6-c1b2dda1a9b5.PNG)
![update2/2](https://user-images.githubusercontent.com/80674568/162566514-8e8138bb-d4f1-45b5-8a82-84b3a66cca50.PNG)




### Features left to implement

#### complete the functionality of the newsletter:
- at the moment it is possible to register emails and delete them but not actually send functional newsletters

#### saving shipping information:
- causing problems, this functionality has been kept on the sidelines for the time being

#### discount function:
- the functionality is set for the CRUD created for the admin, but not yet managed by any views

## TECHNOLOGIES USED

### **Syntax**

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Markdown](https://www.markdownguide.org/basic-syntax/)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Frameworks, Libraries & Programs
- [Font Awesome](https://fontawesome.com/)
  - Used to include icons.

- [Google Fonts](https://fonts.google.com/)
  - Used to import the three fonts used throughout the site xxxxxxxx.

- [GitHub](https://github.com/)
  - Used to host the entire repository for the project.

- [GitPod](https://www.gitpod.io/)
  - The code editor used to build the entire project.

- [W3C Validator HTML](https://validator.w3.org/)
  - Validator for HTML.

- [W3C Validator CSS](https://jigsaw.w3.org/css-validator/)
  - Validator for CSS.

- [JSHint](https://jshint.com/)
  - This is a tool used to detect errors or potential problems within Javascript code, used to test and validate all Javascript written for this project.

- [Django](https://www.djangoproject.com/)
  - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

- [Heroku](https://id.heroku.com/login)
  - Heroku is a cloud platform as a service (PaaS) supporting several programming languages.
  - The Heroku network runs the customer's apps in virtual containers which execute on a reliable runtime environment.

- [W3Schools](https://www.w3schools.com/)
  - To check demos and explanations.

- [Stack overflow](https://stackoverflow.com/)
  - To find answers to most common problems.

- [Postgres Db](https://www.postgresql.org/)
  - PostgreSQL is a powerful, open source object-relational database system.

- [Vanilla-titl.js](https://micku7zu.github.io/vanilla-tilt.js/) 
  - A smooth 3D tilt javascript library used for moving the descriptions cards.

- [Haikei](https://app.haikei.app/) 
  - Haikei is a web app to generate unique SVG shapes, backgrounds, and patterns – ready to use with your design tools and workflow.


## Testing

### test for unregistered users:

![invitoagli utenti non registrati](https://user-images.githubusercontent.com/80674568/162567881-4128082d-f8fc-48f7-85a7-89cc7317d301.PNG)
as an unregistered user entering the site I have the navigation bar that asks me to register or log in,

![newsletter](https://user-images.githubusercontent.com/80674568/162568110-19ddad12-b3e4-40e4-bb3d-abdfb18126a2.PNG)
i can sign up for newsletter clikking in carousel button newsletter here or in the footer link

![productpage](https://user-images.githubusercontent.com/80674568/162568176-fbbd99c7-d859-4498-87b3-e47a16baf0ee.PNG)
I can access the products via search bar and navbar


![product description](https://user-images.githubusercontent.com/80674568/162568311-e5932e3d-9775-497d-ada3-d1273ce18f86.PNG)
I can see the products and their descriptions, add them to the cart, choose with which material to add it. an invitation under the product image asks us to register or log in to be able to rate this product

![add to cart](https://user-images.githubusercontent.com/80674568/162568350-82e2d3a6-9d4d-4f99-9eca-dca4166f8b4d.PNG)
adding the product to the cart to buy it, a toast appears to inform me of the action taken, and the option go to cart appears

![cart](https://user-images.githubusercontent.com/80674568/162568416-f58fb68f-07d5-41dc-957b-500ab9dd36c3.PNG)
once the products have been added by selecting the relevant material, the cart screen informs me that there is a surplus of € 200 for titanium products, if I have to adjust the quantity of the products then I can do it from the cart. The total item informs me of the expense

![test](https://user-images.githubusercontent.com/80674568/162571374-9e50007e-67c6-45de-a04d-67cced918e50.PNG)
![test2](https://user-images.githubusercontent.com/80674568/162571491-c0e5dbba-67ab-4ca3-a9b8-e24187f06169.PNG)
the payment made on the site is actually recorded and goes by stripe:
![stripe confirms](https://user-images.githubusercontent.com/80674568/162581743-a33444f2-bb6f-4e97-9719-5e2afd9ce997.PNG)

### test for registered users:

![login](https://user-images.githubusercontent.com/80674568/162582349-5a4615bb-947d-4fcc-83ae-7e3fe5ac142e.PNG)
![login2](https://user-images.githubusercontent.com/80674568/162582353-5245c808-c7cb-47d5-9e5f-bf14e93f6c23.PNG)
the registered user can log in and access a personal menu
![myaccount](https://user-images.githubusercontent.com/80674568/162582637-9d382d77-d83f-4755-8824-8c2338362a5b.PNG)

![order history](https://user-images.githubusercontent.com/80674568/162582681-0335283d-2312-4410-9bb0-4c46220778af.PNG)
the registered user can access his order history

![rategear](https://user-images.githubusercontent.com/80674568/162582442-46fcc4ea-af60-4416-b879-17e939061732.PNG)
the registered user can review the products
![review results](https://user-images.githubusercontent.com/80674568/162582591-d8bb07fe-2fad-4e1a-97b7-2026678fb573.PNG)
the latest reviews will be displayed and the average rating of the product will appear under the product

### test for Admin:

![addtest](https://user-images.githubusercontent.com/80674568/162582811-8209c8b7-68d4-4db4-ad7c-82e3b6d0b594.PNG)
![addtest2](https://user-images.githubusercontent.com/80674568/162582816-2cca3c1e-d592-4d4b-8e02-f3240a8e562b.PNG)


admins can add products from the My account actions

![updatetest](https://user-images.githubusercontent.com/80674568/162583032-800feedb-992e-4b76-99f0-e5d04ddd5045.PNG)
![updatetest2](https://user-images.githubusercontent.com/80674568/162583034-13bbde94-d0f7-4b77-987c-ea738d2c4302.PNG)


the admin can modify the product from the product description sheet

![updatetest3](https://user-images.githubusercontent.com/80674568/162583040-b7684ad0-d429-46c4-be85-c8a1b4988bb2.PNG)
![updatetest4](https://user-images.githubusercontent.com/80674568/162583043-3c8427a1-6332-4ffc-aecf-bcc4d1fb1cd8.PNG)
![updatetestresult](https://user-images.githubusercontent.com/80674568/162583045-59cc7d61-6fe0-44da-a611-d0c8a72e9454.PNG)
this is the results

![deletetest](https://user-images.githubusercontent.com/80674568/162583275-1b6ef809-6183-49ca-8695-277e388cdd01.PNG)
![deletetest2](https://user-images.githubusercontent.com/80674568/162583281-1e67f8f0-ae97-4b0f-987e-3ff5da83ab1f.PNG)
the admin from the product description has the possibility to delete it
![deletetest3](https://user-images.githubusercontent.com/80674568/162583332-5ca30bc1-31ef-4c87-b25b-b0cb06c5f840.PNG)
the product will be deleted from the product list and a message confirms that the product has been deleted

## API

### Stripe
To set up Stripe, proceed as follows:

1. Register for an account at stripe.com
2. Click on the Developers section of your account once logged in.
3. Under Developers, click on the API keys section.
4. Note the values for the publishable and secret keys
5. In your local environment(env.py) and heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values.
<br><code>os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')</code>
<br><code>os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')</code>

6. Back in the Developers section of your stripe account click on Webhooks
7. Create a webhook with the url of your website <url>/checkout/wh/
8. Select the payment_intent.payment_failed and payment_intent.succeeded as events to send.
9. Note the key created for this webhook
10. In your local environment(env.py) and heroku, create environment variable STRIPE_WH_SECRET with the secret values
<code>os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')</code>
11. Feel free to test out the webhook and note the success/fail attempts for troubleshooting.
![Webhook](readme_files/stripe/webhook_successful.png)


<br>

### Gmail for Django

To set up the project to send emails and to use a Google account as an SMTP server, the following steps are required:
1. Create an email account at google.com, login, navigate to Settings in your gmail account and then click on Other Google Account Settings.
2. Turn on 2-step verification and follow the steps to enable.
3. Click on app passwords, select Other as the app and give the password a name, for example Django.
4. Click create and a 16 digit password will be generated, note the password down.
5. In the env.py file, create an environment variable called EMAIL_HOST_PASS with the 16 digit password.
6. In the env.py file, create an environment variable called EMAIL_HOST_USER with the email address of the gmail account.
7. Set and confirm the following values in the settings.py file to successfully send emails.
<br><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code>
<br><code>EMAIL_USE_TLS = True</code>
<br><code>EMAIL_PORT = 587</code>
<br><code>EMAIL_HOST = 'smtp.gmail.com'</code>
<br><code>EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')</code>
<br><code>EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')</code>
<br><code>DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')</code>

8. You will also need to set the variables EMAIL_HOST_PASS and EMAIL_HOST_USER in your production instance, for example Heroku.

---

## Deployment

### Heroku and Postgres DB
To deploy this application to Heroku, run the following steps:

1. Create an account at heroku.com
2. Create an app, give it a name and select a region.
3. Under resources search for postgres, and add a Postgres database to the app.    
4. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
5. Install the plugins dj-database-url and psycopg2-binary.
6. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
7. Create a Procfile with the text
8. In the settings.py ensure the connection is to the Heroku postgres database.
9. Ensure debug is set to false in the settings.py file.
10. Add localhost and nameapp.herokuapp.com to the ALLOWED_HOSTS variable in settings.py.
11. Run "python3 manage.py showmigrations" to check the status of the migrations.
12. Run "python3 manage.py migrate" to migrate the database.
13. Run "python3 manage.py createsuperuser" to create a super/admin user.
14. Install gunicorn and add it to the requirements.tx file using the command pip3 freeze > requirements.txt
15. From the CLI login to Heroku using the command heroku git:remote 
16. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1
17. Push the code to Heroku using the command git push heroku master.
18. Ensure the following environment variables are set in Heroku.
19. Connect the app to GitHub, and enable automatic deploys from main    
20. Click deploy to deploy your application to Heroku for the first time
21. Click on the link provided to access the application
22. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue

### Amazon Web Services
To set up AWS S3 Bucket, proceed as follows:

1. Create an account at aws.amazon.com
2. Open the S3 application and create an S3 bucket.
3. Uncheck the "Block All Public access setting".
4. In the Properties section, navigate to the "Static Website Hosting" section and click edit.
5. Enable the setting, and set the index.html and the error.html values.
![AWS Static](readme_files/aws/aws_img1.png)
6. In the Permissions section, click edit on the CORS configuration and set the below configuration.
![AWS CORS](readme_files/aws/aws_img3_CORS.png)
7. In the permissions section, click edit on the bucket policy and generate and set the below configuration(or similar to your settings).
![AWS Bucket Policy](readme_files/aws/aws_img2_bucket_policy.png)
8. In the permissions section, click edit on the Access control list(ACL).
9. Set Read access for the Bucket ACL for Everyone (Public Access).
10. The bucket is created, the next step is to open the IAM application to set up access.
11. Create a new user group named "add_group_name".
12. Add the "AmazonS3FullAccess" policy permission for the user group.
![AWS Bucket Policy](readme_files/aws/aws_img4_amz_fullaccess.png)
13. Go to "Policies" and click "Create New Policy"
14. Click "Import Managed Policy" and select "AmazonS3FullAccess" > Click 'Import'.
15. In the JSON editor, update the policy "Resource"
16. Give the policy a name and click "Create Policy".
17. Add the newly created policy to the user group.
18. Go to Users and create a new user
19. Add the user to the user group "add_group_name"
20. Select "Programmatic access" for the access type
21. Note the AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID variables, they are used in other parts of this README for local deployment and Heroku setup.
22. The user is now created with the correct user group and policy.
23. Note the AWS code in settings.py. Note an environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage.
![AWS Settings](readme_files/aws/aws_img5_settings.png)
24. These settings set up a cache policy, set the bucket name, and the environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY that you set in your aws account.
25. The configuration also requires the media/static folders that must be setup in the AWS S3 bucket to store the media and static files.
26. AWS S3 Stored images.
![AWS Bucket Policy](readme_files/aws/aws_images.png)
27. AWS S3 Stored static files.
![AWS Bucket Policy](readme_files/aws/aws_objects.png)

## MARKETING AND SEO
to improve the seo and therefore indirectly also the marketing potential of the site itself, I followed a series of steps:
  1. Brainstorm  general topics:
  ![brainstorming](https://user-images.githubusercontent.com/80674568/162583586-0d848392-6093-4f09-8e5f-332873dda3fb.jpg)
  2. Brain dump possible keywords for each of the general topics so the list is:
  what is buhurt?, what does it mean?, where i can find a team?, there are rules?, is that a discipline?, where i can buy armor?,  why the cost are never clear?
  can buy an used armour?, what are the injuries?, buhurt in eu, buhurt in Italy, tournaments, buhurt weapon, buhurt rules, buhurt team, buhurt cost,  buhurt training
  buhurt ranking team, buhurt official channel, maximum wheight of armour, maximum wheight of weapons, eu buhurt turnament, official tournament,  unofficial tournament
  time period allowed?, historicity in the armour?, how big are the match?, there is a refree?, what is the scope of the combat?
  3. Research brain dump of ideas in Google Search:
  ![Research ideas in Google Search2)](https://user-images.githubusercontent.com/80674568/162583722-4e341047-4739-44d6-85dc-f10888f7b99a.PNG)
  ![Research ideas in Google Search](https://user-images.githubusercontent.com/80674568/162583726-edab8a44-2da9-4b5f-af36-e39d5101555f.PNG)
  4. from this long list I have chosen 5 concepts among the most searched on google helping me with the next phase
  5. Assess choices for relevance and authoritativeness, and dig into the data available on keyword volume and competition using wordtracker.com
  ![Assess choices ](https://user-images.githubusercontent.com/80674568/162583843-5260842f-2c47-4812-8135-737b2f78b470.PNG)
  6. to choose which content to give to the homepage I asked myself a series of questions:
    - What do your users need?
    - What information and features can you provide to meet those needs?
    - How can you make the information easy to understand?
    - How can you demonstrate expertise, authoritativeness and trustworthiness in your content?
    - Would there be other pages within your own site you could link to from your chosen page?
    - Are there opportunities to link back to external websites that already rank highly on Google?
    - How can you help users discover other relevant parts of your web application?
actually part of the selected content has been changed in the course of work. The sport we are talking about was born in Russia and is managed with regard to official channels mainly by russian sports associations ... given the recent developments some sites are unusable and in protest some of these associations have preferred to suspend some of the most important events
  
however the world of sport is supportive and since the official youtube channels of this sport are still available, I preferred to use some of the videos that help newcomers to this sport to make some important decisions as well as to show the strengths of this sport
  
the homepage in fact presents the basic rules for understanding this sport and is supported by videos.
  
the site also proposes in the footer link to demonstrate to users the authority of the site and its reliability by dedicating the policy section mainly to this

  7. Create a sitemap.xml to ensure searc engines will crawl every essential page on the website using a sitemap generator

  8. Create a robots.txt file that tells search engines where they are not allowed (this ensure that search engines take the existence of this file in this site as a sign of quality so this improve SEO), even if in the sitemap created previously some of the links specified in robots are not mentioned, I specify in this file not to see the url deriving from the apps: accounts,add_product,edit_product,checkout

  9. at this point the main work to maximize SEO is done but by not certifying a DNS we cannot complete this implementation

  10. to accelerate the growth of the community that follows the Fucina Martelli brand I created a facebook group accessible from the social link in the footer of the site created specifically to reach new users also through social media (this was created for demonstration purposes only)
  ![fucina martelli fb page](https://user-images.githubusercontent.com/80674568/162585863-92ff3e12-c81e-47f0-bd3b-8432a188ba01.PNG)
  


## CREDITS

### Content
- Stack Overflow for guidance

- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page") for the Boostrap features.

- [Vanilla-titl.js](https://micku7zu.github.io/vanilla-tilt.js/) a smooth 3D tilt javascript library for moving the descriptions cards
  
- [Haikei](https://app.haikei.app/) to generate svg waves
  
- [Youtube](https://www.youtube.com/watch?v=TBVsILIt4HM&t=15s)mastercode online to show how to create a newsletter app

- [Facebook](https://www.facebook.com/FucinaMartelliBuhurtShop)facebook for create a shop in fb

- [Xml-sitemaps](https://www.xml-sitemaps.com/) to generate a sitemap.xml

### Media
- wikipedia
