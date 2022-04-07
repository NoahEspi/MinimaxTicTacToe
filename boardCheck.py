def fullBoardCheck(board):
  
  for c in board:
    if 0 in c:
      return False

  return True

def xWinCheck(board):
  
  # checks row tictactoes 
  for r in board:
    if sum(r) == 3:
      return True

  # checks diagonals 
  if board[0][0] + board[1][1] + board[2][2] == 3:
    return True
  elif board[0][2] + board[1][1] + board[2][0] == 3:
    return True

  # checks columns 
  for c in range(3):
    if board[0][c] + board[1][c] + board[2][c] == 3:
      return True

  return False

def oWinCheck(board):

  # checks row tictactoes
  for r in board:
    if sum(r) == -3:
      return True

  # checks diagonals
  if board[0][0] + board[1][1] + board[2][2] == -3:
    return True
  elif board[0][2] + board[1][1] + board[2][0] == -3:
    return True

  # checks columns
  for c in range(3):
    if board[0][c] + board[1][c] + board[2][c] == -3:
      return True

  return False