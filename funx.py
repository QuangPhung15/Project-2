from random import *
from graphics import *

# define fuctions
def prBrd(width, height, win):
	"""prints the entire board"""
	for i in range(3):
		for j in range(3):
			box = Rectangle(Point(0 + width * j, 0 + height * i), Point(0 + width * (j + 1), 0 + height * (i + 1)))
			box.setFill("white")
			box.draw(win)

def drawX(xX, xY, xWin):
	"""draws X based on the center of the box"""
	x1 = Polygon(Point(xX - 25, xY - 25), Point(xX - 20, xY - 30), Point(xX + 25, xY + 25), Point(xX + 20, xY + 30))
	x2 = Polygon(Point(xX + 25, xY - 25), Point(xX + 20, xY - 30), Point(xX - 25, xY + 25), Point(xX - 20, xY + 30))
	x1.setFill("blue")
	x1.setOutline("blue")
	x2.setFill("blue")
	x2.setOutline("blue")
	x1.draw(xWin)
	x2.draw(xWin)

def drawO(oX, oY, oWin):
	"""draws O based on the center of the box"""
	o1 = Circle(Point(oX, oY), 30)
	o2 = Circle(Point(oX, oY), 24)
	o1.setFill("red")
	o1.setOutline("red")
	o2.setFill("white")
	o2.setOutline("red")
	o1.draw(oWin)
	o2.draw(oWin)

def drawLine(box11, box12, box13, box21, box22, box23, box31, box32, box33, lWin):
	"""draw a line showing where the winning move is"""
	if box11 == box12 == box13:
		line = Line(Point(10, 250), Point(290, 250))
		line.setWidth(8)
		line.setOutline(color_rgb(84, 255, 0))
		line.draw(lWin)
	elif box21 == box22 == box23:
		line = Line(Point(10, 150), Point(290, 150))
		line.setWidth(8)
		line.setOutline(color_rgb(84, 255, 0))
		line.draw(lWin)
	elif box31 == box32 == box33:
		line = Line(Point(10, 50), Point(290, 50))
		line.setWidth(8)
		line.setOutline(color_rgb(84, 255, 0))
		line.draw(lWin)
	elif box11 == box21 == box31:
		line = Line(Point(50, 290), Point(50, 10))
		line.setWidth(8)
		line.setOutline(color_rgb(84, 255, 0))
		line.draw(lWin)
	elif box12 == box22 == box32:
		line = Line(Point(150, 290), Point(150, 10))
		line.setWidth(8)
		line.setOutline(color_rgb(84, 255, 0))
		line.draw(lWin)
	elif box13 == box23 == box33:
		line = Line(Point(250, 290), Point(250, 10))
		line.setWidth(8)
		line.setOutline(color_rgb(84, 255, 0))
		line.draw(lWin)
	elif box11 == box22 == box33:
		line = Line(Point(15, 285), Point(285, 15))
		line.setWidth(8)
		line.setOutline(color_rgb(84, 255, 0))
		line.draw(lWin)
	elif box13 == box22 == box31:
		line = Line(Point(285, 285), Point(15, 15))
		line.setWidth(8)
		line.setOutline(color_rgb(84, 255, 0))
		line.draw(lWin)
	
def evalClick(cX, cY):
	"""turns player's click into the box's number"""
	if 0 < cY < 100:
		if 0 < cX < 100:
			return 7
		elif 100 < cX < 200:
			return 8
		else:
			return 9
	elif 100 < cY < 200:
		if 0 < cX < 100:
			return 4
		elif 100 < cX < 200:
			return 5
		else:
			return 6
	else:
		if 0 < cX < 100:
			return 1
		elif 100 < cX < 200:
			return 2
		else:
			return 3

def evalCenter(boxNum):
	"""turns the box's number to its center's coordinates"""
	if boxNum == 1:
		return 50, 250
	elif boxNum == 2:
		return 150, 250
	elif boxNum == 3:
		return 250, 250
	elif boxNum == 4:
		return 50, 150
	elif boxNum == 5:
		return 150, 150
	elif boxNum == 6:
		return 250, 150
	elif boxNum == 7:
		return 50, 50
	elif boxNum == 8:
		return 150, 50
	else:
		return 250, 50
		
def checkWin(box11, box12, box13, box21, box22, box23, box31, box32, box33):
	"""checks to see if there's a winner, returns True if there is, False otherwise"""
	winner = False
	# more code here
	if box11 == box12 == box13:
		winner = True
	elif box21 == box22 == box23:
		winner = True
	elif box31 == box32 == box33:
		winner = True
	elif box11 == box21 == box31:
		winner = True
	elif box12 == box22 == box32:
		winner = True
	elif box13 == box23 == box33:
		winner = True
	elif box11 == box22 == box33:
		winner = True
	elif box13 == box22 == box31:
		winner = True
	return winner

def pTurn(valMove, bVals, pWin):
	"""define player's turn"""
	# Get the user's move and assert that it's on the board.
	pMove = pWin.getMouse()
	pX = pMove.getX()
	pY = pMove.getY()
	pBox = evalClick(pX, pY)
	while not pBox in valMove:
		pMove = pWin.getMouse()
		pX = pMove.getX()
		pY = pMove.getY()
		pBox = evalClick(pX, pY)
	# Change the chosen box's value to "x" if it was the blank before the user's move.
	pX, pY = evalCenter(pBox)
	drawX(pX, pY, pWin)
	bVals[pBox - 1] = "x"
	valMove.remove(pBox)
	# Create a variable to hold the return value of checkWin().
	wCheck = checkWin(bVals[0], bVals[1], bVals[2], bVals[3], bVals[4], bVals[5], bVals[6], bVals[7], bVals[8])
	return wCheck

def cTurn(valMove1, bVals1, cWin):
	"""define computer's turn"""
	# Generate a random move by the computer.
	cBox = randint(1, 9)
	while not cBox in valMove1:
		cBox = randint(1, 9)
	cX, cY = evalCenter(cBox)
	drawO(cX, cY, cWin)
	# Change the chosen box's value to "o" if it was blank before the computer's move.
	bVals1[cBox - 1] = "o"
	valMove1.remove(cBox)
	# Reset the win variable to hold the return value of checkWin() after the computer
	wiCheck = checkWin(bVals1[0], bVals1[1], bVals1[2], bVals1[3], bVals1[4], bVals1[5], bVals1[6], bVals1[7], bVals1[8])
	return wiCheck