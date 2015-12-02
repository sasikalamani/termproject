#level 2
from tkinter import *
import random
import copy
import util
import string

def init(data):
    data.rows = 9
    data.cols = 9
    data.mode = "homeScreen"
    data.cells = []
    data.jellies = []
    data.jelly2 = []
    create2dBoard(data)
    data.gameOver1 = False
    data.oneClicked = False
    data.locks = []
    data.openLocks = []
    data.swapx = None
    data.swapY = None
    data.swapCandy = None
    data.score = 0
    data.candies = util.turnTo2Dlist(data.cells, data.rows, data.cols)
    data.jellies = util.turnTo2Dlist(data.jellies, data.rows, data.cols)
    data.jelly2 = util.turnTo2Dlist(data.jelly2, data.rows, data.cols)
    data.moves = 25
    data.target = 5000
    data.passed1 = False
    data.timerDelay = 50
    data.counter = 0
    data.row = None
    data.col = None
    data.redH = PhotoImage(file = "redH.gif").subsample(2,2)
    data.swapHand = False
    data.swap1 = False
    data.swapUsed = False
    data.hammer = False
    data.hammerUsed = False

class Jelly(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.jelly = PhotoImage(file = "jelly.gif").subsample(2,2)
    def draw(self, canvas):
        if(self.jelly == None):
            pass
        canvas.create_image(self.x, self.y, image = self.jelly)
class DarkJelly(Jelly):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.jelly = PhotoImage(file = "darkJelly.gif")

class Candy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 15
        blueCandy = PhotoImage(file = "Bluecandy.gif").subsample(2,2)
        orangeCandy = PhotoImage(file = "Orange.gif").subsample(2,2)
        redCandy = PhotoImage(file = "Red.gif").subsample(2,2)
        greenCandy = PhotoImage(file = "Green.gif").subsample(2,2)
        purpleCandy = PhotoImage(file = "Purple.gif").subsample(2,2)
        yellowCandy = PhotoImage(file = "Yellow.gif").subsample(2,2)

        self.image = random.choice([blueCandy, orangeCandy,
                                    redCandy, greenCandy,
                                    purpleCandy, yellowCandy])
        if(self.image == blueCandy): self.color = "blue"
        elif(self.image == greenCandy): self.color = "green"
        elif(self.image == orangeCandy): self.color = "orange"
        elif(self.image == redCandy): self.color = "red"
        elif(self.image == purpleCandy): self.color = "purple"
        elif(self.image == yellowCandy): self.color = "yellow"
        elif(self.image == None): self.color = "clear"

    def draw(self, canvas):
        if(self.image == None):
            pass
        canvas.create_image(self.x, self.y, image = self.image)

    def __repr__(self):
        return "%s" % self.color

    def __eq__(self, other):
        if(type(self) == None):
            self.color = "clear"
        return self.color == other.color

class PackagedCandy(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.r = 15
        self.color = color
        bluePack = PhotoImage(file = "Wrapped_blue.gif").subsample(2,2)
        greenPack = PhotoImage(file = "Wrapped_green.gif").subsample(2,2)
        redPack = PhotoImage(file = "Wrapped_red.gif").subsample(2,2)
        yellowPack = PhotoImage(file = "Wrapped_yellow.gif").subsample(2,2)
        purplePack = PhotoImage(file = "Wrapped_purple.gif").subsample(2,2)
        orangePack = PhotoImage(file = "Wrapped_orange.gif").subsample(2,2)

        if(self.color == "blueP"): self.image = bluePack
        if(self.color == "greenP"): self.image = greenPack
        if(self.color == "yellowP"): self.image = yellowPack
        if(self.color == "orangeP"): self.image = orangePack
        if(self.color == "purpleP"): self.image = purplePack
        if(self.color == "redP"): self.image = redPack

    def draw(self, canvas):
        if(self.image == None):
            pass
        canvas.create_image(self.x, self.y, image = self.image)

    def __repr__(self):
        return "%s" % self.color

    def __eq__(self, other):
        if(type(self) == None):
            self.color = "clear"
        return self.color == other.color

class ColorBomb(Candy):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.color = "colorful"
        Colorbomb = PhotoImage(file = "Color_bomb_trans_.gif").subsample(2,2)
        self.image = Colorbomb
        if(self.image == Colorbomb): self.color = "colorful"

    def draw(self, canvas):
        if(self.image == None):
            pass
        canvas.create_image(self.x, self.y, image = self.image)


def makeDivisible(num, divider):
    x = 0
    while((num+x) % divider != 0):
        x+=1
    return num+x

def create2dBoard(data):
    rows = data.rows ; cols = data.cols
    for row in range(20, 288, 32):
        for col in range(70, 358, 32):
            data.jellies.append(Jelly(row, col))
            data.jelly2.append(DarkJelly(row, col))
            data.cells.append(Candy(row, col))

def isLegal(candy, otherCandy):
    if((abs(candy.x-otherCandy.x)== 32) and (abs(candy.y - otherCandy.y) == 0)):
        return True
    elif((abs(candy.x-otherCandy.x)== 0) and (abs(candy.y-otherCandy.y) == 32)):
        return True
    return False

def replaceBomb(candy, other, data):
    data.score+= 200
    (rows, cols) = (data.rows, data.cols)
    if(candy.color != "colorful"):
        color = candy.color
        checkCandy = other
    else:
        color = other.color
        checkCandy = candy
    for row in range(rows):
        for col in range(cols):
            if(data.candies[row][col].color == color or
                data.candies[row][col].x == checkCandy.x and
                data.candies[row][col].y == checkCandy.y):
                switch = data.candies[row][col]
                data.candies[row][col] = Candy(switch.x, switch.y)
                clearAllOfColor(data, color)

def clearAllOfColor(data, color):
    (rows, cols) = (data.rows, data.cols)
    for row in range(rows):
        for col in range(cols):
            if(data.candies[row][col].color == color):
                candy = data.candies[row][col]
                data.candies[row][col] = Candy(candy.x, candy.y)

def clearARow(data, rowOrCOl, dirs):
    if(dirs == "V"):
        for row in range(data.rows):
            (x, y) = (data.candies[row][rowOrCOl].x, data.candies[row][rowOrCOl].y)
            data.candies[row][rowOrCOl] = Candy(x, y)
    elif(dirs == "H"):
        for col in range(data.cols):
            (x, y) = (data.candies[rowOrCol][col].x, data.candies[rowOrCol][col].y)
            data.candies[rowOrCol][col] = Candy(x, y)

def keyPressed(event, data):
    pass

def callAll(data):
    (l, flag1) = util.findMatchingNum(
        data.candies,
        data.rows,
        data.cols,
        3)
    (n, flag2) = util.findMatchingNum(
        data.candies,
        data.rows,
        data.cols,
        4)
    (m, flag3) = util.findMatchingNum(
        data.candies,
        data.rows,
        data.cols,
        5)
    if(m == None and n== None and l==None):
        return False
    return True

def timerFired(data):
    (m, flag5) = util.findMatchingNum(
        data.candies,
        data.rows,
        data.cols,
        5)
    if(m!= None):
        (x, y) = m[2]
        candy = data.candies[x][y]
        data.candies[x][y] = ColorBomb(candy.x, candy.y)
        for (row, col) in m:
            if(data.candies[row][col].color != "colorful"):
                data.candies[row][col].color = "clear"
                data.candies[row][col].image = None

    (n, flag4) = util.findMatchingNum(
        data.candies,
        data.rows,
        data.cols,
        4)
    if(n != None):
        letter = util.findOrientation(n)
        for (row, col) in n:
            color = data.candies[row][col].color
            image = util.findImage(color, letter)
            data.candies[row][col].image = image
            data.candies[row][col].color = color + letter

    package = util.findPackage(
        data.candies,
        data.rows,
        data.cols,
        3)
    if(package != None):
        (x, y) = package[2]
        color = data.candies[x][y].color + "P"
        candy = data.candies[x][y]
        data.candies[x][y] = PackagedCandy(candy.x, candy.y, color)
        for (row, col) in package:
            if(data.candies[row][col].color != color):
                data.candies[row][col].color = "clear"
                data.candies[row][col].image = None

    (l, flag3) = util.findMatchingNum(
        data.candies,
        data.rows,
        data.cols,
        3)
    if(l != None):
        for (row, col) in l:
            data.candies[row][col].color = "clear"
            data.candies[row][col].image = None
            if(data.jelly2[row][col].jelly != None):
                data.jelly2[row][col].jelly = None
            elif(data.jellies[row][col].jelly != None):
                data.jellies[row][col].jelly = None
    gameOver(data)
    (rows, cols) = (data.rows,data.cols)
    for row in range(rows):
        for col in range(cols):
            if(data.candies[row][col].color == "clear"):
                data.score += 60
                candy = data.candies[row][col]
                data.candies[row][col] = Candy(candy.x, candy.y)
            elif(data.candies[row][col].color.endswith("V")):
                print("enter")
                clearARow(data, col, "V")
            elif(data.candies[row][col].color.endswith("H")):
                clearARow(data, row, "H")
    if(data.gameOver1):
        data.mode = "playGame2"

def noMoreJelly(data):
    (rows, cols) = (data.rows, data.cols)
    for row in range(rows):
        for col in range(cols):
            if(data.jelly2[row][col] != None):
                return False
            elif(data.jellies[row][col] != None):
                return False
    return True

def gameOver(data):
    if(noMoreJelly(data)):
        data.passed1 = True
        data.gameOver1 = True
    if(data.moves == 0 and data.score<data.target):
        data.mode = "lost"
    if(data.score>= data.target):
        data.passed1 = True
        data.gameOver1 = True

def redrawAll(canvas, data):
    (rows, cols) = (data.rows, data.cols)
    util.drawBackground(canvas, data)
    canvas.create_text(140, 380, text = "Clear All The Jelly", 
        font = "Helvetica 18")
    for row in range(rows):
        for col in range(cols):
            data.jellies[row][col].draw(canvas)
            data.jelly2[row][col].draw(canvas)
            data.candies[row][col].draw(canvas)

def mousePressed(event, data):
    (rows, cols) = (data.rows, data.cols)
    if(event.x> 7 and event.x<40 and event.y>5 and event.y<30 and 
        data.swapUsed == False):
        data.swapHand = True
    elif(event.x> 85 and event.x<115 and event.y>3 and event.y<25 and 
        data.hammerUsed == False):
        data.hammer = True
    elif(data.hammer == True):
        if(util.findPosCandy(event.x, event.y, data) != None):
            (x, y, row, col, candy) = util.findPosCandy(event.x, event.y, data)
            data.candies[row][col] = Candy(x, y)
            if(data.jelly2[row][col].jelly != None): data.jelly2[row][col].jelly = None
            elif(data.jellies[row][col].jelly != None): data.jellies[row][col].jelly = None
            data.hammer = False ; data.hammerUsed = True
    elif(event.x>50 and event.x<80 and event.y>5 and event.y<25):
        data.moves +=5
    elif(event.x>5 and event.x<30 and event.y>445 and event.y<490):
        data.mode = "help"
    elif(data.swapHand == True and data.swap1 == True):
        if(util.findPosCandy(event.x, event.y, data) != None):
            (x, y, row, col, candy) = util.findPosCandy(event.x, event.y, data)
            data.candies[data.row][data.col].x = x
            data.candies[data.row][data.col].y = y
            data.candies[data.row][data.col] = candy
            data.candies[row][col].x = data.swapx
            data.candies[row][col].y = data.swapY
            data.candies[row][col] = data.swapCandy
            data.swapHand = False; data.swap1 = False; data.swapUsed = True
            (data.swapx, data.swapY, data.row, data.col,
            data.swapCandy) =  (None, None, None, None, None)
    elif(data.swapHand == True):
        if(util.findPosCandy(event.x, event.y, data) != None):
            (data.swapx, data.swapY, data.row, data.col, 
            data.swapCandy) = util.findPosCandy(event.x, event.y, data)
            data.swap1 = True
    else:
        if(util.findPosCandy(event.x, event.y, data) != None):
            (x, y, row, col, candy) = util.findPosCandy(event.x, event.y, data)
            (x0, y0, x1, y1) = (candy.x-candy.r, candy.y-candy.r,
                                candy.x+candy.r, candy.y+candy.r)
            if(event.x>x0 and event.y>y0 and event.x<x1 and event.y<y1):
                if(data.oneClicked is False):
                    data.oneClicked = True
                    (data.swapx, data.swapY, data.row, data.col,
                        data.swapCandy) =(x, y, row, col, candy)
                    return
                elif(data.oneClicked is True):
                    data.oneClicked = False
                    if(isLegal(candy, data.candies[data.row][data.col])):
                        data.moves-=1
                        data.candies[data.row][data.col].x = x
                        data.candies[data.row][data.col].y = y
                        data.candies[data.row][data.col] = candy
                        data.candies[row][col].x = data.swapx
                        data.candies[row][col].y = data.swapY
                        data.candies[row][col] = data.swapCandy
                        if(candy.color == "colorful" or
                            data.swapCandy.color == "colorful"):
                            replaceBomb(candy, data.swapCandy, data)
                        elif(callAll(data) == False):
                            data.moves += 1
                            (data.swapx, data.swapY, 
                                data.swapCandy) = (data.candies[row][col].x, 
                                data.candies[row][col].y,data.candies[row][col])
                            data.candies[row][col].x = data.candies[data.row][data.col].x
                            data.candies[row][col].y = data.candies[data.row][data.col].y
                            data.candies[row][col] = data.candies[data.row][data.col]
                            data.candies[data.row][data.col].x = data.swapx
                            data.candies[data.row][data.col].y = data.swapY
                            data.candies[data.row][data.col] = data.swapCandy
                    (data.swapx, data.swapY, data.row, data.col,
                     data.swapCandy) =  (None, None, None, None, None)
                    return

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    # create the root and the canvas
    root = Tk()
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(300, 500)
