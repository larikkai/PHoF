# Padel Hall of Fame - User instructions

Open the app's homepage at http://padel-hall-of-fame.herokuapp.com/

On the homepage, you can observe the functionality of the application and read general information.

## Getting Started

Some of the application's functions can only be used by a user who is sign up and logged in or require user type to be admin.

For general navigation, use the links in the navigation bar:

![alt text](https://raw.githubusercontent.com/larikkai/PHoF/master/documentation/navbar_info.PNG "navbar info")

### Visitor

As a visitor, you can read the front-page news and view the list of games. For testing purposes, you can use pre-created user or admin type accounts:

| User type        | Username      | Password        |
| :-------------: |:-------------:| :-------------: |
| Admin           | admin         | test123         |
| User            | test_user1    | test123         |


### Sign up

If desired, as visitor you can create your personal account by filling out the forms on the sign-up page.

#### Sign up form validation
| Form            | Min           | Max             | Unique          |
| :-------------: |:-------------:| :-------------: | :-------------: |
| First name      | 3             | 10              | full name: true |
| Last name       | 3             | 15              | full name: true |
| Username        | 3             | 15              | true            |
| Password        | 4             | 15              |                 |

After successful sign up, application will redirect you to login page.

### Logging

After successful sign up or if desired (sign up earlier), you can login into the application. Use navigation bar link to entry Login page, fill out login forms and press Login. 

### Logout 

When you stop using the application, you can log out by pressing Logout in the navigation bar.

## Games and tournaments

### Add games or tournaments

As sign up user you can create new game, user navbar to entry Add a game or Add a tournament page. Invent the game name and fill it in the game name field, select the number of players from dropdown form. When done click Add a new game / tournament.

### Join or leave game or tournament

As sign up user you can you can join into a game or tournament. Browse games or tournaments, if you are qualified to join, join button is visible. If you are joined to an game or a tournament and it is not full, you can leave the game or tournament. After the game or the tournament is full you cannot leave.

## Ranking and news

At ranking page you can observe statistic from the application. The news rotates in the bar on the front page, more details can be found on the news page.
It is convenient navigation bar link to navigate.

## User types

The upper type contains, in addition to its own rights, all the rights of the lower types. User can manage the application on admin page, admin bar is only visible if user type is admin.

### Admin 

Admin can remove any game or tournament.
Admin can change any single game or tournament game result.

Admin can remove user.

### User

Add, join, leave games or tournaments and set or confirm game result.
