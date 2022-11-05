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

def pTurn(valMove, bVals):
	print("------------------------- PLAYER TURN ------------------------------")
	# Get the user's move and assert that it's on the board.
	uMove = input("Please choose the box that you want to go with \n>> ")
	while not uMove in valMove:
		uMove = input("Please choose the box that you want to go with \n>> ")
	# Change the chosen box's value to "x" if it was the blank before the user's move.
	bVals[int(uMove) - 1] = "x"
	valMove.remove(uMove)
	# Print the board to show the user's move.
	prBrd(bVals[0], bVals[1], bVals[2], bVals[3], bVals[4], bVals[5], bVals[6], bVals[7], bVals[8])
	# Create a variable to hold the return value of checkWin().
	wCheck = checkWin(bVals[0], bVals[1], bVals[2], bVals[3], bVals[4], bVals[5], bVals[6], bVals[7], bVals[8])
	return wCheck

def cTurn(valMove1, bVals1):
	print("------------------------- COMPUTER TURN ------------------------------")
	# Generate a random move by the computer.
	cMove = str(randint(1, 9))
	while not cMove in valMove1:
		cMove = str(randint(1, 9))
	# Change the chosen box's value to "o" if it was blank before the computer's move.
	bVals1[int(cMove) - 1] = "o"
	valMove1.remove(cMove)
		# Inform the user if the computer couldn't make a valid move.
	# Print the board to show the computer's move.
	prBrd(bVals1[0], bVals1[1], bVals1[2], bVals1[3], bVals1[4], bVals1[5], bVals1[6], bVals1[7], bVals1[8])
	# Reset the win variable to hold the return value of checkWin() after the computer
	wiCheck = checkWin(bVals1[0], bVals1[1], bVals1[2], bVals1[3], bVals1[4], bVals1[5], bVals1[6], bVals1[7], bVals1[8])
	return wiCheck

