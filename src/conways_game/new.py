import tkinter as tk
import numpy as np
import time

# Global variable definition
N_COLS = 250  # Number of columns of the matrix
N_ROWS = 250  # Number of rows of the matrix
CELL_SIZE = 5

matrix = np.random.randint(2, size=(N_ROWS, N_COLS))
# np.zeros((N_ROWS, N_COLS), dtype=int)





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
            cell = canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="cell", outline="grey")
            canvas.tag_bind(
                cell,
                "<Button-1>",
                lambda event, cell=cell, row=i, col=j: change_canvas_value(
                    row, col, cell
                )
            )


def play():
    measure_time(calculate_step)
    input()
    root.after(1000, play)

def measure_time(func):
    # meanlist=[]
    # for i in range(1000):
    start_time = time.time()
    func()
    end_time = time.time()
        # meanlist.append(end_time - start_time)
    print("Tiempo de ejecución:", end_time - start_time,
        #   np.mean(meanlist), 
          "segundos")

def calculate_step():
    global matrix
    next_matrix = np.zeros((N_ROWS, N_COLS), dtype=int)
    # Calculate the sum of its neighbors TODO: Es mas rapido acceder a 5 posiciones que usar slicing en la matriz
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
                matrix[(i + 1) % N_ROWS, (j + 1) % N_COLS]
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
    
    

def direct_check():
    sum([matrix[-1, -1], matrix[-1, 0], matrix[-1, 1], matrix[0, -1], matrix[0, 1], matrix[1, -1], matrix[1, 0], matrix[1, 1]])
def other():
    sum(matrix[:3, [-1, 0, 1]])  

def count1():
    [matrix[-1, -1], matrix[-1, 0], matrix[-1, 1], matrix[0, -1], matrix[0, 1], matrix[1, -1], matrix[1, 0], matrix[1, 1]].count(1)
def count2():
    np.count_nonzero([matrix[-1, -1], matrix[-1, 0], matrix[-1, 1], matrix[0, -1], matrix[0, 1], matrix[1, -1], matrix[1, 0], matrix[1, 1]] == 1)

# measure_time(direct_check)
# measure_time(count1)
# measure_time(count2)
# Dibujar el tablero inicial
# draw_grid()
# root.after(1000, draw_grid)
# 

# Crear la ventana de juego
root = tk.Tk()
root.title("Conway's Game of Life")
# Crear el lienzo para dibujar el tablero
canvas = tk.Canvas(root, width=N_COLS * CELL_SIZE, height=N_COLS * CELL_SIZE)
canvas.pack()
button1 = tk.Button(root, text="Clean", command=lambda: matrix.fill(0))
button1.pack(fill="x")

button2 = tk.Button(root, text="Start", command=play)
button2.pack(fill="x")

button3 = tk.Button(root, text="Stop/Resume", command=None)
button3.pack(fill="x")

draw_grid()

root.mainloop()