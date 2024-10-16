# Crowdfunding Back End
Anaya Dodge

## Planning:
### HarveztCirkle
A crowdfunding platform inspired to uplift the building of community-driven urban gardens and strengthening the spirit of communal sharing.  Our goal is to elevate and support both new and existing urban gardens, whether they be on balconies, rooftops, backyards, or community gardens.  

### Intended Audience/User Stories
-  New and/or aspiring urban gardeners looking to receive support to get up and running.
-  Community leaders or organisers looking to launch their community garden project.
-  Existing urban gardeners looking to get financial assistance.

### Front End Pages/Functionality
- Home Page (Anybody can view)
    - A list of completed/closed Projects.
    - A list of open/seeking supporter Projects with a short summary, their fundraising goal and progress.
    - A link to sign up as a new user or login.
    - A link to create a new Project.
    - As anybody, I can not create a Project.  I am redirected to the User login page.
    - As a User, I am directed to the Project Creation page.
- Login/Sign up Page (Anybody can view)
    - Captures username/email address and password to login.
    - Once User is logged in, it will redirect them to the User Profile Page.
- Project Creation Page (Users can view and create only)
    - As a User I can upload a photo to the Project.
    - I can create the Project Title, text details (no char limit), and the summary blurb (<100 char) to display on the Home Page.
    - I can add the Pledge funding goal amount.
    - I can select a (boolean) option whether the Project is open for Pledges or Closed.
    - The Project Creation date is captured automatically once completed.
- Project Detail Page (Anybody can view, Owners can edit, Users can create a Pledge)
    - As anybody, I can view the Project descriptions, goals, date created, funding progress, and available pledge options.
    - As anybody, I can view a list of previous comments from supporters, including anonymous pledges with the amount pledged only.
    - As the Owner, I can edit the Project details.
    - As the Owner, I can delete the Project.  The delete function cascades to delete all Pledges that are attached to the Project.
    - As a User/Supporter, I can not edit the Project details.
    - As a User/Supporter I can make a pledge including the following as optional: 
        - To keep my username/name as anonymous and display the amount only.
        - To leave a comment in addition to the pledge.
    - As the Owner, I can change the Project status to Open for Pledges or Closed for Pledges.
- User Profile Page (Only User Owner can view and edit)
    - As the Owner of a Project, I can access a list of links to my previously created Projects.
    - As a User, I can view my previous pledges including anonymous.
    - As a User, I can edit the comment, delete or anonymise my Previous Pledges.  I can not edit the Pledge amount.
    - As anybody, I do not have access.
    - As a User, I only have access to my own Projects and Pledges.  I do not have access to anybody else's.
    - As a User, I can edit/upload my profile picture.
    - As a User, I can edit my email address and contact details.  
    - As a User I can not edit my username.
    - As a User I can delete my User Account.  This will cascade to delete all details except Pledge amounts attached to Projects.
- Custom 404 Error Page
    - To be displayed upon a 404 error.

### API Spec  (TBD)

Current WIP in Google Sheets - <https://docs.google.com/spreadsheets/d/1ACvwULLxWViPqJfXjPXxRTgflq9LrYQnFXFYjVkPopc/edit?usp=sharing>

| URL | HTTP Method | Purpose | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
|     |             | ------- | ------- | ------------ | --------------------- | ---------------------------- |
|     |             |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |


### DB Schema (TBD)
![]( {{ ./relative/path/to/your/schema/image.png }} )