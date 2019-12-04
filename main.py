import numpy as np
import os
import sys
class Board(object):
	def __init__(self,size):
		self.size = size
		self.board1 = np.chararray([self.size,self.size])
		self.board2 = np.chararray([self.size,self.size])
		self.board1[:] =  ""
		self.board2[:] = ""


	def PrintBoard(self):
		print(self.board1)
		print(self.board2)
		

class Player():
	def __init__(self,missiles,boardsize,ships):
		self.missiles = missiles
		self.boardsize = boardsize
		self.ships = ships
		# self.board = 
	def CheckValid(x,y):
		if (x<1 or x > self.M or y<1 or y > self.M):
			print("Wrong input")
			return False
		return True
	def InitialzeBoard(board):
		for i in range(self.ships):
			x = int(raw_input("x"))
			y = int(raw_input("y"))
			if self.CheckValid(x,y):
				board[x,y]  = "B"
	def MakeMove(board,x,y):
		x = int(raw_input("x"))
		y = int(raw_input("y"))
		if self.CheckValid(x,y):
			if(board[x,y] == "B"):
				board[x,y]  = "X"
			else:
				board[x,y] = "0"


	
def FileReader(filename,board1,board2):
	file = open(filename,"r")
	lineidx = 0
	result  = []
	for line in file:
		elif(lineidx == 0):
			res.append(line)
		elif(lineidx == 1):
			line.split(":")
			
		elif(lineidx == 2):
			input1
		elif(lineidx == 3):
			input1
		elif(lineidx == 4):
			input1
		elif(lineidx == 5):
			input1
		else :
			pass
		lineidx++


def main():
	boardsize = int(input("Enter size of Board "))
	board = Board(boardsize)
	board.PrintBoard()
	FileReader("input.txt",board.board1,board.board2)	
	# player1 = Player(boardsize,boardsize,boardsize)
	# player2 = Player(boardsize,boardsize,boardsize)

	# player2 = Player()


	board.PrintBoard()

main()

