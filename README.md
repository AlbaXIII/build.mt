# BUILD.MT

## Introduction

build.mt is an online catalogue for the collection, sharing and review of character builds in role-playing games (RPGs). Many modern RPGs have an overabundance of character creation options, with many diverging paths, abilities, spells, gear – it’s enough to confuse many casual fans or first time players trying RPGs for the first time. built.mt is designed to take the stress out of choosing how to play a character. Prospective players can create an account, share their characters and how they play, strengths and weaknesses, and most of all – how fun they are to play! 

As well as a catalogue of build ideas, build.mt has an easy to read explanation page for each featured RPG so potential players (and account holders) can learn the basics of the game without being overwhelmed by information.

To summarise, build.mt is character inspiration made simple.

build.mt was designed initially with Larian’s 2023 release ‘Baldur’s Gate III’ and From Software’s 2022 release ‘Elden Ring’ – two of the most popular and creative RPGs on the markets, with myriad options of how to play.

This is my fourth Code Institute project and was developed using HTML, CSS, JavaScript, Python, Django, and PostgreSQL. 

View the website and join the community [here].

## Table of Contents

-----------------------------
 
## User Experience

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

## User Stories

### Agile Working

Before starting the coding on build.mt, I created a custom user story template and linked it to the project Kanban board, to allow me to create an iterative and fluid development and deployment schedule. The use of the board allowed me to isolate applications and functions of the code and work on them in iterative sections, whilst keeping track of the status of each particular function of the code.

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
- Sort builds by class
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

-----------------------------

