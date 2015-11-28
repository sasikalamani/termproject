#Sasikala Mani
#TP
#Section EE

from tkinter import *
import random
import copy
import util

####################################
# init
####################################

def init(data):
    print ("HAHAHAHAH")
    data.mode = "homeScreen"
    data.cells = []
    create2dBoard(data)
    data.gameOver1 = False
    data.oneClicked = False
    data.locks = []
    createListLocks(data)
    data.openLocks = []
    data.swapx = None
    data.swapY = None
    data.swapCandy = None
    data.score = 0
    data.candies = util.turnTo2Dlist(data.cells, 9, 9)
    data.moves = 10
    data.target = 3500
    data.passed1 = False
    data.timerDelay = 50
    data.counter = 0
    data.row = None
    data.col = None

####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "homeScreen"): homeScreenMousePressed(event, data)
    elif (data.mode == "demoLevel"):   demoLevelMousePressed(event, data)
    elif (data.mode == "help"):       helpMousePressed(event, data)
    elif(data.mode == "playGame2"): playGame2MousePressed(event, data)
    elif(data.mode == "lock"): lockMousePressed(event, data)
    elif(data.mode == "lock1"): lock1MousePressed(event, data)
    elif(data.mode == "lost"): lostMousePressed(event, data)


def keyPressed(event, data):
    if (data.mode == "homeScreen"): homeScreenKeyPressed(event, data)
    elif (data.mode == "demoLevel"):   demoLevelKeyPressed(event, data)
    elif (data.mode == "help"):       helpKeyPressed(event, data)
    elif(data.mode == "playGame2"): playGame2KeyPressed(event, data)
    elif(data.mode == "lock"): lockKeyPressed(event, data)
    elif(data.mode == "lock1"): lock1KeyPressed(event, data)
    elif(data.mode == "lost"): lostKeyPressed(event, data)


def timerFired(data):
    if (data.mode == "homeScreen"): homeScreenTimerFired(data)
    elif (data.mode == "demoLevel"):   demoLevelTimerFired(data)
    elif (data.mode == "help"):       helpTimerFired(data)
    elif(data.mode == "playGame2"):  playGame2TimerFired(data)
    elif(data.mode == "lock"):  lockTimerFired(data)
    elif(data.mode == "lock1"):  lock1TimerFired(data)
    elif(data.mode == "lost"):  lostTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "homeScreen"): homeScreenRedrawAll(canvas, data)
    elif (data.mode == "demoLevel"):   demoLevelRedrawAll(canvas, data)
    elif (data.mode == "help"):       helpRedrawAll(canvas, data)
    elif(data.mode == "playGame2"): playGame2RedrawAll(canvas, data)
    elif(data.mode == "lock"): lockRedrawAll(canvas, data)
    elif(data.mode == "lock1"): lock1RedrawAll(canvas, data)
    elif(data.mode == "lost"): lostRedrawAll(canvas, data)

####################################
# splashScreen mode
####################################

def homeScreenMousePressed(event, data):
    leftX = 100; rightX= 200; topX = 245; topY=275
    if(event.x>leftX and event.x<rightX and event.y>topX and event.y<topY):
        data.mode = "demoLevel"
    if(event.x>110 and event.x<140 and event.y>420 and event.y<450):
        data.mode = "help"
    if(data.passed1):
        data.mode = "lock1"
    elif(event.x>130 and event.x<160 and event.y>470 and event.y<500):
        data.mode = "lock"

def homeScreenKeyPressed(event, data):
    pass

def homeScreenTimerFired(data):
    pass

def homeScreenRedrawAll(canvas, data):
    data.image = PhotoImage(file="homepage.gif")
    image = data.image
    data.halfImage = data.image.subsample(2,2)
    canvas.create_image(150, 250, image=data.halfImage)

####################################
# lockedLevels mode
####################################
class Locks(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, canvas):
        self.lock = PhotoImage(file = "lockSymbol.gif").subsample(2,2)
        canvas.create_image(self.x, self.y, image = self.lock)

class OpenLock1(Locks):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.r = 30
    def draw(self, canvas):
        canvas.create_rectangle(self.x-self.r, self.y-self.r,
                                self.x+self.r, self.y+self.r, fill="blue")
        canvas.create_text(self.x, self.y, text = "1")

def createListLocks(data):
    for row in range(50, 250, 95):
        for col in range(50, 250, 95):
            data.locks.append(Locks(row, col))

def lockMousePressed(event, data):
    if(event.x>270 and event.x<300 and event.y>0 and event.y<30):
        data.mode = "homeScreen"

def lockKeyPressed(event, data):
    pass

def lockTimerFired(data):
    pass

def lockRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, 300, 500, fill = "light blue")
    canvas.create_rectangle(270, 0, 300, 30, fill = "red")
    canvas.create_text(285, 15, text = "X")
    for lock in data.locks:
        lock.draw(canvas)
    for lock in data.openLocks:
        lock.draw(canvas)
    canvas.create_text(150, 375, text = "Now Create Your Own Level",
        font = "Comic 20")

####################################
# lock1 mode
####################################

def lock1MousePressed(event, data):
    if(event.x>270 and event.x<300 and event.y>0 and event.y<30):
        data.mode = "homeScreen"
    elif(event.x>20 and event.x<80 and event.y>20 and event.y<80):
        data.mode = "demoLevel"

def lock1KeyPressed(event, data):
    pass

def lock1TimerFired(data):
    pass

def lock1RedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, 300, 500, fill = "light blue")
    canvas.create_rectangle(270, 0, 300, 30, fill = "red")
    canvas.create_text(285, 15, text = "X")
    for lock in data.locks:
        lock.draw(canvas)
    for lock in data.openLocks:
        lock.draw(canvas)
    canvas.create_text(150, 375, text = "Now Create Your Own Level",
        font = "Comic 20")
    OpenLock1(50, 50).draw(canvas)

####################################
# lost mode
####################################
def lostMousePressed(event, data):
    if(event.x>90 and event.x<200 and event.y>350 and event.y<380):
        init(data)

def lostKeyPressed(event, data):
    pass

def lostTimerFired(data):
    pass

#taken from notes
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def lostRedrawAll(canvas, data):
    beige = rgbString(220, 213, 183)
    canvas.create_rectangle(0, 0, data.width, data.height, fill = beige)
    data.image = PhotoImage(file = "youfailed.gif").subsample(2,2)
    canvas.create_image(data.width/2, data.height/2, image = data.image)
    canvas.create_rectangle(183, 285, 230, 310, fill = beige, outline = beige)
    canvas.create_text(210, 300, text = data.score)
    canvas.create_rectangle(265, 80, 300, 400, fill = beige, outline = beige)
    canvas.create_rectangle(0, 390, 300, 410, fill = beige, outline = beige)
    canvas.create_rectangle(0, 85, 10, 420, fill = beige, outline = beige)

####################################
# help mode
####################################

def helpMousePressed(event, data):
    (rangex, rangex1, rangey, rangey1) = (260, 300, 0, 40)
    if(event.x>rangex and event.x< rangex1 and event.y>rangey and event.y<rangey1):
        data.mode = "demoLevel"
def helpKeyPressed(event, data):
    data.mode = "demoLevel"

def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    data.image = PhotoImage(file="howtoplay.gif")
    image = data.image
    canvas.create_image(150, 125, image=image)
    data.image2 = PhotoImage(file = "helpscreen.gif")
    canvas.create_image(150, 375, image = data.image2)

####################################
# level1 mode
####################################

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

