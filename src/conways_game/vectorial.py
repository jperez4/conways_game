import numpy as np
import tkinter as tk
import random, time

# Tamaño de la cuadrícula y velocidad del juego
GRID_SIZE = 150
CELL_SIZE = 5
SPEED = 100  # milisegundos

# Crear una matriz para el tablero
grid = np.random.randint(2, size=(GRID_SIZE, GRID_SIZE), dtype=int)

# Función para calcular el siguiente estado del juego
def next_generation():
    neighbors = (
        np.roll(grid, (-1, -1), axis=(0, 1)) + np.roll(grid, (-1, 0), axis=(0, 1)) +
        np.roll(grid, (-1, 1), axis=(0, 1)) + np.roll(grid, (0, -1), axis=(0, 1)) +
        np.roll(grid, (0, 1), axis=(0, 1)) + np.roll(grid, (1, -1), axis=(0, 1)) +
        np.roll(grid, (1, 0), axis=(0, 1)) + np.roll(grid, (1, 1), axis=(0, 1))
    )

    new_grid = np.where((grid == 1) & ((neighbors < 2) | (neighbors > 3)), 0, grid)
    new_grid = np.where((grid == 0) & (neighbors == 3), 1, new_grid)

    grid[:] = new_grid
    draw_grid()

# Función para dibujar el tablero
def draw_grid():
    canvas.delete("cell")
    live_cells = np.argwhere(grid == 1)
    for i, j in live_cells:
        x1 = i * CELL_SIZE
        y1 = j * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill="black", tags="cell")

# Función para iniciar el juego
def start_game():
    measure_time(next_generation)
    input()
    root.after(SPEED, start_game)

# Función para medir el tiempo de ejecución de una función
def measure_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("Tiempo de ejecución:", end_time - start_time, "segundos")

# Crear la ventana de juego
root = tk.Tk()
root.title("Conway's Game of Life")

# Crear el lienzo para dibujar el tablero
canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
canvas.pack()

# Botón de inicio
start_button = tk.Button(root, text="Start", command=start_game)
start_button.pack()

# Dibujar el tablero inicial
draw_grid()

root.mainloop()
