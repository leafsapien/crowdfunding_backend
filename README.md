# Crowdfunding Back End
by Anaya Dodge

> In order to interact with this content using Insomnia, you must first activate your Virtual machine and turn on your Server using the following commands in the terminal:
> - .venv/Scripts/activate
> - python manage.py runserver

## Project Requirements
- [x] (1/2 done - Front end site coming next) Be separated into two distinct projects: an API built using the Django Rest Framework and a website built using React.
- [x] Have a unique and creative project name (bonus points for puns and missing vowels!).
- [x] Define a clear target audience for the platform.
- [x] Implement user accounts with the following attributes:
    - [x] Username
    - [x] Email address
    - [x] Password
- [x] Enable users to create a "project" to be crowdfunded with at least these attributes:
    - [x] Title
    - [x] Owner (a user)
    - [x] Description
    - [x] Image
    - [x] Target amount to fundraise
    - [x] Status of accepting new supporters (open/closed)
    - [x] Creation date
- [x] Allow users to make "pledges" to a project, including at least these attributes:
    - [x] Amount
    - [x] The project the pledge is for
    - [x] The supporter/user (who created the pledge)
    - [x] Option for anonymous pledging
    - [x] Comment on the pledge
- [x] Implement suitable update/delete functionality, e.g., define if a project owner can update project details.
- [x] Define permissions, e.g., specify who can delete a pledge.
- [x] Return relevant status codes for both successful and unsuccessful API requests.
- [ ] (For the front end functionality in future project) Handle failed requests gracefully (e.g., implement a custom 404 page instead of a default error page).
- [x] Use Token Authentication, including an endpoint for obtaining a token along with the current user's details.
- [ ] (For the front end functionality in future project) Ensure responsive design for mobile and desktop compatibility.

## Planning:
### HarveztCirkle
A crowdfunding platform inspired to uplift the building of community-driven urban gardens and strengthening the spirit of communal sharing.  Our goal is to elevate and support both new and existing urban gardens, whether they be on balconies, rooftops, backyards, or community gardens.  

### Intended Audience
- Community members seeking funding to begin an edible garden with the intention of sharing the excess produce within their local community.
- Existing and/or established community gardens seeking funding for expansion or new works related to edible produce that is shared communally (not for profit).
- Community members and/or any persons wanting to contribute financial support towards the creation or upgrading of community gardens for edible purposes.

### User Stories
**For Users**
-  As a new visitor I want to sign up and create a personal account so that I can participate in the community.
-  As a user I want to log in securely so that I can access my account details and manage my contributions.
-  As a user I want to update my profile details (like email or contact information) so that my information remains current.
-  As a user I want to delete my account so that my data can be anonymised and I can leave the platform if I wish to.
-  As a user I want to create new projects so that I can receive support for my urban gardening initiative.
-  As a user I want to pledge support to projects so that I can contribute to the initiatives that I care about.
-  As a user I want the option to make my pledge anonymous so that I can keep my identity private if I choose to.
-  As a user I want to view my past pledges so that I can keep track of my contributions and see the impact I have made.

**For Project Owners**
-  As a project owner I want to create detailed project descriptions so that I can clearly communicate my goals to potential supporters.
-  As a project owner I want to compare the money donated so far from supporters against the goal funding amount so that I can track the progress towards the funding goal.
-  As a project owner I want to view a list of pledges and comments made on my projects so that I can engage with my supporters.
-  As a project owner I want to edit or close my project when necessary so that I can keep it relevant and/or end the campaign when my funding goal is met.

**For Administrators (aka SuperUsers)**
-  As an administrator I want to delete or anonymise users or projects so that sensitive or abandoned data is handled securely and responsively.
-  As an administrator I want to manage user accounts and project records so that I can enforce platform rules and remove inappropriate and/or rule breaking content.
-  As an administrator I want to access to view all pledge and project information so that I can moderate the platform appropriately.

