def turnTo2Dlist(data):
    result = list()
    (rows, cols) = (9,9)
    result = [ ([0] * cols) for row in range(rows) ]
    for row in range(9):
        for col in range(9):
            result[row][col] = data.cells[(8*col)+row+col]
    return result

def findFive(data):
    (rows, cols) = (len(data.candies), len(data.candies[0]))
    for row in range(rows):
        for col in range(cols):
            color = data.candies[row][col]
            result = checkRowCol(row, col, 5, color, data)
    return result  

def findFour(data):
    (rows, cols) = (len(data.candies), len(data.candies[0]))
    for row in range(rows):
        for col in range(cols):
            color = data.candies[row][col]
            result = checkRowCol(row, col, 4, color, data)
    return result       

def findThree(data):
    (rows, cols) = (len(data.candies), len(data.candies[0]))
    for row in range(rows):
        for col in range(cols):
            color = data.candies[row][col]
            result = checkRowCol(row, col, 3, color, data)
            if len(result) == 3:
                return result
    return None

def checkRowCol(startRow, startCol, num, color, data):
    (rows, cols) = (len(data.candies), len(data.candies[0]))
    directions = [(0, 1), (1, 0)]
    for dirs in range(len(directions)):
        result = list()
        (drow, dcol) = directions[dirs]
        for i in range(num):
            checkRow = startRow + i*drow
            checkCol = startCol + i*dcol
            if ((checkRow < 0) or (checkRow >= rows) or
                (checkCol < 0) or (checkCol >= cols) or
                (data.candies[checkRow][checkCol] != color)):
                break
            else:
                result.append((checkRow, checkCol))
                if(len(result) == num):
                    return result
    return result