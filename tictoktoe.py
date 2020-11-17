#global vaiables

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

#is the game still going on
game_still_going = True
#defining the global variable winner
winner = None
#defining the current player
current_player = "X"

def display_board():
  print(board[0] + "|" + board[1] + "|" + board[2])
  print(board[3] + "|" + board[4] + "|" + board[5])
  print(board[6] + "|" + board[7] + "|" + board[8])

def play_game():
  global game_still_going 
  global winner

  #display the board
  display_board()
  
  while game_still_going:
    #handling the single turn of an orbitory input1
    handle_turn(current_player)
    #checking the status of the game
    check_if_game_over()
    #flip to another player
    flip_player()

  #the game has ended
  if winner =="X" or winner =="O":
    print(winner + 'Won.')
  elif winner == None:
    print("Tie.")


def handle_turn(player):
  print(player + "'s turn,")
  position = input("Select the position from 1 to 9:")
  valid = False
  while not valid: 
    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Invalid Input, Select the position again from 1 to 9:")
      position = int(position)-1 #type casting the string
      if board[position] == "-":
        valid = True
      else:
        print("you can't go there again") 
      board[position]= "X"
      display_board()

def check_if_game_over():
  check_if_win()

  check_if_tie()

def check_if_win():
  global winner 
  #check diagonals
  diagonal_winner = check_diagonals()
  #check rows
  row_winner = check_rows()
  #check colomns
  colomn_winner = check_colomns()

  if row_winner:
    #there is a winner
    winner = row_winner()
  elif colomn_winner:
    #there is a winner
    winner = colomn_winner()
  elif diagonal_winner:
    #there is a winner
    winner = diagonal_winner()
  else:
    #there is a tie    
    winner = None 
  return

def check_rows():
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]    
  return

def check_colomns():
  global game_still_going
  colomn_1 = board[0] == board[3] == board[6] != "-"
  colomn_2 = board[1] == board[4] == board[7] != "-"
  colomn_3 = board[2] == board[6] == board[8] != "-"

  if colomn_1 or colomn_2 or colomn_3:
    game_still_going = False
  if colomn_1:
    return board[0]
  elif colomn_2:
    return board[1]
  elif colomn_3:
    return board[2]    
  return


def check_diagonals():
  global game_still_going
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"

  if diagonal_1 or diagonal_2:
    game_still_going = False
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[6]
  return

def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return

def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"  
  
  return


play_game()

