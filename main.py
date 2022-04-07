from player import HumanPlayer, CpuPlayer, SmartCpuPlayer
from boardCheck import fullBoardCheck, xWinCheck, oWinCheck
from evaluate import evaluateBoard
import os
import time

class TicTacToe:

  def __init__(self, x, o):
    self.board = [[0,0,0],[0,0,0],[0,0,0]] 
    self.gameOver = False # initializes board as 0, 1, or -1
    
    if x == 1:
      self.x = HumanPlayer(self.board)
    elif x == -1:
      while True:
        try:
          depth = int(input("Depth of X cpu >> "))
          break
        except:
          print("\nInvalid depth\n")
          continue
          
      self.x = SmartCpuPlayer(self.board, True, depth)
      
    if o == 1:
      self.o = HumanPlayer(self.board)
    elif o == -1:
      while True:
        try:
          depth = int(input("Depth of O cpu >> "))
          break
        except:
          print("\nInvalid depth\n")
          continue
      self.o = SmartCpuPlayer(self.board, False, depth)

  def draw_board(self):

    # draws board using X's and O's in place of the number values
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    for c in self.board:
      for s in c: 
        if s == 0:
          print('-',end=' ')
        elif s == 1:
          print('X',end=' ')
        elif s == -1:
          print('O',end=' ')
        else:
          print('-',end=' ')
      print('\n')

  
  def play(self):

    while not self.gameOver:
      
      self.draw_board()
      # print(evaluateBoard(self.board))

      xMove = self.x.get_move()

      self.board[xMove[0]][xMove[1]] = 1 # adds move to board

      # checks if X wins the game after they move
      if xWinCheck(self.board):
        print(evaluateBoard(self.board))
        self.draw_board()
        print('X wins')
        self.gameOver = True
        break
      # checks if the last move was a cat's game AFTER it checks if X wins
      elif fullBoardCheck(self.board):
        print(evaluateBoard(self.board))
        self.draw_board()
        print("\nCat's game")
        self.gameOver = True
        break


      self.draw_board()
      # print(evaluateBoard(self.board))
      oMove = self.o.get_move()

      self.board[oMove[0]][oMove[1]] = -1 # adds move to the board

      if oWinCheck(self.board):
        print(evaluateBoard(self.board))
        self.draw_board()
        print('O wins')
        self.gameOver = True
        break


if __name__ == '__main__':
  
  while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    try:
      xPlayer = input("X player (1 for human, -1 for cpu) >> ")
      oPlayer = input("O player (1 for human, -1 for cpu) >> ")
        
      game = TicTacToe(int(xPlayer), int(oPlayer))
      game.play();
          
    except ValueError:
      os.system('cls' if os.name == 'nt' else 'clear')
      continue

    playAgain = input("\n\nPlay again? (y/n) >> ")

    if playAgain.lower() != 'y':
      os.system('cls' if os.name == 'nt' else 'clear')
      print("See you later!")
      break