#lab09 & prog09 by Linh H & Quang

# import modules
from funx import *
from time import *
from graphics import *

# 9 box variables: row#col#
boxVals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
validMove = [boxVals[0], boxVals[1], boxVals[2], boxVals[3], boxVals[4], boxVals[5], boxVals[6], boxVals[7], boxVals[8]]
winCheck = False

# The main code starts here.
ticWin= GraphWin("Tic Tac Toe", 300, 300)
ticWin.setCoords(0, 0, 300, 300)

# Print the starting, empty board.
prBrd(100, 100, ticWin)

# Start a loop that will repeat for more times than the game will need.
while winCheck == False:
	# PLAYER TURN
	winCheck = pTurn(validMove, boxVals, ticWin)
	# If the user has won, congratulate the player and exit the program.
	if winCheck == True:
		drawLine(boxVals[0], boxVals[1], boxVals[2], boxVals[3], boxVals[4], boxVals[5], boxVals[6], boxVals[7], boxVals[8], ticWin)
		print("You win! Congratulations!")
	elif validMove == []:
		print("Game tie! Try again!")
		winCheck = True
	else:
		# COMPUTER TURN
		sleep(1)
		winCheck = cTurn(validMove, boxVals, ticWin)
		if winCheck == True:
			drawLine(boxVals[0], boxVals[1], boxVals[2], boxVals[3], boxVals[4], boxVals[5], boxVals[6], boxVals[7], boxVals[8], ticWin)
			print("You lose! Sorry")
		
ticWin.getMouse()
ticWin.close()