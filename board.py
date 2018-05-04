import tkinter as tk
import random

class menuItems(object):
    def __init__(self):
        menubar = Menu(app)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New...", command=self.new)
        filemenu.add_command(label="Open...", command=self.open)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=app.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        app.config(menu=menubar)

    def new(self):
        pass

    def open(self):
        pass

    def save(self):
        print("You have saved the file")





# Set number of rows and columns
ROWS = 16
COLS = 16

# Create a grid of None to store the references to the tiles
tiles = [[None for _ in range(COLS)] for _ in range(ROWS)]
values = [[0 for _ in range(COLS)] for _ in range(ROWS)]


def create_board():
    c.pack()
    app.update_idletasks()
    # gets unit widths for columns and rows
    col_width = c.winfo_width()/COLS
    row_height = c.winfo_height()/ROWS
    # create 40 mines (about 1/6 of ROW*COL)

    def generate_mine():
        a = random.randint(0, ROWS-1)
        b = random.randint(0, COLS-1)
        if values[a][b] == 0:
            values[a][b] = -1
            return
        else:
            generate_mine()

    for _ in range(40):
        generate_mine()

    # creates numbers
    def count_surrounding():
        sum = 0
        for r in range(ROWS):
            for c in range(COLS):
                if values[r][c] == -1:
                    continue
                if r-1 < 0:
                    # top right corner
                    if c+1 > COLS-1:
                        if values[r+1][c-1] == -1 : sum += 1
                        if values[r][c-1] == -1 : sum += 1  # left
                        if values[r+1][c] == -1 : sum += 1  # bottom
                    # top left corner
                    elif c-1 < 0:
                        if values[r+1][c] == -1 : sum += 1  # bottom
                        if values[r+1][c+1] == -1 : sum += 1  # bottom right
                        if values[r][c+1] == -1 : sum += 1  # right

                    # top most row
                    else:
                        if values[r+1][c+1] == -1 : sum += 1  # bottom right
                        if values[r+1][c] == -1 : sum += 1  # bottom
                        if values[r+1][c-1] == -1 : sum += 1  # bottom left
                        if values[r][c-1] == -1 : sum += 1  # left
                        if values[r][c+1] == -1 : sum += 1  # right

                elif r+1 > ROWS-1:
                    # bottom right corner
                    if c+1 > COLS-1:
                        if values[r][c-1] == -1 : sum += 1  # left
                        if values[r-1][c-1] == -1 : sum += 1  # top left
                        if values[r-1][c] == -1 : sum += 1  # up
                    # bottom left corner
                    elif c-1 < 0:
                        if values[r-1][c] == -1 : sum += 1  # up
                        if values[r-1][c+1] == -1 : sum += 1  # top right
                        if values[r][c+1] == -1 : sum += 1  # right
                    # bottom most row
                    else:
                        if values[r-1][c] == -1 : sum += 1 # up
                        if values[r-1][c+1] == -1 : sum+= 1# top right
                        if values[r][c-1] == -1 : sum+= 1 # left
                        if values[r-1][c-1] == -1 : sum+= 1 # top left
                        if values[r][c+1] == -1 : sum+= 1 # right
                # left column
                elif c-1 < 0 and r-1 >= 0 and r+1<=ROWS-1:
                    if values[r-1][c] == -1 : sum += 1 # up
                    if values[r-1][c+1] == -1 : sum+= 1# top right
                    if values[r][c+1] == -1 : sum+= 1 # right
                    if values[r+1][c+1] == -1 : sum += 1  # bottom right
                    if values[r+1][c] == -1 : sum += 1  # bottom
                # right column
                elif c+1 > COLS-1 and r-1 >= 0 and r+1<=ROWS-1:
                    if values[r+1][c] == -1 : sum += 1  # bottom
                    if values[r-1][c] == -1 : sum += 1 # up
                    if values[r][c-1] == -1 : sum+= 1 # left
                    if values[r-1][c-1] == -1 : sum+= 1 # top left
                    if values[r+1][c-1] == -1 : sum += 1  # bottom left
                # everything else
                else:
                    print(r, c)
                    if values[r+1][c] == -1 : sum += 1  # bottom
                    if values[r-1][c] == -1 : sum += 1 # up
                    if values[r][c-1] == -1 : sum+= 1 # left
                    if values[r-1][c-1] == -1 : sum+= 1 # top left
                    if values[r+1][c-1] == -1 : sum += 1  # bottom left
                    if values[r-1][c+1] == -1 : sum+= 1# top right
                    if values[r][c+1] == -1 : sum+= 1 # right
                    if values[r+1][c+1] == -1 : sum += 1  # bottom right

            values[r][c] = sum
            sum = 0
    count_surrounding()
    print(values)

    # creates all untouched squares on canvas
    for i in range(ROWS):
        for j in range(COLS):
            c.create_rectangle(j*col_width, i*row_height, (j+1)*col_width, (i+1)*row_height, fill="grey", outline='black')

def callback(event):
    # Get rectangle diameters
    col_width = c.winfo_width()/COLS
    row_height = c.winfo_height()/ROWS
    # Calculate column and row number
    col = int(event.x//col_width)
    row = int(event.y//row_height)
    #print(col, row)
    # If the tile is not filled, create a rectangle
    if not tiles[row][col]:
        c.delete(tiles[row][col])
        tiles[row][col] = c.create_rectangle(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="white")
        tiles[row][col] = c.create_text(col*col_width + col_width/2, row*row_height + row_height/2, text=values[row][col])

    # If the tile is filled, delete the rectangle and clear the reference

    # else:
    #     c.delete(tiles[row][col])
    #     tiles[row][col] = None

# Create the window, a canvas and the mouse click event binding
global app, menu
app = tk.Tk()
app.title("Python Minesweeper")
c = tk.Canvas(app, width=750, height=750, borderwidth=5, background='white')
c.pack()
app.update_idletasks()

create_board()

#menu = menuItems()
c.bind("<Button-1>", callback)

app.mainloop()
