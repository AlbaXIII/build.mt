# BUILD.MT

IMAGE

## INTRODUCTION

build.mt is an online catalogue for the collection, sharing and review of character builds in role-playing games (RPGs). Many modern RPGs have an overabundance of character creation options, with many diverging paths, abilities, spells, gear – it’s enough to confuse many casual fans or first time players trying RPGs for the first time. built.mt is designed to take the stress out of choosing how to play a character. Prospective players can create an account, share their characters and how they play, strengths and weaknesses, and most of all – how fun they are to play! 

As well as a catalogue of build ideas, build.mt has an easy to read explanation page for each featured RPG so potential players (and account holders) can learn the basics of the game without being overwhelmed by information.

To summarise, build.mt is character inspiration made simple.

build.mt was designed initially with Larian’s 2023 release ‘Baldur’s Gate III’ in mind - but future realeases would include many of today's most popular and feature-rich RPGs, with From Software’s 2022 release ‘Elden Ring’ being the first to be added in a future realease.

This is my fourth Code Institute project and was developed using HTML, CSS, JavaScript, Python, Django, and PostgreSQL. 

View the website and join the community [here](https://build-mt-7c3508717c5e.herokuapp.com/).

IMAGE

## TABLE OF CONTENTS

1. [User Experience (UX)](#user-experience-ux)
    - [Strategy](#strategy)
    - [Site Goals](#site-goals)
    - [Ideal User](#ideal-user)
2. [User Stories & Methodology](#user-stories--methodology)

-----------------------------
 
## USER EXPERIENCE

### Strategy 

build.mt is designed to be an accessible and simple-to-use collection of character builds. Visitors will be able to peruse the builds at leisure, whilst authenticated site members will be able to log in and add their own, as well as like or share their favourites.

### Site Goals

* To provide **all users** with access to a build repository, with an organised list of build articles featuring structured and easy to understand information.
* To provide **all users** with the ability to sign up to the website and create an account.
* To provide **authenticated users** full CRUD functionality to upload and remove their own build to the database.
* To provide **authenticated users** the ability to like, share, comment and review other people’s build submissions.
* To provide site **administrators** the ability to approve comments, remove builds, and control user access.

### Ideal User

The ideal user of the site would be someone who is interested in starting to play role-playing games, and/or an experienced user who would be looking to experiment with new builds should they be wracked for ideas or wanting to try something new when playing their favourite games. Modern role-playing games are often incredibly complex and resources surrounding them can also be daunting to understand, so the ideal user would come to build.mt to have the process streamlined, and gain fun and interesting builds to try.

-----------------------------

## USER STORIES & METHODOLOGY

### Agile Working

Before starting the coding on build.mt, I created a custom user story template and linked it to the project Kanban board, to allow me to create an iterative and fluid development and deployment schedule. The use of the board allowed me to isolate applications and functions of the code and work on them in iterative sections, whilst keeping track of the status of each particular function of the code.

IMAGE

### Milestones/EPICs

7 Milestones were created at the beginning of the project, and from there the user stories were extracted. Each milestone was further categorised into feature sections, then further linked to the priority user stories subcategory on the project Kanban board.

1. Initialise setup
2. Build Catalogue 
3. User Registration
4. Build interaction
5. Build submission
6. Build collation
7. Site owner objectives

### User Stories

Each user story was linked to the project template with 3 completion benchmarks (as base, number of acceptance criteria extends depending on user story) as a criteria to for adequate completion of the story;

Using **project**;

As a **visitor/user/admin** I can **ability** in order to **result**

### Completion Benchmark

**CB1**

**CB2**

**CB3**

The list of user stories can bee viewed on the ‘completed’ tab of the project kanban board, but also viewable below;

- Initialise Django Setup
- Create Database
- Deploy to Heroku
- Create database admin superuser
- Create base html & styles
- Add static files and directories
- Create BG3 build list
- Create BG3 detailed build page
- Search via keyword
- Create & register user accounts
- Create a build post
- Moderate posts
- Leave comments on builds
- Moderate comments
- Add build to favourites
- View account & favourite builds
- Create ER detailed build page
- Create home app directory 
- Add 404 & 403 page
- Detailed testing 
- Detailed testing 
- Complete README documentation

Furthermore, each user story is categorised into it’s relevant EPIC, to provide as clear working pathway and thorough planning of each individual app on the website.

### User Visitor Goals

- As a site visitor I would like to understand the purpose of the website when first accessing the home page.
- As a site visitor I would like to be able to view builds posted to the database.
- As a site visitor I would like to understand the registration process is mandatory to add my own builds.
- As a site visitor I would like to be able to easily create my own account and notified that I am logged in.

### User Member Goals 

- As a site member I can log into my account using the login button on all pages.
- As a site member I would like to see if I am still logged in.
- As a site member I would like to be able to upload my own builds using the built-in submission page.
- As a site member I would like to be able to edit and delete my posted builds once logged in.
- As a site member I can add comments to other builds in the database.

### Admin Goals

- As a site administrator I can approve comments left on individual builds.
- As a site administrator I can utilise full CRUD functionality on all posts on the database.

## Design

### Wireframes 

Wireframes for all HTML templates were created using [Balsamiq Wireframes](https://balsamiq.com/). These designs were used as the design basis of all html template pages.

IMAGE(s)

### Color Scheme

The color scheme was designed using [Coolers.co](https://coolors.co/). The primary colors used in this project are dark greys and gold, remeniscent both of the branding of Baldur's Gate itself as well as the color of treasure - a staple of any fantasy setting.

IMAGE

### Fonts

The main font used in the project is 'Libre Baskerville' - based on American Type Founder's Baskerville from 1941 and chosen again for it's proximity to the font used in the BG3 branding but also because it gives a antiquitean feeling to the website whilst also looking clean and grandiose.

IMAGE

Additional font used is 'Domine' - chosen for it's modern contrast to the more old-school Baskerville.

IMAGE

### ERD - DrawSQL

The main Entity Relationship Diagram (ERD) for the project was designed using the web service [DrawSQL](https://drawsql.app/). This diagram was used as the basis for the main Bgbuild database model for both individual instances of single builds and the comment model in relation to each individual build. Although some tweaks were made to the fields in place for the main model, this diagram was the single point of reference across the planning stage for the project.

IMAGE

## FEATURES

### NavBar

The NavBar element is everpresent across all pages as part the of base html of the site and sets the visual tone of the website. On the left-hand side, the site name is shown with an implemented color scheme as well as a custom designed icon for some flair, and to provide an appealing indicator of the site's purpose - as well as providing a constant link back to the home page.

IMAGE

The NavBar links on the right are organised in a reactive collapsable style, so as when the user is utilising the site on a smaller device the links fold into a hamburger menu, which will then dropdown the links when clicked.

IMAGE

IMAGE

When logged out, the user will have the option to go straight to the Build list and view the builds, or they can click login or register to access the relevant account functionality. When logged in, the account username is shown in place of the register link, and becomes a nested dropdown that stores links to the users' submitted builds and favourites.

IMAGE

IMAGE

### Footer 

Also part of the base html is the footer, which is styled inline with the NavBar for consistent branding. Inside the footer is a copyright notice, as well as an actionable link to the developer (my) Github page.

IMAGE

### Home Page

The home page serves as the first access point to the website, being linked to an empty URL redirecting traffic to the index. Utilised as the background is a loading page of Baldur's Gate III - an image of fantasy wilds with a bustling city in the background. Across the middle is the site branding, with contrasting fonts and colors, and a link to the build list page. Both of these elements combine to show a prospective user the purpose of the site in a clear manner as well as establishing the visual style of the product from the first click.

IMAGE

### Build List

The main build list is the main meat of the website. All submitted builds are displayed in bootstrap card format, listed by 4 to a row and paginated by 8, so most viewports will have an uncluttered view of the builds on display. Each build displays the number of comments and favourites attatched to it, as well as if the auth user has favourited. At the bottom of each build, there is a reactive button link to the build detail.

IMAGE

Each build card has a header, an image related to the build, and a few lines of information outlining the key points to the build. 
Also present in each build is a reactive class image - this variable template is linked to the main class of the database entry, so it will change depending on the base class used. 

IMAGE

The user who uploaded the build is listed in the bottom of the build information.

Inside the build list, the builds are listed from newest onwards. Any unnaproved builds are listed with italics and the explore button deactivated, showing clear and obvious build moderation.

IMAGE

### Search Bar

At the top of the build list page there is a search bar - linked to show the result of a filter query to the database for class name and build role. Users can enter a class name, e.g 'cleric' and the site will return a page rendered with the result of the filtered query.

IMAGE

### Add Build

Below the search bar on the build list page is a clear call to action to upload a build through a button marked with a 'plus' symbol. This will redirect unauthenticated users to register, and authenticated users to the add build form.

IMAGE

Once accessed, the add build form is a straightforward display of the Bgaddbuild form. Each field is clearly marked with large font and spacing.

IMAGE

Within the fields, there is a image field - this is linked to a Cloudinary database configured in the site settings.

IMAGE

As the build form has a lot of potential variables - each class has at least 3 subclasses - the form is controlled by a javascript script which reveals relevant build information when certain eventlisteners are fulfilled, so if the user has chosen a Barbarian class, the Barbarian subclass field will be revealed, and then hidden when a new class is chosen.

IMAGE

This process is also used on the multiclass field.

Also present is a link back to the main build list page for users to return if desired.

IMAGE

### Build Detail

The build detail page once accessed has the result of each add build form displayed in an accessible format, with the information being presented in a visually appealing and straightforward manner.

IMAGE

### Edit & Delete Build

Below the main build information but contained within the card body, there are two buttons which allow authenticated build post owners to either edit or delete their builds.

IMAGE

Edit build will take users to the add build form, where they can adjust the fields of their build and resubmit to the database. Once reposted, a Django message will inform the user of their successful edit.

IMAGE

Delete build will redirect authenticated users to a delete confirmation page - letting the users know that the action is permanent and irreversible.

IMAGE

### Favourite Build

Below the card body with the build information, the number of comments and favourites is displayed. The favourite button is reactive depending on the authentication state of the user - if the user is unauthorised, the favourite button will be hidden and just the number of favourites will be shown, but if the user is logged in the button will be available. Furthermore, if the user has already favourited the build, the button will be red to show previous interaction with the build. Users can favourite and unfavourite at will.

IMAGE

### Comment & Reply

Contained below the build detail is the comment form. Authenticated users are able to leave comments on each build post, with a Django message confirmation shown after each comment. Comments are displayed within another card, listed by user and submission time & date.

IMAGE

Furthermore, each comment contains an individual instance of a reply form, linked to the id of the parent comment. This allows users to give text-based reactions to other comments.

IMAGE

### My Builds

Authenticated users, once logged in, can access a list of their submitted build by clicking on their account name and the 'my builds' link in the dropdown list. This page display is a filtered queryset showing only builds that have been created by the user, displayed in the same manner as the main build list.

IMAGE

### Favourite Builds

Also within the authenticated user dropdown is the favourite builds tab. As above, this filters the main model to only display the builds with a relevant many-to-many field accessed by the authenticated user, and again shown in the same manner as the main build list.

IMAGE

### Account Interaction

Using Django's Allauth system, users can register, login and logout at their convenience. These pages have solid backgrounds to provide a visual distinction to the main site and ensure the user is focused when inputting any sensitive information.

### Error Pages

Continuing the visual theme of the account pages, the site has custom styling for 403, 404 and 500 error pages. When accessed, these pages will display the error and provide users a clear link back to the home page.

IMAGE 

IMAGE

IMAGE

## SECURITY

### Env.py

Sensitive information, such as API and secret keys, contained within the env.py file are hidden from deployment and therefore unable to be accessed by outside actors.

### Defensive Programming Measures

Utilised within the code are several authentication measures such as {% if user.is_authenticated %}, barring anauthenticated users from accessing areas roped off for site memebers.

Within the Django class-based views the security based mixins - LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin - are used for extra protection against unauth users gaining access to areas marked for users only.

### Input Validation

Within the account forms and add build form there is input validation built in, disallowing users from submitting empty fields. 

Furthermore, for the difficulty rating, the max number validator is in place to stop users submitting a value above 5.

## BUGS

### Known Bugs

### Unfixed Bugs




## FUTURE FEATURES 

By design, build.mt is envisioned as a framework wherein extra games can be plugged in to the system through quite simple processes. With this in mind, I had originally hoped to include From Software's 2022 release 'Elden Ring' in intial deployment as an additional build catalogue - however time constraints affected this plan. However this is still an option for ongoing development.

Further interaction with the comment section was also planned - allowing users to edit and delete their comments.

Allowing users to sort the build list page by class or build role is also planned to be implemented in the future.

## TESTING



## DEPLOYMENT

### Local Deployment

Project was initially created in Gitpod before being migrated to VSCode.

Git commands were were grouped into the following commit messages;

- "feat" - feature work
- "maint" - maintenance work
- "docs" - documentation work

All commands passed through the git commit -m command, and pushed to github with git push.

### Environmental Variables

The deployment process followed is based primarily from Code Institutes 'I Think Therefore I Blog' Walkthrough project.

- Create env.py in root directory of project.
- Add env.py to .gitignore.
- Add DATABASE_URL, SECRET_KEY and CLOUDINARY_URL to env.py.
- Open settings.py in build_mt main project directory.
- Import env.py.
- Add paths for DATABASE_URL, SECRET_KEY and CLOUDINARY_URL.
- Ensure INSTALLED_APPS, MIDDLEWARE, STATICFILES, TEMPLATES are all configured correctly.
- Ensure ALLOWED_HOSTS has .herokuapp in array.
- Run python manage.py collectstatic to pool all staticfiles in correct folder.
- Create Procfile in root directory & initialise gunicorn wsgi.
- Freeze requirements to requirements.txt.
- Turn debug to 'False' in settings.py.

### Heroku Deployment

In Heroku;

- Log in or register, then click 'create app'.
- In the new app menu, click on deploy.
- Connect the project to Github by clicking on the deployment method, selecting Github, and locating the repository.
- In the settings tab, add DATABASE_URL, SECRET_KEY and CLOUDINARY_URL as config vars.
- Back in the deploy tab, click deploy branch at the bottom of the page if the correct branch is selected above (main by default).
- View app when the process is complete.

### Forking & Cloning

To fork this repository;

1. On Github, navigate to [the build.mt repository](https://github.com/AlbaXIII/build.mt).
2. In the top-right hand corner of the page, click fork.
3. Choose an owner for the forked repository.
4. Optionally, rename, add a description, and/or copy the default branch only.
5. Click create fork.

To clone this repository;

1. On Github, navigate to [the build.mt repository](https://github.com/AlbaXIII/build.mt).
2. Above the list of files click <> Code.
3. Copy the URL of the repository - you may choose to clone by HTTPS, using a SSH key, or Githubn CLI.
4. Open Git Bash or other IDE.
5. Navigate to your selected working directory.
6. Type git clone, then post the URL.
7. Press enter. 

## TECHNOLOGIES USED

### Main Software

- Django
- Python
- HTML 
- CSS
- CI PostgreSQL Database

### Modules

Relevant installed modules below;

- cloudinary==1.36.0 - allow users to store images in purpose-built offsite storage.
- crispy-bootstrap5==0.7 - crispy forms stylings for add/edit build form.
- dj-database-url==0.5.0 - 
- dj3-cloudinary-storage==0.0.6 - storage link to Cloudinary.
- Django==4.2.17 - main Django version.
- django-allauth==0.57.2 - Allauth used for user authentication and registration.
- django-crispy-forms==2.3 - crispy forms for add/edit build form.
- django-summernote==0.8.20.0 - advanced admin tool.
- gunicorn==20.1.0 - web server gateway interface for python. 
- oauthlib==3.2.2 - framework for Oauth logic.
- psycopg2-binary==2.9.10 - PostgreSQL driver.
- python3-openid==3.2.0 - decentralised identity system for application.
- sqlparse==0.5.3 - sql parser for Python.
- whitenoise==6.9.0 - middleware for serving static files.

### Django Imports

- cloudinary - full import for HTTPS error on images.
- cloudinary.models\CloudinaryField - ImageField for Cloudinary storage.
- django.contrib\admin - Default admin interface.
- django.contrib.auth.mixins\LoginRequiredMixin, UserPassesTestMixin - Django security mixins.
- django.contrib.auth.models\User - Default Django User model.
- django.contrib\messages - Django message functionality.
- django.contrib.messages.views\SuccessMessageMixin - Django notification mixin.
- django.core.validators\MaxValueValidator, MinValueValidator - default Django integer max/min validators.
- django.core.wsgi\get_wsgi_application - create app object.
- django forms - default Django forms.
- django.http\HttpResponseRedirect - returns Http status code 302.
- django.shortcuts\render, get_object_or_404, reverse - Fetch object from list or 404 error, reverse URL code.
- django_summernote.admin\SummernoteModelAdmin - Advanced Admin functionality provided by Summernote.
- django.urls\path, include - Django default URL paths, include for layering.
- django.views.generic\TemplateView, ListView - Django default Template & List views
- django.views\generic - Generic display views.
- uuid - apply Universally Unique Identifiers.

### Additional Software

- Adobe Illustrator - logo design
- [Cloudinary image converter](https://cloudinary.com/tools/png-to-webp) - condense images to .webp format

## CREDIT & ACKNOWLEDGEMENTS

### Image Credits

### Code Inspiration

### Special Thanks

- My mentor Dick Vlaanderen, for his advice.
- My friends Sam, Penny and especially Kate for their support, input and tolerance!