### Front End Pages/Functionality
- Home Page
    - Access Level: Publicly accessible to all viewers.
    - Purpose: Display open and completed projects and prompt new visitors to create account or existing users to sign in.
    - Features:
        - A list of open/seeking supporter Projects with summaries, fundraising goals, and progress.
        - A list of completed Projects.
        - A link to log in or signup.
        - A link for the project creation page where:
            - Non-authenticated users are redirected to the login page when attempting to create a project.
            - Authenticated users are directed to the project creation page.

- Login/Sign up Page
    - Access Level: Publicly accessible to all viewers.
    - Purpose: Allows users to login or new visitors to sign up to join.
    - Features:
        - Log in with username/email and password.
        - Redirects to the profile page upon successful authentication.

- Project Creation Page
    - Access Level: Authenticated users only.  Non-authenticated users are prompted to login/signup page.
    - Purpose: Enables users to create new projects.
    - Features:
        - Fields for the title, description, image upload, funding goal, and an option to accept pledges.
        - Automatically captures the project's creation date.
 
- Project Detail Page
    - Access Level: Anybody can view, only project owners and admin can edit, only admin can delete (cascade deletion of related pledges), only authenticated users can add a pledge.
    - Purpose: Displays detailed information for the project.
    - Features:
        - Detailed project descriptions, goal, creation date, funding progrress.
        - Anonymous and regular pledge details and comments.

- User Profile Page
    - Access Level: Authenticated user owner only, or admin.
    - Purpose: Provides access to user projects, pledges, and profile management.
    - Features:
        - Links to created projects ("My Projects") and list of past pledges ("My Pledges") (including anonymised pledges).
        - Profile management includes editing email address, contact details and profile picture.  User can not change username.
        - Account deletion request to anonymise their data.  (On the back-end this request will go to the admin to review and prompt deletion/anonymisation of content so as to not affect any open projects/relevant pledges)

- Custom 404 Error Page
    - Access Level: Display for any 404 errors.
    - Purpose: Provides a user-friendly message for not found errors.

## API Specifications

| URL                | HTTP Method | Purpose                                                            | Request Body                                                                                          | Success Response Code | Authentication/Authorisation           | Complete |
|--------------------|-------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------|-----------|
| projects/          | GET         | Returns all projects                                               | N/A                                                                                                   | 200                   | None                                   | [x]       |
| projects/          | POST        | Creates a new project                                              | title: string, description: string, goal: int, image: url, is_open: bool, date_created: UTC, owner: FK | 201                   | Bearer Token for User                  | [x]       |
| projects/<int:pk>/ | GET         | Returns project with INT ID                                        | N/A                                                                                                   | 200                   | None                                   | [x]       |
| projects/<int:pk>/ | PUT         | Edits an existing Project with INT ID, e.g., Closing Project       | project id: int, & any details that require updating.                                                 | 200                   | Bearer Token for User & be Project Owner | [x]   |
| projects/<int:pk>/ | DELETE      | Permanent cascade deletion of project and all associated pledges   | N/A                                                                                                   | 202                   | Admin ONLY                              | [x]       |
| pledges/           | GET         | Returns all pledges                                                | N/A                                                                                                   | 200                   | Admin ONLY                              | [x]       |
| pledges/           | POST        | Creates a new pledge                                               | Amount: int, comment: string, anonymous: boolean, project: pk, supporter: fk                          | 201                   | Bearer Token for User                  | [x]       |
| pledges/<int:pk>/  | GET         | Returns pledge with INT ID                                         | N/A                                                                                                   | 200                   | Bearer Token for User & be Pledge Owner | [x]   |
| pledges/<int:pk>/  | PUT         | Edits an existing pledge with INT ID                               | Pledge id: int, & any details that require updating.                                                  | 200                   | Bearer Token for User & be Pledge Owner | [x]   |
| pledges/<int:pk>/  | DELETE      | Permanent deletion of pledge with INT ID                           | N/A                                                                                                   | 202                   | Admin ONLY                              | [x]       |
| users/             | POST        | Creates a new user                                                 | username: string, email: email, password: string, first_name: string, last_name: string               | 201                   | Unique Username and Email address      | [x]       |
| users/             | GET         | Returns list of all users for dev queries                          | N/A                                                                                                   | 200                   | Admin ONLY                              | [x]       |
| users/<int:pk>/    | GET         | Returns user details for INT ID                                    | N/A                                                                                                   | 200                   | Bearer Token for User                  | [x]       |
| users/<int:pk>/    | PUT         | Edits user details with INT ID                                     | User id: int, & any details that require updating (Username excluded)                                 | 200                   | Bearer Token for User                  | [x]       |
| users/<int:pk>/    | DELETE      | Permanent deletion of user and associated projects/pledges         | N/A                                                                                                   | 202                   | Admin ONLY                              | [x]       |
| /api-token-auth/   | POST        | Creates a JWT for User                                             | N/A                                                                                                   | 201                   | Correct username and password          | [x]       |


