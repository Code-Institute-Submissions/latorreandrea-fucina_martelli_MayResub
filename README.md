# Fucina Martelli



![Image of the mockup of the live website](#)

### [View live project here](#)


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

9. [CREDITS](#credits)

10. [REFERENCES](#references)

11. [ACKNOWLEDGEMENTS](#acknowledgements)

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
  8. Be able to add personal details to make my order faster.
  9. Be able to update personal details.
  10. Be able view my order history.

 #### As the admin I want to:
  11. Be able to add products to the site.
  12. Be able to update product details (for example put a product in the special offers).
  13. Be able to delete products from the site. 
  14. Have unique access to all features.

  #### As the website owner I want to:
  15. Make the website as accessible and responsive as possible.  
  16. Use reviews to increase customer satisfaction.
  17. Find the best way to allow communication bewteen customers and the organization.
  19. Inform users of any changes to the regulations of this sport
  20. Limit the request for products to a maximum of 10 per order as production takes from 2-3 months per type of product

---



### **Strategy**

- #### User needs

The main goal of this website is to make order management efficient and to transmit passion in this spor in such a way as to create customer loyalty in order to increase sales too.
Registered users will be able to see their previous orders and their current ones. In addition to that, as in most e-commerce shops, the convenience of having the personal data already saved is itself a good reason to register.



The steps a new user would ideally take when landing onto the website are the following:
  - Explore the websites landing page, where the information will explain the user the reason to be of the site.
  - see if there is any news on spor and if there are any special offers
  - buy a product 
  - Log in/out.
  - Check out the links in the footer.

The website needs to enable the **User** to:
  - Easy access the features of the website.
  - Register and log in if further interested.
  - Get in touch with the website owner and/or admin.
  - Give feedback.

The website needs to enable the **Website owner and/or admin** to:
  - Develop an online presence .
  - Provide an easily navigable website for users.
  - Improve the website thanks to the contacts.

---

### **Scope**

- **Features within the design plan :**
  - Minimal but functional and appealing homepage .
  - Navigation links clearly visible on the top of the website.
  - Responsive navigation bar.
  - Only allow registered users to create and manage their own accounts.
  - Only allow registered users to check out their previous orders.
  - Only allow registered users to delete their account.


---

### Skeleton and Wireframes

---

## DESIGN

The design of the website was created to be as simple and harmonious as possible, not to distract the user with too many color schemes and trying to bring the focus onto the products.

### **Color scheme**

The colors used are variations of dark green. this color was chosen because it is the historical color of the medieval militias of northern Italy, the area of ​​origin of the owners of the site
 


---

### **Typography**

(##)

---

### **Imagery**

- Currently using wikipedia images and descriptions with creative commons license

---

### **Logo**

- the font used for the logo is Unifraktur (used for its mefievale lines) 

---

## Database Model

### Database model features

- The website is a data-centric one with html, javascript, css used with the bootstrap (version 5) framework as a frontend.
- The backend consists of Python built with the Django framework with a database of a Postgres for the deployed Heroku version (production).
- [Postgres](https://www.postgresql.org/) is a powerful, open source object-relational database system.
- [SQLLite](https://www.sqlite.org/index.html) database was used for local development. 

- This model contains all fields stored in the database collections with their data type and mimics the structure of what is actually stored in the Postgres database.

![DB Data Structure](##)

---

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

<br>

### Admin Feature


#### Admin Functionality in the website
- Other than through the default Django admin interface, products can be added/created, edited and removed (CRUD) directly from the website when entering with admin credentials. This feature facilitates the management of products thanks to a more friendly and direct user interface. This feature makes things easier for the website owner in case he/she needs to make changes on the products without having to access the Django admin interface.

- Add new product
![Add new product](##)

- Delete Product
![Delete Product](##)

- Update/Edit product Details
![Update product details](##)

<br>

### Design Features
(##)

#### Header
#### Search Button

#### Navigation bar on smaller devices


#### Footer


### Features left to implement

#

---

## TECHNOLOGIES USED

### **Syntax**

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Markdown](https://www.markdownguide.org/basic-syntax/)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

---

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







---

## Testing
##

---

## API

### Stripe
To set up Stripe, proceed as follows:

1. Register for an account at stripe.com
2. Click on the Developers section of your account once logged in.
3. Under Developers, click on the API keys section.

![API keys](readme_files/api/api_key.png)

4. Note the values for the publishable and secret keys
5. In your local environment(env.py) and heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values.
<br><code>os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')</code>
<br><code>os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')</code>

6. Back in the Developers section of your stripe account click on Webhooks
7. Create a webhook with the url of your website <url>/checkout/wh/

![Webhook](readme_files/stripe/wb_created.png)

8. Select the payment_intent.payment_failed and payment_intent.succeeded as events to send.
9. Note the key created for this webhook
10. In your local environment(env.py) and heroku, create environment variable STRIPE_WH_SECRET with the secret values
<code>os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')</code>

11. Feel free to test out the webhook and note the success/fail attempts for troubleshooting.
![Webhook](readme_files/stripe/webhook_successful.png)
12. For futher information please check Stripe Testing in the [(TESTING.md) ](TESTING.md) file.

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
9. For futher information please check GMAIL testing in the [(TESTING.md) ](TESTING.md) file, bottom of the page (Other Features).

---

## Deployment

### Heroku and Postgres DB
To deploy this application to Heroku, run the following steps:

1. Create an account at heroku.com
2. Create an app, give it a name and select a region.
3. Under resources search for postgres, and add a Postgres database to the app.

![Heroku Postgres](readme_files/heroku/heroku_postgres.png)
    
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

![Heroku Env variables](readme_files/heroku/heroku_vars.png)

19. Connect the app to GitHub, and enable automatic deploys from main

![Heroku Postgres](readme_files/heroku/heroku_connected.png)
    
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

### Github

#### Forking the Repository
By forking the GitHub Repository a copy of the original repository is made on the GitHub account. To view and/or to make  changes without affecting the original repository: 
1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](##).
3. At the top of the repository, on the right side of the page, select "Fork".
4. You should now have a copy of the original repository in your GitHub account.

  ---

## CREDITS

### Content
- Stack Overflow for guidance

- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page") for the Boostrap features.

- [Vanilla-titl.js](https://micku7zu.github.io/vanilla-tilt.js/) a smooth 3D tilt javascript library for moving the descriptions cards

### Media
- wikipedia
