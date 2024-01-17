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

## Second approach
After doing the game with lists I was wondering if there was a better solution/implementation (speed). So I researched and I found numpy, so I tried to implement the game using it. 

Futhermore I wanted to show the user an empty board to fill with its own values. So, in the numpy version first it will appear a window with the empty board and then each time the user clicks a square in the canvas, changes its value, and then with the button Start, it starts the game. I was expecting better execution times but the result was even worse than the lists version, I thought that cant be possible, so I started researching.

## Final approach
After some research about numpy and its capabilities I realize i was wrong, I was using it wrong. There is no advantage of using numpy over list if I'm going to use "normal" operations (loop, count, sums). In fact in certain cases, numpy can be slower if the size is small. 

The solution? Vectorial operations. This time instead of looping over each element of the matrix calculating the next step, we do it for all element at the same time. We roll over the axis in the eight possible directions (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)  to calculate the neighbors alining the neighbor cells with the central cell.

"Align the neighbor cells" means that we want to put the neighbot cells in specific position to compare it with the centrall cell in an eficient process.

An example with a centrall cell and its neighbors in a 3x3 matrix:

X X X
X C X
X X X

Where "C" is the centrall cell and X the neighbor cells. If we want to apply the game rules to the centrall cell we need to evaluate the state of its eight neighbors. To do this efficiently we roll the matrix

Up shift: The up neigbor cells "X" aligns with the centrall cell "C"

X C X
X X X
X X X

Down shift: The down neigbor cells "X" aligns with the centrall cell "C"

X X X
X X X
X C X

An so on

np.roll it's a NumPy function that rotates the matrix elements in one or several axis. That can be usefull to perform neighborhood operations.

np.roll(a, shift, axis=None)
a: matrix.
shift: integer value or tuple of integer with the value of positions to shift the elements.
axis: integer or tuple of integer indicating along which axes to shift. 

For example, matrix mat and I want to shift it's elements one position top in the row axis (0)

mat = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

shifted_mat = np.roll(mat, shift=-1, axis=0)

print(shifted_mat)

[[4 5 6]
 [7 8 9]
 [1 2 3]]

In the game, np.roll it's used to perform the neighborhood of each cell shifting the matrix in the eight possible directions, without using loops. 

After calculating the eight possible directions, we sum all the neighborhood matrices. Each cell in the neighbors matrix represent the sum of its eight neigbors

## I made use of/learn
- Random
- Time
- Tkinter (canvas, root.after, root.mainloop, pack)
- Numpy
- List comprehension
- Operators (%)
- Decorators
- Sometimes its faster to access n positions than slicing
- Black formatting
- Mutable vs Inmutable objects