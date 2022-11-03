#lab09 & prog09 by Linh H & Quang

# import modules
from funx import *
from time import *

# 9 box variables: row#col#
boxVals = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
validMove = [boxVals[0], boxVals[1], boxVals[2], boxVals[3], boxVals[4], boxVals[5], boxVals[6], boxVals[7], boxVals[8]]
winCheck = False

# The main code starts here.

# Print the starting, empty board.
prBrd(boxVals[0], boxVals[1], boxVals[2], boxVals[3], boxVals[4], boxVals[5], boxVals[6], boxVals[7], boxVals[8])

# Start a loop that will repeat for more times than the game will need.
while winCheck == False:
	# PLAYER TURN
	winCheck = pTurn(validMove, boxVals)
	# If the user has won, congratulate the player and exit the program.
	if winCheck == True:
		print("You win! Congratulation!")
	elif validMove == []:
		print("Game tie! Try again!")
		winCheck = True
	else:
		# COMPUTER TURN
		sleep(1.5)
		winCheck = cTurn(validMove, boxVals)
		if winCheck == True:
			print("You lose! Sorry")