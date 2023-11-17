import tkinter as tk
import random, time

# Board size and speed of the game
GRID_SIZE = 150
CELL_SIZE = 5
SPEED = 100  # miliseconds

# Creates the board
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

# Initialize the board
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        grid[i][j] = random.choice([0, 1])

# Perform a step in the game
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

# Draws the board
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

# Starts the game
def start_game():
    measure_time(next_generation)
    root.after(SPEED, start_game)

# Función para medir el tiempo de ejecución de una función
def measure_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("Execution time:", end_time - start_time, "seconds")


# Creates game window
root = tk.Tk()
root.title("Conway's Game of Life")

# Creates canvas
canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
canvas.pack()

# Button to start the game
start_button = tk.Button(root, text="Start", command=start_game)
start_button.pack()

# Draws the initial board
draw_grid()

root.mainloop()
