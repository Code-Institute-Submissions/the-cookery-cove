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

