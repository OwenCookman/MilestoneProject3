## Testing
**Testing was carried out on a desktop computer**

Below are the different ways in which I tested this project.

- The CSS code was validated using the [**W3C Markup Validation Service**](https://validator.w3.org/) website

### User Stories Tested

#### User who would like to read reviews to see if they like the sound of a movie
As someone who enjoys watching movies, I would like to search for a movie that I have heard of, read something about it and also read what other people who have already watched it think.

- The Home Page gives a quick explenation of what the website is used for and how to use it
- searching for a movie returns that movie and any related titles
- selecting a movie opens a page with information about the movie
- underneath the movies information are reviews left by other users

#### User who has watched a movie and would like to give their opinion of that movie
As someone who has recently watched a movie, I would like to leave a review of that movie so that others can make an informed choice as the weather they want to watch it or not.

- The Home Page gives a quick explenation of what the website is used for and how to use it
- searching for a movie returns that movie and any related titles
- selecting a movie opens a page with information about the movie
- underneath the movies information is a button labeled Review and reviews left by other users
- Pressing the Review button opens a page with a form on it to give a username, comments and score for the movie
- Returning to the movies page displays other users reviews and the one just entered
- selecting edit review will allow the review to be edited
- selecting delete review will remove the review

#### User who would like to know more details about a movie
As someone who enjoys watching movies, I would like to know more details about a particular movie such as who it was directed by.

- The Home Page gives a quick explenation of what the website is used for and how to use it
- searching for a movie returns that movie and any related titles
- selecting a movie opens a page with information about the movie
- Below the movie poster is information about the movie such as the run time, its rating, the director(s) and writer(s)

### Manual Testing

#### Navbar

- Open the page in a new browser window
- right click and select inspect
- select toggle device toolbar or press Ctrl+shift+M
- set the device to responsive
- move the slider in and out to see that the Navbar changes to have a burger icon at 991px
- press the home button to see that the page reloads on to index.html
- press the title "MOVIESTORE" to see that the page reloads on to index.html

#### Search Bar

- Open the page in a new browser window
- select the search bar
- type in a move title (for example: Star Wars)
- select the button labelled Search or press enter
- see that a list of movies relating to the search has been rendered on to the page

#### Movie Information

- Open the page in a new browser window
- select the search bar
- type in a move title (for example: Star Wars)
- select the button labelled Search or press enter
- see that a list of movies relating to the search has been rendered on to the page
- select the movie you were looking for
- see that the movies poster has been rendered in the centre of the page and information about the movie has been rendered underneath

#### Reviews
- Open the page in a new browser window
- select the search bar
- type in a move title (for example: Star Wars)
- select the button labelled Search or press enter
- see that a list of movies relating to the search has been rendered on to the page
- select the movie you were looking for
- see that the movies poster has been rendered in the centre of the page and information about the movie has been rendered underneath
- see that below the information and below the Review button Reviews have rendered (if movie has been reviewed)

#### Submitting Reviews
- Open the page in a new browser window
- select the search bar
- type in a move title (for example: Star Wars)
- select the button labelled Search or press enter
- see that a list of movies relating to the search has been rendered on to the page
- select the movie you were looking for
- scroll down to just below the movie information
- select the Review button
- see that a form has been rendered
- fill in the username, comments and score boxes
- see that putting in a number below 1 and above 5 display a message when attempting to submit
- submit the correctly filled out form
- return to the movies page to see the review rendered

#### Editing Reviews
- Open the page in a new browser window
- select the search bar
- type in a move title (for example: Star Wars)
- select the button labelled Search or press enter
- see that a list of movies relating to the search has been rendered on to the page
- select the movie you were looking for
- scroll down to just below the movie information
- find the review you wish to edit and press the Edit button
- see that a form has been rendered
- fill in the username, comments and score boxes
- see that putting in a number below 1 and above 5 display a message when attempting to submit
- submit the correctly filled out form
- return to the movies page to see the review has been replaced

#### Deleting Reviews
- Open the page in a new browser window
- select the search bar
- type in a move title (for example: Star Wars)
- select the button labelled Search or press enter
- see that a list of movies relating to the search has been rendered on to the page
- select the movie you were looking for
- scroll down to just below the movie information
- find the review you wish to delete and press the Delete button
- return to the movies page to see the review has been Deleted

### Code Validation

- The **HTML** code was validated using [**W3C Markup Validation**](https://validator.w3.org/)
- The **CSS** code was validated using [**W3C CSS Validation**](https://jigsaw.w3.org/css-validator/)

### Further Testing

The page was shared with family and friends to gather any feedback on any issues found

While setting up the required files to deploy the application on Heroku the CLI generated Procfile didn't format properly and caused issues, this is a known issue with Windows and was fixed by creating another procfile and copying the content of the CLI generated one over.