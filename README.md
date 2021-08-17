# Milestone Project 3 - Battleships Game

This python based project will be a simple version of the popular battleships boardgame.

The game will be for 2 players. Each player will have to place 5 battleships on their own 5x5 board, the position of each players ships are stored. The players will then take it in turns to guess the locations of each ship, a correct guess will "sink" said ship. Once a player has sunk all of the opposing ships, they win.

As this is purely a backend python project, there is no visual aspect to the game. Each players board will also be visible to the other so it wont be usable as a competitive game. It is only to show off my code for the project

# UX

### User Stories

* As a user, I want the game to be intuative and easy to use
* As a user, I'd like to be able to see the rules of the game
* As a user, I want the game to be interactive and engaging 

* Again, as this is purely a backend project, the UX is very limited. But I have tried to build the game with these goals in mind.

# Flowchart

[Flowchart](docs/flowchart/flow-chart.PNG)

# Features

* The game will start by creating each players 5x5 board, storing them in variables
* Following this the game will ask each player their name, which will be stored in variables.
* Each player will then take it in turns to select 5 coordinates to place their ships on their 5x5 boards. The x axis will be labelled A-E and the y axis 1-5, so the required format for the coordinates will be something like A5. If the correct format is not used this will trigger an error and the player will have to re-enter in the correct format.
* When a player enters a correct coordinate, this will modify the board variables to store the location of each ship.
* Once each player has placed 5 ships, the game will begin. Once again each player will have to input valid coordinates, this time to guess the locations of the opposing ships.
* When a coordinate is entered, the coordinates are validated, then the board is checked to see if that square had already been guessed previously
* If the coordinates are valid and the guess isn't a dupluicate, the board variable is checked to see if the attempt was successful, if it was the variable is modified to store the hit.
* Any successful hits will trigger a check to see if any ships are still remaining, if there are the game will continue. If not, the game will end and the player will be declared the winner.

# Technologies Used

* Python

# Testing

### Code Validation

[PEP8 Online Check](http://pep8online.com/)

### Testing User Stories

1. As a user, I want the game to be intuative and easy to use
  * The game is very simple, only requiring a few inputs. All of which you are guided through thoroughly.
2. As a user, I'd like to be able to see the rules of the game
  * As this is a backend project, displaying all of the rules would make the game very cluttered. Instead you are guided through each step.
3. As a user, I want the game to be interactive and engaging
  * If the boards weren't visible to each player and there was an aspect of competition. I believe the game would provide an interactive and engaging experience.

### Testing for Bugs

* I have extensively tested each aspect of the game searching for bugs
* On both Gitpod and Heroku, I have played through the game several times, entering a wide range of valid and invalid inputs.
* My stress testing yielded no bugs, the game runs as expected.

# Deployment

 * Heroku
   * Navigate to the apps page on Heroku
   * Click new > Create app
   * Enter a unique name for your app and choose your region
   * Click create app
   * Navigate to the Settings tab
   * Click on Add buildpack
   * Select python, then save changes
   * Add another buildpack, nodejs and save changes
   * Make sure python is above nodejs on your buildpack list, drag them into the correct order if not
   * Navigate to the Deploy tab
   * Click on Connect to GitHub in the  deployment method section
   * Enter your projects repository name in the Connect to GitHub section, then click search.
   * When your repository is displayed, click connect
   * If you wish for your deployed app to be rebuilt each time you push a new change, click Enable Automatic Deploys
   * If you wish to deply manually, click Deploy Branch
   * Once your app has finished building, it is then deployed on Heroku.

# External Resources

* [w3schools](https://www.w3schools.com/) For help with code issues
* [Stack Overflow](https://stackoverflow.com/) For help with code issues
* [Python Tutor](http://pythontutor.com/index.html) To help debug code

 # Credits

 * Thanks to my mentor Rohit Sharma, for the support with my project.
 * Thanks to everyone on Slack for just being a great source of help and information.

   