# The Cookery Cove

## UX

This web application is made for users who would like to store and easily access cooking recipes of different cuisines, categories, ingredients and difficulties. 
My target market could include anyone of any age group, but more specifically, this application is made for people who enjoy cooking, learning new recipes and wanting to share their own recipes with the online community.
This type of user will want to be able to have their own account where they can add, edit or delete any of their recipes, view recipes of different ingredients, categories and difficulties, and also explore different cuisines.
This user will also want to be able to know what allergens or main ingredients there are in these recipes, and how long these recipes will take to prepare and complete.
My project is a suitable way of achieving this because it provides a form for the user to use when signing in or registering onto the application, filters which will be used to sort recipes by categories, difficulties and cuisines, and functions which will allow the user to create and update their own recipes, as well as delete them.

General User Stories:

 - As a user type, I want to be able to create an account with my own username and password, and login with these credentials each time I want to access the application.
 - As a user type, I would like to be able to login and create my own recipes.
 - As a user type, I would like to be able to view a recipe based on the cuisine, ingredient or difficulty it belongs to. 
 - As a user type, I would like to be aware of what allergens are in each recipe. 

Real Life User Stories:

 - User 1: I'd like my username to be 'USER1' and would also like to have my own password when logging in.
 - User 2: I would like to be able to find a variety of vegetarian or vegan recipes.
 - User 3: I would like to create a recipe for a 'Classic Trifle'.
 - User 4: I would like to be able to select certain allergens whilst creating a recipe.

