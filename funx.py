# define fuctions
def prRow(box1, box2, box3):
	"""prints a particular row of 3 boxes"""
	print(" " + box1 + " | " + box2 + " | " + box3)

def prBrd(box11, box12, box13, box21, box22, box23, box31, box32, box33):
	"""prints the entire board"""
	divider = "---+---+---"
	# call prRow() function and print divider between to draw the board
	prRow(box11, box12, box13)
	print(divider)
	prRow(box21, box22, box23)
	print(divider)
	prRow(box31, box32, box33)

def checkWin(box11, box12, box13, box21, box22, box23, box31, box32, box33):
	"""checks to see if there's a winner, returns True if there is, False otherwise"""
	winner = False
	# more code here
	return winner