## Insomnia Testing Specifications

> In addition to meeting the base Project requirements, I have developed comprehensive Testing Specifications to be used in Insomnia as follows.

| Filter Type | Endpoint                | Action                                                                                  | Expected Result          | Success |
|-------------|--------------------------|-----------------------------------------------------------------------------------------|--------------------------|---------|
| Users       | /users/<int:pk>          | DELETE as the ADMIN                                                                     | 204                      | [x]     |
| Users       | /users/<int:pk>          | DELETE as anyone (non token bearer)                                                     | 401                      | [x]     |
| Users       | /users/<int:pk>          | DELETE as DIFFERENT token bearer                                                        | 401                      | [x]     |
| Projects    | /projects/<int:pk>       | DELETE as the ADMIN                                                                     | 200                      | [x]     |
| Projects    | /projects/<int:pk>       | DELETE as a different Token Bearer                                                      | 403                      | [x]     |
| Pledge      | /pledge/<int:pk>         | DELETE related Pledge as the ADMIN as consequence of "Cascade Deletion" of related Project | 200                      | [x]     |
| Pledge      | /pledge/<int:pk>         | DELETE as the ADMIN                                                                     | 200                      | [x]     |
| Pledge      | /pledge/<int:pk>         | DELETE as a DIFFERENT Token Bearer                                                      | 403                      | [x]     |
| Pledge      | /pledge/<int:pk>         | DELETE as anyone (non token bearer)                                                     | 403                      | [x]     |
| Pledge      | /pledge/<int:pk>         | DELETE non existent pledge                                                              | 404                      | [x]     |
| Projects    | /projects/<int:pk>       | DELETE non existent project                                                             | 404                      | [x]     |
| Users       | /users/<int:pk>          | DELETE non existent user                                                                | 404                      | [x]     |
| Users       | /users/                  | GET Users list as anyone                                                                | 401                      | [x]     |
| Users       | /users/                  | GET Users as Admin                                                                      | 200                      | [x]     |
| Users       | /users/                  | POST a new User with original username and email                                        | 201                      | [x]     |
| Users       | /users/                  | POST a new User with duplicate username and email to previous User                      | 404                      | [x]     |
| Users       | /users/                  | POST a new User with missing required information                                       | 400                      | [x]     |
| API Token   | /api-token-auth/         | POST token with correct username + password provided                                    | 200                      | [x]     |
| API Token   | /api-token-auth/         | POST token with incorrect username + password provided                                  | 400                      | [x]     |
| Users       | /users/<int:pk>          | GET User details as anyone                                                              | 404                      | [x]     |
| Users       | /users/<int:pk>          | GET all User details as Bearer Token Owner OR Admin                                     | 200                      | [x]     |
| Users       | /users/<int:pk>          | GET User details for User that does not exist                                           | 404                      | [x]     |
| Users       | /users/<int:pk>          | PUT - Edit User details for Bearer Token owner or Admin (Except username)               | 400                      | [x]     |
| Users       | /users/<int:pk>          | PUT - Edit User details as NON-matching Bearer Token owner                              | 401                      | [x]     |
| Users       | /users/<int:pk>          | PUT - Edit User details as anyone                                                       | 401                      | [x]     |
| Projects    | /projects/               | GET Projects list as anyone                                                             | 200                      | [x]     |
| Projects    | /projects/               | POST New complete project with Bearer Token                                             | 201                      | [x]     |
| Projects    | /projects/               | POST New project as anyone                                                              | 401                      | [x]     |
| Projects    | /projects/               | POST New incomplete project with Bearer Token - Missing compulsory fields               | 400                      | [x]     |
| Projects    | /projects/<int:pk>       | PUT - Edit Project Details as Token Bearer and Project Owner or Admin                   | 200                      | [x]     |
| Projects    | /projects/<int:pk>       | PUT - Edit Project Details as Token Bearer and NOT Project Owner                        | 403                      | [x]     |
| Projects    | /projects/<int:pk>       | PUT - Edit Project Details as anyone                                                    | 401                      | [x]     |
| Pledges     | /pledge/                 | GET Pledge list as anyone                                                               | 400                      | [x]     |
| Pledges     | /pledge/                 | GET Pledge list as Superuser Bearer Token                                               | 200                      | [x]     |
| Pledges     | /pledge/                 | POST New Pledge against Project as Token Bearer or Admin AS not anonymous               | 200                      | [x]     |
| Pledges     | /pledge/                 | POST New Pledge against Project as Token Bearer or Admin AS anonymous                   | 200                      | [x]     |
| Pledges     | /pledge/                 | POST New Pledge against Project as Token Bearer or Admin with incomplete details        | 400                      | [x]     |
| Pledges     | /pledge/<int:pk>         | PUT - Edit Pledge against Project as Token Bearer Pledge Owner or Admin                 | 200                      | [x]     |
| Pledges     | /pledge/<int:pk>         | PUT - Edit Pledge against Project as non-Token Bearer Pledge Owner                      | 400                      | [x]     |
| Pledges     | /pledge/<int:pk>         | PUT - Edit Pledge against Project as anyone                                             | 400                      | [x]     |
| Pledges     | /pledge/                 | POST New Pledge against Project as anyone                                               | 401                      | [x]     |
| Pledges     | /pledge/<int:pk>         | GET Pledge details IF is_anonymous = True                                               | 200                      | [x]     |
| Pledges     | /pledge/<int:pk>         | GET Pledge details IF is_anonymous = False                                              | 200                      | [x]     |
| Pledges     | /pledge/                 | POST Pledge with Bearer Token where Project does not exist                              | 400                      | [x]     |


