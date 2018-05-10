import tkinter as tk
import random
import emoji
from PIL import Image, ImageTk

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
ROWS = 8
COLS = 16
flag_count = 0
tiles_pressed = 0
number_of_flags = 37 # 40 ordinarily

# Create a grid of None to store the references to the tiles
tiles = [[None for _ in range(COLS)] for _ in range(ROWS)]
values = [[0 for _ in range(COLS)] for _ in range(ROWS)]


def create_board():
    c.pack()
    app.update_idletasks()
    # gets unit widths for columns and rows
    col_width = c.winfo_width()/COLS
    row_height = c.winfo_height()/ROWS
    """
    # will generate 40 random mines
    def generate_mine():
        a = random.randint(0, ROWS-1)
        b = random.randint(0, COLS-1)
        if values[a][b] == 0:
            values[a][b] = -1
            return
        else:
            generate_mine()
    # create 40 mines (about 1/6 of ROW*COL)
    for _ in range(40):
        generate_mine()
    """
    # P
    values[1][0], values[2][0], values[3][0], values[4][0], values[1][1], values[3][1], values[1][2], values[2][2], values[3][2] = [-1] * 9
    # R
    values[1][4], values[1][5], values[1][6], values[2][4], values[2][6], values[3][4], values[3][5], values[4][4], values[4][6] = [-1] * 9
    # O
    values[1][8], values[2][8], values[3][8], values[4][8], values[4][9], values[4][10], values[3][10], values[2][10], values[1][10], values[1][9] = [-1] * 10
    # M
    values[1][12], values[1][14], values[2][12], values[2][13], values[2][14], values[3][12], values[3][14], values[4][12], values[4][14] = [-1] * 9

    # check surrounding for a given datapoint
    # where r = {0, ROWS-1} and c = {0, COLS-1}
    def count_surrounding(r, c):
        sum = 0
        # bottom left
        if r+1 < ROWS and c-1 >= 0:
            if values[r+1][c-1] == -1: sum += 1
        # left
        if c-1 >= 0:
            if values[r][c-1] == -1: sum += 1
        # bottom
        if r+1 < ROWS:
            if values[r+1][c] == -1: sum += 1
        # bottom right
        if r+1 < ROWS and c+1 < COLS:
            if values[r+1][c+1] == -1 : sum += 1
        # right
        if c+1 < COLS:
            if values[r][c+1] == -1 : sum += 1
        # top
        if r-1 >= 0:
            if values[r-1][c] == -1 : sum += 1
        # top right
        if r-1 >= 0 and c+1 < COLS:
            if values[r-1][c+1] == -1 : sum += 1
        # top left
        if r-1 >= 0 and c-1 >= 0:
            if values[r-1][c-1] == -1 : sum += 1
        # if sum = 0
        values[r][c] = sum

    # fill in values
    for row in range(ROWS):
        for col in range(COLS):
            if values[row][col] == -1:
                continue
            count_surrounding(row, col)
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
    # If the tile is not filled, create a rectangle
    if not tiles[row][col]:
        c.delete(tiles[row][col])
        tiles[row][col] = c.create_rectangle(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="white")
        # check to see if value is 0, make it clear
        val = "" if values[row][col] == 0 else values[row][col]
        tiles[row][col] = c.create_text(col*col_width + col_width/2, row*row_height + row_height/2, text=val, font=("Purisa", 18))
        # tiles_pressed += 1
        # for this special program, we have 37 flags
        # if tiles_pressed == (ROWS*COLS)-number_of_flags and flag_count == number_of_flags:
        # win screen
        imageBal = Image.open('balloon.jpg')
        imageBal.paste(imageBal, (750, 750))
        # Convert the Image object into a TkPhoto object
        tkimage = ImageTk.PhotoImage(imageBal)

        panel1 = tk.Label(app, image=tkimage)
        panel1.grid(row=0, column=2)

        l = tk.Label(app,text="Campbell, will you go to prom with me?", font=("Purisa", 18))
        l.place(x=300, y=300, anchor="center")
        app.mainloop()


    # If the tile is filled, delete the rectangle and clear the reference

    # else:
    #     c.delete(tiles[row][col])
    #     tiles[row][col] = None

def flag(event):
    # Get rectangle diameters
    col_width = c.winfo_width()/COLS
    row_height = c.winfo_height()/ROWS
    # Calculate column and row number
    col = int(event.x//col_width)
    row = int(event.y//row_height)

    if not tiles[row][col]:
        tiles[row][col] = c.create_text(col*col_width + col_width/2, row*row_height + row_height/2, text=emoji.emojize(":heart:", use_aliases=True), font=("Purisa", 24))
        # correctly placed flag
        if values[row][col] == -1:
            flag_count += 1
        #print(tiles[row][col])
    else:
        c.delete(tiles[row][col])
        tiles[row][col] = None
        flag_count -= 1


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
c.bind("<Button-2>", flag)

app.mainloop()
