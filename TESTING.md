# Eat Me! - Testing

## Validators
- HTML
    - No errors were returned when passing through the official[W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Featmeproject.herokuapp.com%2F)
- CSS 
     - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Featmeproject.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- JavaScript
    - No errors were found when passing through [Jshint](https://jshint.com/)
- Python
    - No errors were found when passing through [PEP8](http://pep8online.com/)

## User Story Testing

### EPIC | Navigation
*As a User I can immediately understand the websites purpose so that I know if its what im looking for.*
- As soon as a user arrives on the home page they are welcomed by a brief message explaining the sites purpose.

*As a User I can navigate around the site so that I can easily view desired content.*
- A navigation bar sits at the top of every page with the current page's link darkened.

*As a User I can view a list of recipes so that I can choose one to read.*
- The all recipes page shows a list of every page on the site.

*As a User I can click on a recipe so that I can read the recipe details.*
- Clicking anywhere inseide a recipes card will take you directly to the recipes page.

*As a User I can search recipes so that I can find specific recipes im looking for.*
- In the top righthand corner of the navigation bar is a search bar.

### EPIC | User's Recipes
*As a User I can create recipes so that other users can view them.*
- Once a user has created an account they can navigate to 'Your Recipes' and from there can add there own recipes. Once created they will appear on the All Recipes page.

*As a User I can view my recipes so that I can see and manage all recipes I have created.*
- All the users created recipes are available to see and manage on the 'Your Recipes' page.

*As a User I can edit recipes so that I can update any changes or mistakes to my recipes.*
- On the 'Your Recipes' page each recipe will have a 'Edit' button which can be used to edit the recipe.

*As a User I can delete recipes so that I can remove any unwanted recipes I have made.*
- On the 'Your Recipes' page each recipe will have a 'Delete' button which can be used to delete the recipe.

*As a User I can view all my liked recipes so that I can return to them with ease.*
- All recipes that the user has liked will appear in the 'Favourite Recipes' page.

### EPIC | User Interaction
*As a User I can like/unlike recipes so that I can mark which recipes I enjoyed.*
- Each recipe has a heart button which can be toggled by signed in users to like/unlike the recipe.

*As a User I can comment on recipes so that I can give my feedback to others.*
- Each recipe has a comment section that can be used by users that are signed in.

*As a User I can view the number of likes on a recipe so that I can see which is most popular.*
- Each recipe has a counter next to the like button which displays the total likes.
- The home page also has a Most Loved section that displays the most liked recipes.

*As a User I can view comments on recipes so that I can read other user's feedback.*
- Every comment left is displayed at the bottom of the recipes page.

### EPIC | Sign in
*As a User I can register for an account so that I can begin to use the services afforded to members.*
- In the navbar is a register link that takes you to the sign up page. 
- There is also a sign up button located on the index page which also takes you to the sign up page.

*As a User I can log in/out so that I can like recipes, comment on recipes and manage my recipes.*
- In the navbar there is a link to log in or log out.

*As a User I can see my login status so that I know if i'm logged in or out.*
- If logged in a message will appear in the navbar stating what account is logged in.

### EPIC | Admin
*As a Admin I can view, create, edit and delete all recipes and comments so that I can control the websites content.*
- Admins have full access to CRUD functionallity for both recipes and comments in the admins page.

*As a Admin I can feature recipes so that I can highlight them on the home page.*
- Admins can select any recipe to be featured form the admins page.

## Feature Testing

## Bugs