import tkinter as tk
import numpy as np
import time

# Global variable definition
N_COLS = 15  # Number of columns of the matrix
N_ROWS = 15  # Number of rows of the matrix
CELL_SIZE = 5

matrix = np.zeros((N_ROWS, N_COLS), dtype=int)


def change_canvas_value(row, column, cell):
    if matrix[row, column] == 1:
        matrix[row, column] = 0
        color = "white"
    else:
        matrix[row, column] = 1
        color = "black"
    canvas.itemconfig(cell, fill=color)


def draw_grid():
    canvas.delete("cell")
    for i in range(N_ROWS):
        for j in range(N_COLS):
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


def play():
    measure_time(calculate_step)
    root.after(1000, play)


def measure_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("Execution time:", end_time - start_time, "seconds")


def calculate_step():
    global matrix
    next_matrix = np.zeros((N_ROWS, N_COLS), dtype=int)
    for i in range(N_ROWS):
        for j in range(N_COLS):
            neighbors = [
                matrix[i - 1, j - 1],
                matrix[i - 1, j],
                matrix[i - 1, (j + 1) % N_COLS],
                matrix[i, j - 1],
                matrix[i, (j + 1) % N_COLS],
                matrix[(i + 1) % N_ROWS, j - 1],
                matrix[(i + 1) % N_ROWS, j],
                matrix[(i + 1) % N_ROWS, (j + 1) % N_COLS],
            ]
            living_neighbors = sum(neighbors)
            # Apply rules
            if matrix[i, j] == 1:  # Actual cell is live
                if living_neighbors < 2 or living_neighbors > 3:
                    next_matrix[i, j] = 0  # Dies
                else:
                    next_matrix[i, j] = 1  # Lives
            else:
                if living_neighbors == 3:
                    next_matrix[i, j] = 1  # Lives
    matrix = next_matrix
    draw_grid()


# Creates game window
root = tk.Tk()
root.title("Conway's Game of Life")

# Creates the canvas
canvas = tk.Canvas(root, width=N_COLS * CELL_SIZE, height=N_COLS * CELL_SIZE)
canvas.pack()

button2 = tk.Button(root, text="Start", command=play)
button2.pack(fill="x")

draw_grid()

root.mainloop()
