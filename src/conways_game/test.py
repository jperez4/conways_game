import tkinter as tk
import random, time

# Tamaño de la cuadrícula y velocidad del juego
GRID_SIZE = 250
CELL_SIZE = 5
SPEED = 100  # milisegundos

# Crear una matriz para el tablero
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

# Inicializar el tablero con células vivas aleatorias
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        grid[i][j] = random.choice([0, 1])

# Función para calcular el siguiente estado del juego
def next_generation():
    new_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            neighbors = [
                grid[(i - 1) % GRID_SIZE][(j - 1) % GRID_SIZE],
                grid[(i - 1) % GRID_SIZE][j],
                grid[(i - 1) % GRID_SIZE][(j + 1) % GRID_SIZE],
                grid[i][(j - 1) % GRID_SIZE],
                grid[i][(j + 1) % GRID_SIZE],
                grid[(i + 1) % GRID_SIZE][(j - 1) % GRID_SIZE],
                grid[(i + 1) % GRID_SIZE][j],
                grid[(i + 1) % GRID_SIZE][(j + 1) % GRID_SIZE],
            ]
            live_neighbors = sum(neighbors)
            if grid[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if live_neighbors == 3:
                    new_grid[i][j] = 1

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            grid[i][j] = new_grid[i][j]

    draw_grid()

# Función para dibujar el tablero
def draw_grid():
    canvas.delete("cell")
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 1:
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