Wireframes:

 - Wireframes have been created using [Wireframe.cc](https://wireframe.cc/). These can be viewed in /documentation. 

Database Schema:

![Database Schema](/documentation/database_schema.png)

A more detailed version of the UX Planes can be found [here](/documentation/ux_planes.pdf).

## Features

 - Login/Register form - this will allow the user to either log into an existing account or create a new account, inserting them into the database.
 - Add/edit recipe form - this will allow logged in users to either create a new recipe (which will be inserted into the database) or edit one of their own existing recipes (which will be updated).
 - Delete recipe function - this will allow the logged in user to delete one of their own recipes, completely removing it from the database.
 - Filter by category, cuisine, main ingredient or difficulty - this will allow the user to sort recipes by these filters, directing them to a page displaying these sorted recipes.
 - Filter by cuisine - this will allow the user to be shown all recipes from a specific cuisine which they have chosen from the homepage.
 - Log out - this will allow the user to log out of the current session, also providing them the option to return to the homepage or log back in.

### Existing Features

 - Register form allows User 1 to create their chosen username 'USER1' and have a password of their choice which they can use to log in.
 - Filters on homepage allow User 2 to find vegetarian OR vegan recipes (but not both at the same time).
 - Add/edit recipe form allows User 3 to create their 'Classic Trifle' recipe. They can then view this in 'My Recipes' and 'All Recipes'.
 - Add/edit recipe form allows User 4 to select various allergens to be listed in their recipe when it is submitted into the database.
 - Delete recipe function allows all users to delete their own recipes, however, at this point in time, any user can delete any other user's recipes which is one disadvantage. 
 - Logout allows all users to log out of their current sessions, providing them the options to return to homepage or log back in.

### Features Left to Implement

 - Like/Dislike recipe - this feature would allow the user to like or dislike any recipe. The results of these likes and dislikes would then be displayed on a graphical chart with D3.js. 
 - Favourite a recipe - this feature would allow the user to save their favourite recipes and view them under 'Favourite Recipes'.
 - Most popular/most recent recipes - this feature will display most popular/most recent recipes based on how many likes the recipe received or how recently the recipe was created.

## Technologies Used

- HTML
    - This project uses **HTML** to build the foundation of the web application and includes links to Materialize, Materialize JS, CSS, and Font Awesome.
- CSS
    - This project uses **CSS** to style the features of the web application, including the header, footer and each page of the cookbook.
- [JavaScript](https://www.javascript.com/)
    - This project uses **JavaScript** for interactive functionality of the application.
- [Python](https://www.python.org/)
    - This project uses **Python** to provide the backend functionality of the cookbook, including functions to add, edit or delete a recipe.
- PyMongo
    - This project uses **PyMongo** which is a MongoDB driver for Python, used to access the MongoDB database.
- [JSON](https://www.json.org/)
    - This project uses **JSON** within mLab to provide the core data for the cookbook, including recipes, users, categories, etc.
- [mLab](https://mlab.com/)
    - This project uses **mLab** to host the database for the application.
- [Flask](http://flask.pocoo.org/)
    - This project uses the **Flask** microframework to bring the frontend and backend of the application together.
- [jQuery](https://jquery.com/)
    - This project uses **jQuery** which is included with Materialize to initialise many of the Materialize components used within the application (script found in base.html). 
- [MongoDB](https://www.mongodb.com/)
    - This project uses **MongoDB** which is used to contain the database collections.
- [Font Awesome](https://fontawesome.com/)
    - This project uses **Font Awesome** to provide icons for the application.
- [Wireframes.cc](https://wireframe.cc/)
    - This project uses **Wireframes CC** for the Skeleton and Surface Plan, providing desktop, tablet and mobile views of the web application.
- [Google Fonts](https://fonts.google.com/)
    - This project uses **Google Fonts** to provide fonts for the headings of the web application.

## Testing

### Manual Tests

This web application has been manually tested with different scenarios that the user may experience.

1. Sign In
    1. Click on 'Sign In' in the header or in the welcome card and be directed to 'signin.html'.
    2. Sign in with username 'USER1' and password 'user1'.
    3. Click on 'Sign In' and be directed back to the homepage.
    4. Check the user is logged in by seeing if 'Add Recipe' and 'My Recipes' are available in the navigation.

2. Register
    1. Click on 'Register' in the header or in the welcome card and be directed to 'register.html'.
    2. Choose a username and password of your choice.
    3. Click on 'Register' and be redirected to 'home.html'.
    4. Check the user is logged in by seeing if 'Add Recipe' and 'My Recipe' are available in the navigation. 

3. Homepage
    1. Click on the brand logo in the top-left corner of the page or click on 'Home' in the navigation bar.
    2. Be directed to 'home.html'.

4. Recipes by...
    1. Choose to filter by category, difficulty or ingredient and select an option from the dropdown.
    2. Be directed to appropriate page depending on whichever filter has been chosen.

5. Recipes By Cuisine
    1. From the homepage, choose a cuisine and be shown cuisine description and a button to view all recipes by chosen cuisine.

6. All Recipes
    1. Choose 'All Recipes' in the navigation bar and be directed to 'allrecipes.html'. 
    2. Be shown all recipes in the database on one page.
    3. Be shown recipe description and details when card is clicked on.

7. View Recipe
    1. Click on 'View Recipe'
    2. Be directed to the get_recipe page and be shown all details of the recipe, including the ingredients, method and image.

8. Add Recipe
    1. If username is in session, be directed to 'addrecipe.html'.
    2. Fill in all details in the form and click 'Add Recipe'.
    3. Be redirected to the homepage. 

9. Edit Recipe
    1. On 'My Recipes', click on 'Edit Recipe' when viewing a recipe card.
    2. Edit any details within the form.
    3. Click on 'Update Recipe' and be redirected to 'home.html'. 

10. Delete Recipe
    1. On 'My Recipes', click on 'Delete Recipe' when viewing a recipe card.
    2. Be redirected to 'My Recipes' and see if the recipe has been deleted from the database. 

11. Return To Homepage
    1. Click on 'Return To Homepage' and be redirected to 'home.html'. 

12. Sign Out
    1. Click on Sign Out and be directed to the message page with options to sign back in or return to homepage. 

### Responsiveness Testing

This application has been tested on all mobile, tablet and desktop screen sizes with the Firefox Mozilla Developer Tools and Google Chrome Developer Tools. From these tests, all issues have been resolved.

### Code Validation

The HTML, CSS and JavaScript code for this application has been run through and validated by The W3C Markup Validation Service and JSHint, with the exception of the validation service seeing the Flask/Jinja markup as errors.

### Bugs

In the 'Edit Recipe' form, the 'Category' and 'Allergens' dropdown list will not have preselected values.

Register functionality bug - this function was missing a key line of code which did not allow the user to successfully register into the application and therefore threw a "Method Not Allowed" Exception. This has been corrected and re-tested.

## Deployment

The source code for this application can be found on [Github](https://github.com/kimpea/the-cookery-cove) and the application itself has been deployed onto [Heroku](https://the-cookery-cove.herokuapp.com/). There is no difference between the GitHub code and the code in the live application. 

It can be installed with the following steps:

 - Download the git repository
 - Sign up/login to Heroku.com
 - From the dashboard click Create New App
 - Enter a unique name and your region and click Create
 - From your command line, enter ```heroku``` to ensure heroku is installed (if not installed this can be done with ```sudo snap install --classic heroku```)
    ```
    heroku login
    ```
 - Enter your credentials for heroku.com
    ```
    sudo pip3 install Flask
    sudo pip3 install pymongo
    sudo pip3 freeze --local > requirements.txt
    echo web: python run.py > Procfile
    git add .
    git commit -m "initial commit"
    git push -u heroku master
    heroku ps:scale web=1
    ```
 - Make sure to set debug to True.
 - From heroku.com app settings: set config vars to IP : 0.0.0.0, PORT : 5000 and MONGO_URI :mongodb://[username]:[password]@ds129914.mlab.com:29914/online_cookbook, ensuring that you update the username and password accordingly.
 - Click More > Restart all Dynos
 - Application is live at https://your-app-name.herokuapp.com/

This application's source code has been modified since the initial deployment - this was to fix a major bug regarding the register functionality, and to also tidy up the indentation of the HTML templates.

## Credits and Acknowledgements

- I would like to credit Stack Overflow for helping me fix all of the minor bugs within the application, and I would also like to credit the Code Institute Data Centric Development lessons.

### Media

- All images used in this application are obtained from [BBC Goodfood](https://www.bbcgoodfood.com/)