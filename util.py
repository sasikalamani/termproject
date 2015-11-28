from tkinter import *


""" Given unformatted data, return a 2D list. """
def turnTo2Dlist(data, rows, cols):
    result = [ ([0] * cols) for row in range(rows) ]
    for row in range(rows):
        for col in range(cols):
            result[row][col] = data[(8*col)+row+col]
    return result

""" Given a 2D array, return a list of lists.  Each list has the locations of 
    matching colors of the first value in the list. (TODO: Fix this comment) """
def findMatchingNum(data, rows, cols, num):
    for row in range(rows):
        for col in range(cols):
            result = checkRowCol(row, col, num, data)
            if len(result) == num:
                return result
    return None

""" Given an initial row, column, returns an array of cell locations that match
    whether the color matches the initial location num times, horizontally, or
    vertically (whichever comes first). """
def checkRowCol(startRow, startCol, num, data):
    color = data[startRow][startCol]
    rows = len(data)
    cols = len(data[0])
    directions = [(0, 1), (1, 0)]
    for dirs in range(len(directions)):
        result = list()
        (drow, dcol) = directions[dirs]
        for i in range(num):
            checkRow = startRow + i*drow
            checkCol = startCol + i*dcol
            # Check for out of bounds
            if ((checkRow < 0) or (checkRow >= rows) or
                (checkCol < 0) or (checkCol >= cols) or
                (data[checkRow][checkCol] != color)):
                break
            else:
                result.append((checkRow, checkCol))
                if(len(result) == num):
                    return result
    return result

#taken from notes
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def drawBackground(canvas, data):
    data.back = PhotoImage(file = "level1.gif").subsample(2, 2)
    canvas.create_image(150, 250, image = data.back)
    canvas.create_rectangle(115, 448, 150, 460, fill = "pink", outline = "pink")
    canvas.create_text(132, 454, text = "%d" % data.moves)
    canvas.create_rectangle(210, 447, 245, 463, fill = "pink", outline = "pink")
    canvas.create_text(227, 455, text = "%d" % data.score)
    canvas.create_rectangle(220, 10, 255, 23, fill = "pink", outline = "pink")
    canvas.create_text(237, 16, text = "%d" % data.target, 
        font = "Times 16 italic")
    background = rgbString(125, 155, 216)
    lineColor = rgbString(162, 181, 220)
    canvas.create_rectangle(0,50, 300, 350, fill=background)
    for x in range(36, 270, 32):
        canvas.create_line(x, 50, x, 340, fill=lineColor, width = 2)
    for y in range(53, 358, 32):
        canvas.create_line(0, y, 300, y, fill= lineColor, width =2)