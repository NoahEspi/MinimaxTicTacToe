from random import randint
from boardCheck import fullBoardCheck, xWinCheck, oWinCheck
from evaluate import evaluateBoard
import math

class HumanPlayer:
  def __init__(self, currentBoard):
    self.currentBoard = currentBoard;
    self.moveNums = {'1': (0,0), '2': (0,1), '3': (0,2),
                    '4': (1,0), '5': (1,1), '6': (1,2),
                    '7': (2,0), '8': (2,1), '9': (2,2)}
    
  def get_move(self):

    while True:

      move = input('Move >> ')

      if not ',' in move:
        try:
          x,y = self.moveNums[move]
        except:
          print('\nInvalid input\n')
          continue
          
      else:
        try:
          x,y = move.split(',')
          x,y = int(x), int(y) # checks if input is a number and in correct format
        except ValueError:
          print('\nInvalid input\n') # outputs "invalid input" if it's not in correct format
          continue

      if fullBoardCheck(self.currentBoard):
        return x,y

      try:
        if self.currentBoard[x][y] != 0: # checks if move is an empty space on board
          print('\nInvalid move\n') 
          continue
      except IndexError:
        print('\nInvalid move\n') # returns error output if number is too large for the board (i.e. 4,2 is invalid)
        continue
        
        
      return x,y

      
class CpuPlayer:
  def __init__(self, currentBoard):
    self.currentBoard = currentBoard;

  def get_move(self):

    while True:

      if self.currentBoard[1][2] == 0:
        x,y = 1,2
      else:
        x,y = randint(0,2), randint(0,2) # chooses random move for computer

      while self.currentBoard[x][y] != 0:
        x,y = randint(0,2), randint(0,2) # if random move chosen is not an empty space, re-pick

      return x,y

"""
https://pastebin.com/rZg1Mz9G
"""

class SmartCpuPlayer:
  def __init__(self, currentBoard, maxPlayer, depth):
    self.currentBoard = currentBoard
    self.maxPlayer = maxPlayer
    self.depth = depth
    
  def get_move(self):
    print("\nThinking...\n")
    move = self.minimax(self.currentBoard, -math.inf, math.inf, self.depth, self.maxPlayer)['move']
      
    return move

  def minimax(self, simBoard, alpha, beta, depth, maxPlayer):

    if depth == 0 or xWinCheck(simBoard) or oWinCheck(simBoard) or fullBoardCheck(simBoard):
      return {'eval': evaluateBoard(simBoard), 'move': None}

    emptyCells = []
  
    for i in range(3):
      for j in range(3):

        if simBoard[i][j] == 0:
          emptyCells.append((i,j))

    if maxPlayer:
      maxEval = -math.inf
      move = None
      
      for c in emptyCells:
        
        if simBoard[c[0]][c[1]] == 0:
        
          simBoard[c[0]][c[1]] = 1
      
          eval = self.minimax(simBoard, -math.inf, math.inf, depth-1, False)
        
          simBoard[c[0]][c[1]] = 0

          alpha = max(alpha, eval['eval'])
          if beta <= alpha:
            break

          if maxEval < eval['eval']:
            maxEval = eval['eval']
            move = (c[0], c[1])
        
      return {'eval': maxEval, 'move': move}

    else:
      minEval = math.inf
      move = None
      
      for c in emptyCells:

        if simBoard[c[0]][c[1]] == 0:
          
          simBoard[c[0]][c[1]] = -1

          eval = self.minimax(simBoard, -math.inf, math.inf, depth-1, True)

          simBoard[c[0]][c[1]] = 0

          beta = min(beta, eval['eval'])
          if beta <= alpha:
            break

          if minEval > eval['eval']:
            minEval = eval['eval']
            move = (c[0], c[1])

      return {'eval': minEval, 'move': move}