import numpy as np
import os
import sys
class Game(object):
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
	def __init__(self,missiles,M,ships):
		self.missiles = missiles
		self.M = M
		self.ships = ships
		# self.board = 
	def CheckValid(x,y):
		if (x<1 or x > self.M or y<1 or y > self.M):
			return False
		return True
	def InitialzeBoard(board):
		for i in range(self.ships):
			x = int(raw_input("x"))
			y = int(raw_input("y"))
			if self.CheckValid(x,y):
				board[x,y]  = "B"

	


def main():
	# board1 = np.array[]
	boardsize = int(input("Enter size of Board "))
	game = Game(boardsize)
	# print("oof")
	game.PrintBoard()
	# player1 = Player()
	# player2 = Player()


	# game.InitialzeGame()
	game.PrintBoard()

main()

