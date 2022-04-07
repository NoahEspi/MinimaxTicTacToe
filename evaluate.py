from boardCheck import fullBoardCheck, xWinCheck, oWinCheck
import math

"""
Evaluation equation taken from here:
https://john.cs.olemiss.edu/~dwilkins/CSCI531/fall12/slides/AI_09_games.pdf
"""

def evaluateBoard(board):

  # x2/o2 - number of lines with 2 x's/o's and a blank
  # x1/o1 - number of lines with 1 x/o and a blank
  x1,x2,o1,o2 = 0,0,0,0

  # establishes "rows" of columns and diagonals for ease of access
  col1 = [board[0][0], board[1][0], board[2][0]]
  col2 = [board[0][1], board[1][1], board[2][1]]
  col3 = [board[0][2], board[1][2], board[2][2]]

  diagonal1 = [board[0][0], board[1][1], board[2][2]]
  diagonal2 = [board[0][2], board[1][1], board[2][0]]

  columns = [col1, col2, col3]
  diagonals = [diagonal1, diagonal2] 

  # creates values for x2, o2, x1, o1 variables for below eval equation
  for row in board:
    if row.count(1) == 2 and row.count(0) == 1:
      x2 += 1
    if row.count(-1) == 2 and row.count(0) == 1:
      o2 += 1
    if (1 in row) and row.count(0) == 2:
      x1 += 1
    if (-1 in row) and row.count(0) == 2:
      o1 += 1

  for col in columns:
    if col.count(1) == 2 and col.count(0) == 1:
      x2 += 1
    if col.count(-1) == 2 and col.count(0) == 1:
      o2 += 1
    if (1 in col) and col.count(0) == 2:
      x1 += 1
    if (-1 in col) and col.count(0) == 2:
      o1 += 1

  for diag in diagonals:
    if diag.count(1) == 2 and diag.count(0) == 1:
      x2 += 1
    if diag.count(-1) == 2 and diag.count(0) == 1:
      o2 += 1
    if (1 in diag) and diag.count(0) == 2:
      x1 += 1
    if (-1 in diag) and diag.count(0) == 2:
      o1 += 1

  eval = (3 * x2 + x1) - (3 * o2 + o1)
  
  # checks if position is a win
  if xWinCheck(board):
    eval += 100
  elif oWinCheck(board):
    eval += -100
    
  return eval