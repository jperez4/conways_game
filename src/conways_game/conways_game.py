import tkinter as tk
import threading
import time
import random
import numpy as np

# Global variable definition
N_COLS = 10  # Number of columns of the matrix
N_ROWS = 10  # Number of rows of the matrix

matrix = np.zeros((N_ROWS, N_COLS), dtype=int)

update_matrix_flag = True

def clear_matrix():
    for y in range(n_rows):
        for x in range(n_cols):
            matrix[(y, x)].configure(background='white')

def change_color(square):
    square.config(background="white" if square.cget("background") == "black" else 'black')

def resume_pause_thread():
    global update_matrix_flag
    update_matrix_flag = not update_matrix_flag

def initialize_matrix(n_cols, n_rows):
    """
    Initializes a matrix with the measurements

    Args: 
        n_cols: number of columns of the matrix
        n_rows: number of rows of the matrix
    """
    global matrix
    for y in range(n_rows):
        for x in range(n_cols):
            square = tk.Label(matrix_frame, background="white", width = 5, height = 2, relief = "solid")
            square.bind("<Button-1>", lambda event, square=square:change_color(square))
            square.grid(row = y, column = x)
            matrix[(y, x)] = square

def extract_neighborhood_count(x, y):
    """
    Given the index of the matrix, count the number of neighbors

    Args:
        x: coordinate that represents the x axis
        y: coordinate that represents the y axis

    Return: 
        count: number of neighbors
    """
    count = 0
    count += 1 if matrix[((y - 1) % n_rows, (x - 1) % n_cols)].cget('background') == "black" else 0
    count += 1 if matrix[((y - 1) % n_rows, x % n_cols)].cget('background') == "black" else 0
    count += 1 if matrix[((y - 1) % n_rows, (x + 1) % n_cols)].cget('background') == "black" else 0
    count += 1 if matrix[((y), (x - 1) % n_cols)].cget('background') == "black" else 0
    count += 1 if matrix[((y), (x + 1) % n_cols)].cget('background') == "black" else 0
    count += 1 if matrix[((y + 1) % n_rows, (x - 1) % n_cols)].cget('background') == "black" else 0
    count += 1 if matrix[((y + 1) % n_rows, x % n_cols)].cget('background') == "black" else 0
    count += 1 if matrix[((y + 1) % n_rows, (x + 1) % n_cols)].cget('background') == "black" else 0
    return count

def apply_rules(live, neighborhood_count):
    """
    Applies the 3 rules of the game to any given point
    - If a living square has 2 or 3 living neighbors -> lives
    - If a dead square has 3 living neighbors -> lives
    - Else dies

    Args:
        live: boolean value for living or death
        neighborhood_count: number of neighborhoods

    Return:
        'black' (lives) or 'white' (dies)
    """
    if live and 2 <= neighborhood_count <= 3:
        return 'black'
    elif not live and neighborhood_count == 3:
        return 'black'
    else:
        return 'white'

def main():
    """
    Plays the game
    """
    initialize_matrix(n_rows, n_cols)
    

def update_matrix():
    """
    Updates the matrix following the game rules
    """
    global matrix
    button2.config(state="disabled")
    next_matrix = {}
    # Infinite loop until user stops
    while True:
        if update_matrix_flag:
            # Loop over matrix
            start_time = time.time()
            for y in range(n_rows):
                for x in range(n_cols):
                    print(y,x)
                    # Extract the neighborhood of a pixel
                    count = extract_neighborhood_count(x, y)
                    print(count)
                    # Apply game rules
                    live = True if matrix[(y, x)].cget('background') == 'black' else False
                    print(live)
                    color=apply_rules(live, count)
                    print(color)
                    next_matrix[(y, x)]=color
            for y in range(n_rows):
                for x in range(n_cols):
                    matrix[(y, x)].configure(background=next_matrix[(y, x)])
            end_time = time.time()
            print("Tiempo de ejecución:", end_time - start_time, "segundos")
            time.sleep(0.5)        
            root.update()

def update_thread(): 
    """
    Creates a thread that updates the matrix
    """
    update_thread = threading.Thread(target = update_matrix)
    update_thread.daemon=True
    update_thread.start()


root = tk.Tk()
root.title("Conway's Game of Life")
matrix_frame = tk.Frame(root)
matrix_frame.pack()
button_frame = tk.Frame(root, pady = 10)
button_frame.pack()



# Create buttons
button1 = tk.Button(button_frame, text="Clean", command=clear_matrix, padx=40)
button1.pack(side="left")

button2 = tk.Button(button_frame, text="Start", command=update_thread, padx=40)
button2.pack(side="left")

button3 = tk.Button(button_frame, text="Stop/Resume", command=resume_pause_thread, padx=40)
button3.pack(side="left")

main()

root.mainloop()
