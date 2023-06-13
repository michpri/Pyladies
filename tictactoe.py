def evaluate(board):
 #returns one character based on the game state

  if "xxx" in board:
      return "x"
  elif "ooo" in board:
      return "o"
  elif "-" not in board:
      return "!"
  else:
      return "-"

def player_move(board, player_mark):
  while True:
      try:
          #Note: I had too google try-except to fix the error where user enters varchar instead of int
          position = int(input('Choose a position between 0 and 19 to place your mark: '))
          if position < 0 or position > 19:
              print('Invalid position, enter a number between 0 and 19.')                
          elif board[position] != '-':
              print('Sorry, this position is already taken.')
          else:
              break
      except ValueError:
          print('Please enter numbers between 0 and 19 only.')
  board = board[:position] + player_mark + board[position+1:]
  print(board)
  return board

def computer_move(board, computer_mark):
  from random import randrange
  position = randrange(0, 19)
  while board[position] != '-':
      position = randrange(0, 19)
  board = board[:position] + computer_mark + board[position+1:]
  print(board)
  return board

def tictactoe():
  board = "--------------------"
  
  while True:
      player_mark = input('Choose your mark (x or o):')
      if player_mark == 'x' or player_mark == 'o':
          print('Thanks!')
          break
      print('Incorrect, enter only x or o.')
  if player_mark == 'x':
     computer_mark = "o"
  else:
      computer_mark = 'x'

  while True:
      # player's move
      board = player_move(board, player_mark)
      result = evaluate(board)
      if result == "x":
          print(board)
          print('The mark X wins!')
          break
      elif result == "o":
          print(board)
          print('The mark O wins!')
          break
      elif result == "!":
          print(board)
          print('Draw!')
          break                 

      # computer's move
      board = computer_move(board, computer_mark)
      result = evaluate(board)
      if result == "x":
          print(board)
          print('The mark X wins!')
          break
      elif result == "o":
          print(board)
          print('The mark O wins!')
          break
      elif result == "!":
          print(board)
          print('Draw!')
          break

tictactoe()