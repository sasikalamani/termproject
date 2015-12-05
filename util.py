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
            (result, flag) = checkRowCol(row, col, num, data)
            if len(result) == num:
                return (result, flag)
    return (None, flag)

def findPackage(data, rows, cols):
    for row in range(rows):
        for col in range(cols):
            result = checkPackage(data, row, col)
            if (result!= None):
                return (result, row, col)
    return (None, None, None)

""" Given an initial row, column, returns an array of cell locations that match
    whether the color matches the initial location num times, horizontally, or
    vertically (whichever comes first). """
def checkRowCol(startRow, startCol, num, data):
    flag = None
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
            if ((checkRow < 0) or (checkRow >= rows) or (checkCol < 0) or (checkCol >= cols)):
                break
            if("V" in data[checkRow][checkCol].color or "H" in data[checkRow][checkCol].color):
                flag = data[checkRow][checkCol].color[-1:]
                data[checkRow][checkCol].color = data[checkRow][checkCol].color[:-1]
            # Check for out of bounds
            if ((data[checkRow][checkCol] != color)):
                break
            else:
                result.append((checkRow, checkCol))
                if(len(result) == num):
                    #flag = findFlag(result, data)
                    return (result, flag)
    return (result, flag)

def findFlag(result, data):
    flag = None
    counter += 1
    for (row, col) in result:
        if("V" in data[row][col].color or "H" in data[row][col].color):
            flag = data[row][col].color[-1:]
            data[row][col].color = data[row][col].color[:-1]
    return flag

def checkPackage(data, startRow, startCol):
    num = data[startRow][startCol]
    rows = len(data)
    cols = len(data[0])
    dirs = [((-1, 0), (0, -1)), ((-1, 0), (0, 1)), ((1, 0), (0, -1)), ((1, 0), (0, 1))]
    for dir in range(len(dirs)):
        result = set()
        for direction in dirs[dir]:
            (drow, dcol) = direction
            for i in range(3):
                checkRow = startRow + i*drow
                checkCol = startCol + i*dcol
                if(checkRow< 0 or checkRow>=rows or checkCol< 0 
                    or checkCol>=cols):
                    break
                if(data[checkRow][checkCol] != num):
                    break
                else:
                    result.add((checkRow, checkCol))
                    if(len(result) == 5):
                        return result
    return None

def findImage(color, letter):
    blueH = PhotoImage(file = "blueH.gif").subsample(2,2)
    greenH = PhotoImage(file = "greenH.gif").subsample(2,2)
    redH = PhotoImage(file = "redH.gif").subsample(2,2)
    yellowH = PhotoImage(file = "yellowH.gif").subsample(2,2)
    purpleH = PhotoImage(file = "purpleH.gif").subsample(2,2)
    orangeH = PhotoImage(file = "orangeH.gif").subsample(2,2)

    blueV = PhotoImage(file = "blueV.gif").subsample(2,2)
    greenV = PhotoImage(file = "greenV.gif").subsample(2,2)
    redV = PhotoImage(file = "redV.gif").subsample(2,2)
    yellowV = PhotoImage(file = "yellowV.gif").subsample(2,2)
    purpleV = PhotoImage(file = "purpleV.gif").subsample(2,2)
    orangeV = PhotoImage(file = "orangeV.gif").subsample(2,2)

    if(color == "blue" and letter == "H"): return blueH
    elif(color == "blue" and letter == "V"): return blueV

    if(color == "green" and letter == "H"): return greenH
    elif(color == "green" and letter == "V"): return greenV

    if(color == "red" and letter == "H"): return redH
    elif(color == "red" and letter == "V"): return redV

    if(color == "yellow" and letter == "H"): return yellowH
    elif(color == "yellow" and letter == "V"): return yellowV

    if(color == "purple" and letter == "H"): return purpleH
    elif(color == "purple" and letter == "V"): return purpleV

    if(color == "orange" and letter == "H"): return orangeH
    elif(color == "orange" and letter == "V"): return orangeV

def findOrientation(list1):
    checkRow = None
    for (row, col) in list1:
        if(checkRow == None):
            checkRow = row
        elif(row != checkRow):
            return "V"
    return "H"
        
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
    data.hand = PhotoImage(file = "Booster_free_switch.gif").subsample(4,4)
    canvas.create_image (28, 15, image = data.hand)

def findPosCandy(x, y, data):
    (rows, cols) = (data.rows, data.cols)
    for row in range(data.rows):
        for col in range(data.cols):
            candy = data.candies[row][col]
            (x0, y0, x1, y1) = (candy.x-candy.r, candy.y-candy.r,
                                candy.x+candy.r, candy.y+candy.r)
            if(x>x0 and y>y0 and x<x1 and y<y1):
                return (candy.x, candy.y, row, col, candy)
    return None
