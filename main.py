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

# Start a for loop that will repeat for more times than the game will need.

	# PLAYER TURN
	# Get the user's move and assert that it's on the board.
	# Change the chosen box's value to "x" if it was the blank before the user's move.
	# Print the board to show the user's move.
	# Create a variable to hold the return value of checkWin().
	# If the user has won, congratulate the player and exit the program.

	# COMPUTER TURN
	# Generate a random move by the computer.
	# Change the chosen box's value to "o" if it was blank before the computer's move.
		# Inform the user if the computer couldn't make a valid move.
	# Print the board to show the computer's move.
	# Reset the win variable to hold the return value of checkWin() after the computer