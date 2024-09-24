import numpy as np
import tkinter as tk
import time

GRID_SIZE = 15
CELL_SIZE = 10  # Size in pixels of the rectangle inside the grid
SPEED = 1000  # Miliseconds

# Creates an empty matrix grid size
matrix = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)


def change_canvas_value(row, column, cell):
    """
    Change the value and the color of a cell to the opposite when user clicks it.

    Args:
        row: x-axis index that represents cell position in the grid.
        column: y-axis index that represents cell position in the grid.
        cell: canvas rectangle object to apply the changes.
    """
    if matrix[row, column] == 1:
        matrix[row, column] = 0
        color = "white"
    else:
        matrix[row, column] = 1
        color = "black"
    canvas.itemconfig(cell, fill=color)


def draw_grid():
    """
    Draws the grid based on the grid and cell sizes and the cell value.
    Binds the left click to change cell's value.
    """
    canvas.delete("cell")
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x1 = i * CELL_SIZE
            y1 = j * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            color = "black" if matrix[i, j] == 1 else "white"
            cell = canvas.create_rectangle(
                x1, y1, x2, y2, fill=color, tags="cell", outline="grey"
            )
            canvas.tag_bind(
                cell,
                "<Button-1>",
                lambda event, cell=cell, row=i, col=j: change_canvas_value(
                    row, col, cell
                ),
            )


def next_generation():
    """
    Performs the next step in the game's matrix
    """
    neighbors = (
        np.roll(matrix, (-1, -1), axis=(0, 1))
        + np.roll(matrix, (-1, 0), axis=(0, 1))
        + np.roll(matrix, (-1, 1), axis=(0, 1))
        + np.roll(matrix, (0, -1), axis=(0, 1))
        + np.roll(matrix, (0, 1), axis=(0, 1))
        + np.roll(matrix, (1, -1), axis=(0, 1))
        + np.roll(matrix, (1, 0), axis=(0, 1))
        + np.roll(matrix, (1, 1), axis=(0, 1))
    )

    # Applies the games rules for the dying of the cells
    # np.where(condition, true value, false value)
    new_matrix = np.where(
        (matrix == 1) & ((neighbors < 2) | (neighbors > 3)), 0, matrix
    )
    # Applies the games rules for the new living cells
    new_matrix = np.where((matrix == 0) & (neighbors == 3), 1, new_matrix)

    matrix[:] = new_matrix
    draw_grid()


def draw_grid():
    """
    Draws the game's grid in tkinter.
    Creates a rectangle for each cell of the matrix and assigns a color depending on whether the cell is
    alive or dead. It also links the click event with the change_canvas_value function for each cell.
    """
    canvas.delete("cell")
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x1 = i * CELL_SIZE
            y1 = j * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            color = "black" if matrix[i, j] == 1 else "white"
            cell = canvas.create_rectangle(
                x1, y1, x2, y2, fill=color, tags="cell", outline="grey"
            )
            canvas.tag_bind(
                cell,
                "<Button-1>",
                lambda event, cell=cell, row=i, col=j: change_canvas_value(
                    row, col, cell
                ),
            )


def start_game():
    """
    This function starts the game.
    It calls to the next_generation function to update the game state and it configure
    itself to be called again after a certain time determined by SPEED variable.
    """
    # measure_time(next_generation)
    root.after(SPEED, start_game)


def measure_time(func):
    """
    This function measures the execution time of a function.
    Used to measure the execution time of each step of the game.
    """
    start_time = time.time()
    func()
    end_time = time.time()
    print("Execution time:", end_time - start_time, "seconds")


# Creates the game window
root = tk.Tk()
root.title("Conway's Game of Life")

# Create the canvas to draw the grid
canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
canvas.pack()

# Start button
start_button = tk.Button(root, text="Start", command=start_game)
start_button.pack(fill="x")

# Draw initial grid
draw_grid()

root.mainloop()
