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

After successful sign up, app will redirect you to login page.

### Logging

After successful sign up or if desired (sign up earlier), you can login into the app by filling out login forms at login page. 

### Logout 

When you stop using the app, you can log out by pressing Logout in the navigation bar.

## Games and tournaments

### Add games or tournaments

As sign up user you can create new game in Add a game page. Invent the game name and fill it in the game name field, select the number of players from dropdown form. When done click add new game / tournament.

### Join or leave event

As sign up user you can you can join into a game or tournament. Browse games or tournaments, if you are qualified to join, join button is visible. If you are joined to an event and it is not confirmed, you can leave the event. After event is confirmed you cannot leave.

## User types

The upper type contains, in addition to its own rights, all the rights of the lower types. User can manage the app on admin page, admin bar is only visible if user type is admin or above.

### Superuser

Can promote user to admin.

### Admin 

Admin can remove confirmed event or change result in any given time.

Admin can remove user.

### User

Add, join, leave games or tournaments and set or confirm game result.
