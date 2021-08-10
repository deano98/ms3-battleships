# Milestone Project 3 - Battleships Game

This python based project will be a simple version of the popular battleships boardgame.

The game will be for 2 players. Each player will have to place 5 battleships on their own 5x5 board, the position of each players ships are stored. The players will then take it in turns to guess the locations of each ship, a correct guess will "sink" said ship. Once a player has sunk all of the opposing ships, they win.

As this is primarily a back end project, it will be a simple game in terms of the UX. The board and ships will be stored in the memory rather than displayed, and the only user input will be the player's names and ship locations.

# UX

### User Stories

* As a user, I want the game to be intuative and easy to use
* As a user, I'd like to be able to see the rules of the game
* As a user, I want the game to be interactive and engaging 

# Flowchart

[Flowchart]()

# Features

* The game will first ask each player their name, which will be stored in variables.
* Once both player's names have been entered, the 5x5 boards will be created and stored in variables.
* Each player will then take it in turns to select 5 coordinates to place their ships on their 5x5 boards. The x axis will be labelled A-E and the y axis 1-5, so the required format for the coordinates will be something like A5. If the correct format is not used this will trigger an error and the player will have to re-enter in the correct format.
* When a player enters a correct coordinate, this will modify the board variables to store the location of each ship.
* Once each player has placed 5 ships, the game will begin. Once again each player will have to input valid coordinates to guess the locations of the opposing ships.
* When a coordinate is entered, the board variables are checked to see if the attempt was successful, if it was the variable is modified to store the hit.
* Any successful hits will trigger a check to see if any ships are still remaining, if there are the game will continue. If not, the game will end and the player will be declared the winner.

# Technologies Used

* Python

# Testing