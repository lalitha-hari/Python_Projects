"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["row"]=10
    data["cols"]=10
    data["boardsize"]=500
    data["cellsize"]=data["boardsize"]/data["row"]
    data["computer"]=emptyGrid(data["row"],data["cols"])
    data["user"]=emptyGrid(data["row"],data["cols"])
    data["computerships"]=5
    data["userships"]=0
    data["computerboard"]=addShips(data["computer"],data["computerships"])
    data["userboard"]=addShips(data["user"],data["userships"])
    data["tempship"]=[]
    data["winner"]=None
    data['turns']=0
    data['maxturns']=50
    return data




''''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    
    drawGrid(data,compCanvas,data["computerboard"],showShips=False)
    drawGrid(data,userCanvas,data["userboard"],showShips=True)
    drawShip(data,userCanvas,data["tempship"])
    drawGameOver(data,canvas=userCanvas)
    return None
    



'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    if event.keysym=="Return":
        makeModel(data)
    return None


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    if board=="user":
        if data["userships"]<5:
            cell=getClickedCell(data,event)
            if cell is not None:
                clickUserBoard(data,cell[0],cell[1])
        else:
            print("you are ready placed 5 ships")
    elif board=="comp" and data['userships']==5:
        cell=getClickedCell(data,event)
        if cell is not None:
            runGameTurn(data,cell[0],cell[1])

        


   


#### STAGE 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    lst=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            row.append(EMPTY_UNCLICKED)
        lst.append(row)
    return lst


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    lst=[]
    row=random.randint(1,8)
    col=random.randint(1,8)
    verticalorhorizontal=random.randint(0,1)
    if verticalorhorizontal==0:
        lst.append([row-1,col])
        lst.append([row,col])
        lst.append([row+1,col])
    else:
        lst.append([row,col-1])
        lst.append([row,col])
        lst.append([row,col+1])
    
    return lst


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for coordinate in ship:
        X,Y=coordinate
        if grid[X][Y]!=EMPTY_UNCLICKED:
            return False

    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid,numShips):
        shipscount=0
        while shipscount<numShips:
             ship=createShip()
             if checkShip(grid,ship):
                     for coordinates in ship:
                         X,Y=coordinates
                         grid[X][Y]=SHIP_UNCLICKED
                     shipscount+=1
        return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    cellsize=data["cellsize"]
    
    for i in range(data["row"]):
        for j in range(data["cols"]):
            x1 = j * cellsize
            y1 = i * cellsize
            x2 = x1 + cellsize
            y2 = y1 + cellsize
            if grid[i][j]==SHIP_UNCLICKED and showShips==True:
                color="yellow"
            elif grid[i][j]==EMPTY_UNCLICKED:
                color="blue"
            elif grid[i][j]==SHIP_CLICKED:
                color="red"
            elif grid[i][j]==EMPTY_CLICKED:
                color="white"
            elif grid[i][j]==SHIP_UNCLICKED and showShips==False:
                color="blue"


            canvas.create_rectangle(x1, y1, x2, y2, fill=color)
    


### STAGE 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
        ship.sort()
        if ship[0][1]==ship [1][1]==ship[2][1]:
           if abs(ship[0][0]-ship[1][0])== abs(ship[1][0]-ship[2][0])==1:
               return True
        return False
         


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    ship.sort()
    if ship[0][0]==ship[1][0]==ship[2][0]:
       if abs(ship[0][1]-ship[1][1])==abs(ship[1][1]-ship[2][1])==1:
         return True
    return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    x, y = event.x, event.y
    cellsize = data["cellsize"]
    numRows, numCols = data["row"], data["cols"]

    for row in range(numRows):
        for col in range(numCols):
            x1 = col * cellsize
            y1 = row * cellsize
            x2 = x1 + cellsize
            y2 = y1 + cellsize

            if x1 <= x <= x2 and y1 <= y <= y2:
                return [row, col]
    return  None
    
    
'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    cellsize=data["cellsize"]
    for coord in ship:
        x,y=coord
        x1 = y* cellsize
        y1 = x * cellsize
        x2 = x1 + cellsize
        y2 = y1 + cellsize
        canvas.create_rectangle(x1, y1, x2, y2, fill="white")



'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if len(ship)!=3:
        return False
    if not (checkShip(grid,ship) and (isVertical(ship) or  isHorizontal(ship))):
        return False
    for coord in ship:
        i,j=coord
        if grid[i][j]==SHIP_UNCLICKED:
               return False
    return True


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''

def placeShip(data):
    if shipIsValid(data["userboard"], data["tempship"]):
        for i, j in data["tempship"]:
            data["userboard"][i][j] = SHIP_UNCLICKED  
        data["userships"] += 1
        if data["userships"] == 5:
            print("You have placed 5 ships.")
        else:
            print("Ship placement successful.")
        data["tempship"] = []
    else:
        print("Invalid ship placement.")
        data["tempship"] = []

'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["userships"]>=5:
         print("you have already placed 5 ships.")
         return
    if [row,col] in data["tempship"]:
        return
    data["tempship"].append([row,col])
    if len(data["tempship"])==3:
        placeShip(data)





### STAGE 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if board[row][col]==SHIP_UNCLICKED:
        board[row][col]=SHIP_CLICKED
        if isGameOver(board):
            data["winner"]=player
    elif board[row][col]==EMPTY_UNCLICKED:
        board[row][col]=EMPTY_CLICKED
    return
    


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    if data["computerboard"][row][col]==SHIP_CLICKED or data["computerboard"][row][col]==EMPTY_CLICKED:
        return
    else:
       data['computerboard'][row][col]== updateBoard(data,data["computerboard"],row,col,player="user")
    compguess=getComputerGuess(data["userboard"])
    updateBoard(data,data["userboard"],compguess[0],compguess[1],player="comp")
    data["turns"]+=1

    if data["turns"]==data["maxturns"]:
        data["winner"]="draw"


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    while True:
      row=random.randint(1,8)
      col=random.randint(1,8)
      if board[row][col]!=[SHIP_CLICKED,EMPTY_CLICKED]:
          return [row,col]
    

'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for row in board:
        for col in row:
            if col==SHIP_UNCLICKED:
                return False


    return True


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if data["winner"] == "user":
        canvas.delete("all")
        canvas.create_text(300, 40, text="user won the game", fill="red")
        canvas.create_text(300, 80, text="Press enter to play again", fill="red")
    elif data["winner"] == "comp":
        canvas.delete("all")
        canvas.create_text(300, 40, text="computer won the game", fill="red")
        canvas.create_text(300, 80, text="Press enter to play again", fill="red")
    elif data["winner"] == "draw":
        canvas.delete("all")
        canvas.create_text(300, 40, text="number of turns completed", fill="red")
        canvas.create_text(300, 80, text="Press enter to play again", fill="red")




### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    # print("\n" + "#"*15 + " STAGE 1 TESTS " +  "#" * 16 + "\n")
    # test.stage1Tests()
    # test.testEmptyGrid()
    # test.testCreateShip()
    # test.testCheckShip()
    #test.testAddShips()
    # test.testMakeModel()
    # test.testDrawGrid()
    # test.testIsVertical()
    # test.testIsHorizontal()
    #test.testGetClickedCell()
    #test.testDrawShip()
    # test.testShipIsValid()
    #test.testUpdateBoard()
    # test.testGetComputerGuess()
    # test.testIsGameOver()
    test.testDrawGameOver()

    ## Uncomment these for STAGE 2 ##
    """
    print("\n" + "#"*15 + " STAGE 2 TESTS " +  "#" * 16 + "\n")
    test.stage2Tests()
    """

    ## Uncomment these for STAGE 3 ##
    """
    print("\n" + "#"*15 + " STAGE 3 TESTS " +  "#" * 16 + "\n")
    test.stage3Tests()
    """
    

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
