#lab09 & prog09 by Linh H & Quang

# import modules
from funx import *
from time import *
from graphics import *

# 9 box variables: row#col#

# The main code starts here.
ticWin= GraphWin("Tic Tac Toe", 300, 300)
ticWin.setCoords(0, 0, 300, 300)

# Print the starting, empty board.
prBrd(100, 100, ticWin)
drawX(50, 50, ticWin)
drawO(150, 50, ticWin)

# Start a loop that will repeat for more times than the game will need.
	# PLAYER TURN
	# If the user has won, congratulate the player and exit the program.
		# COMPUTER TURN
		
ticWin.getMouse()
ticWin.close()