class SideStripedCandy(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.r = 15
        self.color = color
        blueCandy = PhotoImage(file = "blueH.gif").subsample(2,2)
        greenCandy = PhotoImage(file = "greenH.gif").subsample(2,2)
        redCandy = PhotoImage(file = "redH.gif").subsample(2,2)
        yellowCandy = PhotoImage(file = "yellowH.gif").subsample(2,2)
        purpleCandy = PhotoImage(file = "purpleH.gif").subsample(2,2)
        orangeCandy = PhotoImage(file = "orangeH.gif").subsample(2,2)
        if(self.color == "blue"): self.image = blueCandy
        elif(self.color == "green"): self.color = greenCandy
        elif(self.color == "orange"): self.color = orangeCandy
        elif(self.color == "red"): self.color = redCandy
        elif(self.color == "purple"): self.color = purpleCandy
        elif(self.color == "yellow"): self.color = yellowCandy
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

class UpStripedCandy(Candy):
    def __init__(self, x, y):
        super().__init__(x, y)
        blueCandy = PhotoImage(file = "blueV.gif").subsample(2,2)
        greenCandy = PhotoImage(file = "greenV.gif").subsample(2,2)
        redCandy = PhotoImage(file = "redV.gif").subsample(2,2)
        yellowCandy = PhotoImage(file = "yellowV.gif").subsample(2,2)
        purpleCandy = PhotoImage(file = "purpleV.gif").subsample(2,2)
        orangeCandy = PhotoImage(file = "orangeV.gif").subsample(2,2)


class PackagedCandy(Candy):
    def __init__(self, x, y):
        super().__init__(x, y)
        blueCandy = PhotoImage(file = "Wrapped_blue.gif").subsample(2,2)
        greenCandy = PhotoImage(file = "Wrapped_green.gif").subsample(2,2)
        redCandy = PhotoImage(file = "Wrapped_red.gif").subsample(2,2)
        yellowCandy = PhotoImage(file = "Wrapped_yellow.gif").subsample(2,2)
        purpleCandy = PhotoImage(file = "Wrapped_purple.gif").subsample(2,2)
        orangeCandy = PhotoImage(file = "Orange_wrapped.gif").subsample(2,2)

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
    rows = 9 ; cols = 9
    for row in range(20, 288, 32):
        for col in range(70, 358, 32):
            data.cells.append(Candy(row, col))

def isLegal(candy, otherCandy):
    if((abs(candy.x-otherCandy.x)== 32) and (abs(candy.y - otherCandy.y) == 0)):
        return True
    elif((abs(candy.x-otherCandy.x)== 0) and (abs(candy.y - otherCandy.y) == 32)):
        return True
    return False

def replaceBomb(candy, other, data):
    data.score+= 200
    (rows, cols) = (9, 9)
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
    (rows, cols) = (9, 9)
    for row in range(rows):
        for col in range(cols):
            if(data.candies[row][col].color == color):
                candy = data.candies[row][col]
                data.candies[row][col] = Candy(candy.x, candy.y)

def demoLevelKeyPressed(event, data):
    print("hi")
    m = util.findMatchingNum(
        data.candies,
        len(data.candies),
        len(data.candies[0]),
        4)
    if(m!= None):
        (x, y) = m[2]
        candy = data.candies[x][y]
        data.candies[x][y] = ColorBomb(candy.x, candy.y)
        for (row, col) in m:
            if(data.candies[row][col].color != "colorful"):
                data.candies[row][col].color = "clear"
                data.candies[row][col].image = None

    l = util.findMatchingNum(
        data.candies,
        len(data.candies),
        len(data.candies[0]),
        3)
    if(l != None):
        for (row, col) in l:
            data.candies[row][col].color = "clear"
            data.candies[row][col].image = None

def demoLevelTimerFired(data):
    gameOver(data)
    (rows, cols) = (9,9)
    for row in range(rows):
        for col in range(cols):
            if(data.candies[row][col].color == "clear"):
                data.score += 60
                candy = data.candies[row][col]
                data.candies[row][col] = Candy(candy.x, candy.y)
    if(data.gameOver1):
        data.mode = "playGame2"

def gameOver(data):
    if(data.moves == 0 and data.score<data.target):
        data.mode = "lost"
    if(data.score>= data.target):
        data.passed1 = True
        data.gameOver1 = True

#taken from notes
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def demoLevelRedrawAll(canvas, data):
    (rows, cols) = (9, 9)
    util.drawBackground(canvas, data)
    for row in range(rows):
        for col in range(cols):
            data.candies[row][col].draw(canvas)

def demoLevelMousePressed(event, data):
    (rows, cols) = (9, 9)
    if(event.x>5 and event.x<30 and event.y>445 and event.y<490):
        data.mode = "help"
    for row in range(rows):
        for col in range(cols):
            candy = data.candies[row][col]
            (x0, y0, x1, y1) = (candy.x-candy.r, candy.y-candy.r,
                                candy.x+candy.r, candy.y+candy.r)
            if(event.x>x0 and event.y>y0 and event.x<x1 and event.y<y1):
                if(data.oneClicked is False):
                    data.oneClicked = True
                    (data.swapx, data.swapY, data.row, data.col,
                        data.swapCandy) =(candy.x, candy.y, row, col, candy)
                    return
                elif(data.oneClicked is True):
                    data.oneClicked = False
                    if(isLegal(candy, data.candies[data.row][data.col])):
                        data.moves-=1
                        data.candies[data.row][data.col].x = candy.x
                        data.candies[data.row][data.col].y = candy.y
                        data.candies[data.row][data.col] = candy
                        data.candies[row][col].x = data.swapx
                        data.candies[row][col].y = data.swapY
                        data.candies[row][col] = data.swapCandy
                        if(candy.color == "colorful" or
                            data.swapCandy.color == "colorful"):
                            replaceBomb(candy, data.swapCandy, data)
                    (data.swapx, data.swapY, data.row, data.col,
                     data.swapCandy) =  (None, None, None, None, None)
                    return

####################################
# level2 mode
####################################

def playGame2KeyPressed(event, data):
    data.mode = "homeScreen"

def playGame2MousePressed(event, data):
    pass

def playGame2RedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2-20,
                       text="Level 2 Screen!", font="Arial 34 bold")

def playGame2TimerFired(data):
    pass

####################################
# use the run function as-is
####################################

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



#sources
#Arathi Mani for debugging
#http://image.online-convert.com/convert-to-gif
#http://candycrush.wikia.com
#http://www.technologytell.com/apple/108797/appidemic-candy-cruch-from-king-com/
#http://ramp.ie/index.php/games/ramp-randoms-candy-crush-saga-devil/

#Questions to ask Sarah
#how do i inherit a level
