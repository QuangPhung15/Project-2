#lab09 & prog09 by Linh H & Quang

# import modules
from funx import *
from time import *
from random import *

# 9 box variables: row#col#
boxVals = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# The main code starts here.

# Print the starting, empty board.
prBrd(boxVals[0], boxVals[1], boxVals[2], boxVals[3], boxVals[4], boxVals[5], boxVals[6], boxVals[7], boxVals[8])

# Start a loop that will repeat for more times than the game will need.
for i in range(20):
	# PLAYER TURN
	# Get the user's move and assert that it's on the board.
	uMove = input("Please choose the box that you want to go with \n>> ")
	# Change the chosen box's value to "x" if it was the blank before the user's move.
	boxVals[int(uMove) - 1] = "x"
	# Print the board to show the user's move.
	prBrd(boxVals[0], boxVals[1], boxVals[2], boxVals[3], boxVals[4], boxVals[5], boxVals[6], boxVals[7], boxVals[8])
	# Create a variable to hold the return value of checkWin().
	# If the user has won, congratulate the player and exit the program.

	# COMPUTER TURN
	# Generate a random move by the computer.
	cMove = str(randint(1, 9))
	# Change the chosen box's value to "o" if it was blank before the computer's move.
	boxVals[int(cMove) - 1] = "o"
		# Inform the user if the computer couldn't make a valid move.
	# Print the board to show the computer's move.
	prBrd(boxVals[0], boxVals[1], boxVals[2], boxVals[3], boxVals[4], boxVals[5], boxVals[6], boxVals[7], boxVals[8])
	# Reset the win variable to hold the return value of checkWin() after the computer