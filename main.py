#lab09 & prog09 by Linh H & Quang

# import modules
from funx import *
from time import *
from random import *

# define fuctions
def prRow(box1, box2, box3):
	"""prints a particular row of 3 boxes"""
	print(" " + box1 + " | " + box2 + " | " + box3)

def prBrd(box11, box12, box13, box21, box22, box23, box31, box32, box33):
	"""prints the entire board"""
	divider = "---+---+---"
	# more code here

def checkWin(box11, box12, box13, box21, box22, box23, box31, box32, box33):
	"""checks to see if there's a winner, returns True if there is, False otherwise"""
	winner = False
	# more code here
	return winner

# 9 box variables: row#col#

# The main code starts here.

# Print the starting, empty board.

# Start a loop that will repeat for more times than the game will need.
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