# Conways Game of Life
This project serves the purpose of learning python and putting into action all the ideas i had and to document all the experiencies I have learned along the way. I'll try to update the project as soon as i learn something new that involves improvement over my code or related.

## First approach
The main idea was to use a list of list to represent the board of the game. Each list inside the father list would have n (board size) values between 0 and 1 to represent the state of the cell.(death or live). Each list represents a row in the matrix of the board.

I just had to initialize a matrix with values between 0 and 1 (I learned about list comprehensions) and apply the 3 rules of the game.
- If a living cell has 2 or 3 living neighbors -> lives
- If a dead cell has 3 living neighbors -> lives
- Else dies

This raised the question of how to loop over the matrix to compute the neighborhood of a cell. I tried to use slicing to form a 3x3 submatrix with rows [x - 1, x, x + 1] given a cell in a position (x,y) but -1 index in slicing gets the last element (ops!).

Anyway, I only had to get 5 elements of the matrix to get the neighborhood so accessing 5 elements was faster than trying to calculate a submatrix.

Then I had problems trying several pattern, specifically when the cells were close to the edges so I realiced after several hours that I needed to cycle the board using the % operator.

The other problem I faced was that I couldn't perform the rules on each iteration of the matrix, because this would affect the sucesive elements. So I had to create a new list but I needed several hours to learn about assignments on mutable objects the hard way, so I used the copy method.

Then why not make it graphical? 
So I read about tkinter and I was curious enough to try. It has several interface elements and I  tried a bunch of them until I decided to use a canvas to represent the board and button to start the game.

The most important part here is learn how to pack (literally) elements in tkinter and how to create the canvas blocks using rectangles with a given size in units. Then how to create the root element that contains all the other tkinter objects and handle it making use of the method after to execute each step of the game and refresh the interface.

Finally I made use of decorators to tried to calculate the performance of each step of the game, giving me a mean of 0.05247926712036133

Implementation of Conways's Game of Life

## Installation

To install with pip on macOS or Linux, run:

    python3 -m pip install conways_game

To install with pip on Windows, run:

    py -m pip install conways_game

## Quickstart Guide

TODO - fill this in later

## Contribute

If you'd like to contribute to Conways Game of Life, check out https://github.com/jperez4/conways_game