### Screenshots of successful Insomnia Tests for API Actions

**GET Method**

![GET Method screen capture](/crowdfunding/img/getmethod.gif)

**POST Method**

![POST Method screen capture](/crowdfunding/img/postmethod.gif)

**Token Return (aka User Authentication)**
> Note: This Test User is now deleted, so the Token shown is no longer valid.

![POST Token Authentication Method screen capture](/crowdfunding/img/apitokenmethod.gif)

### How to create a new user and new project using Insomnia

**Create New User**
1. Create a new HTTP Method: POST
2. Paste the URL: https://harveztcirkle-ec4dcb75e485.herokuapp.com/users/
3. Paste and replace the relevant content in the body: (JSON)

```
{
	"username": "<string>",
	"email": "<email>",
	"password": "<string>",
	"first_name": "<string>",
	"last_name": "<string>"
}
```
> Note: The username and email address must be unique.

**Create New Project**
1. Create a new HTTP Method: POST
2. Paste the URL: https://harveztcirkle-ec4dcb75e485.herokuapp.com/projects/
3. Paste and replace the "..." content in the body: (JSON)

```
{
	"title": "<string>",
	"description": "<varchar>",
	"goal": <int>,
	"image": "<link>",
	"is_open": true,
    "owner_id": <int>
}
```

## Database Schema (Entity Relationship Model)

Made using DB Diagram - [link](https://dbdiagram.io/d/Crowdfunding-Backend-ERM-671b6bdc97a66db9a340b793)

![ERM Database Schema](/crowdfunding/img/db_erm.png)

### Deployed Project Link
**Note: this will only work inside Insomnia** -> [link](https://harveztcirkle-ec4dcb75e485.herokuapp.com/)