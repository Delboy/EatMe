# Eat Me!

Here is a link to the live project. (https://eatmeproject.herokuapp.com/)

Eat me! is a website where users come together to share their favourite created recipes. It is built using the Django Framework in python. 

## User Experience (UX)

A visitor to Eat Me! would be someone who is most likely an adult who is looking to either find new recipes or to share their own creations. 

## User Stories 

A list of my user stories and their tasks can be found [here](https://github.com/delboy/eatme!/issues).

### EPIC | Navigation
- As a User I can immediately understand the websites purpose so that I know if its what im looking for.
- As a User I can navigate around the site so that I can easily view desired content.
- As a User I can view a list of recipes so that I can choose one to read.
- As a User I can click on a recipe so that I can read the recipe details.
- As a User I can search recipes so that I can find specific recipes im looking for.

### EPIC | User's Recipes
- As a User I can create recipes so that other users can view them
- As a User I can view my recipes so that I can see and manage all recipes I have created.
- As a User I can edit recipes so that I can update any changes or mistakes to my recipes.
- As a User I can delete recipes so that I can remove any unwanted recipes I have made.
- As a User I can view all my liked recipes so that I can return to them with e- ase.

### EPIC | User Interaction
- As a User I can like/unlike recipes so that I can mark which recipes I enjoyed.
- As a User I can comment on recipes so that I can give my feedback to others.
- As a User I can view the number of likes on a recipe so that I can see which is most popular.
- As a User I can view comments on recipesso that I can read other user's feedback.

### EPIC | Sign in
- As a User I can register for an account so that I can begin to use the services afforded to members.
- As a User I can log in/out so that I can like recipes, comment on recipes and manage my recipes.
- As a User I can see my login status so that I know if i'm logged in or out.

### EPIC | Admin
- As a Admin I can view, create, edit and delete all recipes and comments so that I can control the websites content.
- As a Admin I can feature recipes so that I can highlight them on the home page.

## Design

### Colour Scheme
- I want to keep the colour scheme simple so will be sticking with black, white and different shades of grey. This is because the uploaded pictures from users could be any host of colours, so by keeping the colour scheme simple the site minimises the risk of clashing with any images, keeping them the main focus of the user.
### Typography
- On the site I will be using the default bootstrap fonts as I find them clean, elegant and easy to read so feel they will fit in with the sites theme nicely. The only font used on the site will be Imbue which is soley used to style the logo.
### Imagery
- All the imagery will be food related with only 4 images being static. The rest will be uploaded by various users.
### Wireframes

Wireframes for each page are linked here:

* [Home Page](assets/documents/home_page.pdf)
* [All Recipes](assets/documents/all_recipes.pdf)
* [Detailed Recipe](assets/documents/detailed_recipe.pdf)
* [Your Recipes](assets/documents/your_recipes.pdf)
* [Favourite Recipes](assets/documents/favourite_recipes.pdf)
* [Searched Recipes](assets/documents/searched_recipes.pdf)
* [Add Recipe](assets/documents/add_recipe.pdf)
* [Register, log in/out](assets/documents/register_log_in_out.pdf)


### Database Schema 

![Database Schemas can be found here](assets/images/eat-me-schema.png)
*<i>note</i> - I forgot to add a Body section to the Comment table when designing. By the time I realised that I left it out my trial period for the schema creator website had expired so could not rectify the mistake.

## Features

### Home Page

- #### Navigation bar
    - The navigation bar is present at the top of every page and houses all links to the various other pages.
    - The active page will be shown to have a bolder font helping users understand what page they're on.
    - Hovering over the links will darken the font.
    - The options to Register or Log in will change to the option to log out once a user has logged in. 
    - Once a user has signed in more options such as 'Your Recipes' and 'Favourite Recipes' become available.
    - Text will also appear in the bar stating which user is signed in if any.
    - A search bar is nested in the navbar to find recipes quickly.
    - The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes to small. 

- #### Hero Image
    - The hero image welcomes the user with a short message advertising what the sites about.
    - A button to sign up and a short message is present in the image. Clicking this takes you to the register an account page.
    - If a user is already signed the message changed to 'welcome back' and the sign up button changes to a 'view recipes' button, which takes you to the all recipes page. 

- #### Carousel
    - The carousel displays any recipes that the admin has selected to be featured.
    - Clicking the image will take you to that recipe's detail page.
    - Buttons on the edge if the carrousel scroll through all the featured recipes.

- #### Most Loved Recipes
    - The most loved recipes section displays the top 5 recipes with the most likes.
    - Clicking each recipe takes you to its detail page.
    - A link to all recipes can be found at the bottom of the list.

- #### Features
    - This section displays a couple short messages with images to showcase the sites basic features.

- #### Footer
    - The footer rests at the bottom of each page and has links to all socail media accounts.
    - Clicking the links in the footer opens a seperate browser to avoid pulling the user away from the site.


### All Recipes Page

- #### Recipe Cards
    - The site will paginate all recipe cards to display 6 to a page.
    - Each card will display the recipes image, Title, Author, Description, Published date and how many likes it has recieved.
    - If the recipe is vegetarian or vegan a small green corosponding label will be present in the bottom left corner.
    - Clicking anywhere inside the recipes card will take you directly to that recipes detail page.

### Favourite Recipes Page

- #### Favourite Recipes
    - This page shows only recipes that the user has liked.
    - If a user tries to access this page without being signed in they will recieve a not logged in error.

### Your Recipes Page

- #### Your Recipes
    - This page displays only the recipes that the user has created. 
    - At the top of the page is an 'Add Recipe' button which takes the user to the add recipe page.
    - Each recipe will have two buttons, an edit and a delete button.
    - The edit button will take users to the edit recipe page for that particular recipe.
    - Clicking the delete button will bring up a modal which asks the user if they are sure they want to delete that particular recipe.
    - If a user tries to access this page without being signed in they will recieve a not logged in error. 

### Searched Recipes Page

- #### Searched Recipes
    - Anything entered into the search bar in the navigation bar displays results here.
    - If the word vegetarian, or vegan is entered into the search bar it will result in all vegetarian or vegan recipes and not just ones with those words in the title. 

### Recipe Deatail Page

- #### Recipe Card
    - At the top of the page the recipe card will show the image, title, author, published date and any dietry information.

- #### Main Section
    - The main body of the page consists of the decription, ingredients, and method. These combined is what creates the whole recipe.
    - At the bottom of the section is an icon and counter for both likes and comments.
    - Clicking the outlined heart renders the recipe 'liked' by the user which will fill in the heart, add 1 to the counter, and add the recipe to the users favourite recipes page.
    - Alternatively, clicking a filled in heart renders the recipe 'unliked' which will change the heart back to an outline, reduce the counter by 1 and remove the recipe from the users favourite recipe page.

- #### Comments
    - At the bottom of the page is the comment section. Here you can view all comments left users.
    - Only signed in users can leave a comment.
    - Comments with profanity automatically fail and will not upload.
    - Any comments left by the user that is currently signed in can be edited or deleted.  

### Add Recipe Page

- #### Adding Recipes
    - The adding recipe page is where users upload thier creations.
    - Each recipe is uploaded by filling out a form.
    - Failing to fill out either the recipes Title, Description, Ingredients, or Method results in the form failing and rendering a message stating which fields you have missed.
    - The form has two checkbox's that toggle wether the recipe is suitable for vegetarians or vegans. 
    - Clicking the vegan checkbox automatically checks the vegetarian checkbox and subsequently unchcecking the vegetarian box unchecks the vegan box.
    - The user has two options to upload an image of their recipe. They can either choose a file to upload or simply put in the URL address of the image. 
    - If neither of the image options are used a default image will be generated.
    - An add Recipe button is present at the bottom of the page once the form is ready to send.
    - If a user tries to access this page without being signed in they will recieve a not logged in error.  

### Edit Recipe Page

- #### Editing Recipes
    - Editing a recipe brings up the form that was filled in when the recipe was created and has all the fields filled out with the orginal content.
    - Changing the content and hitting save at the bottom of the page saves the recipe.
    - If a user tries to access this page without being signed in they will recieve a forbidden access error.