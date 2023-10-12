game_still_going = True
current_player = "X"
winner = None

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print("---------")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("---------")
  print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
  display_board()

  while game_still_going:
    handle_turn(current_player)
    check_game_over()
    flip_player()

  if winner == "X" or winner == "O":
    print("Winner is " + winner)
  elif winner is None:
    print("Tie")


def check_game_over():
  global winner
  ans, win = check_if_win()
  ans2 = check_if_tie()
  if ans:
    winner = win


def check_if_win():
  #check rows
  global game_still_going
  if (board[0] == board[1] == board[2] != "-"):
    game_still_going = False
    return True, board[0]
  elif (board[3] == board[4] == board[5] != "-"):
    game_still_going = False
    return True, board[3]
  elif (board[6] == board[7] == board[8] != "-"):
    game_still_going = False
    return True, board[6]
  #check columns
  if (board[0] == board[3] == board[6] != "-"):
    game_still_going = False
    return True, board[0]
  elif (board[1] == board[4] == board[7] != "-"):
    game_still_going = False
    return True, board[1]
  elif (board[2] == board[5] == board[8] != "-"):
    game_still_going = False
    return True, board[2]
  #check diagonals
  if (board[0] == board[4] == board[8] != "-"):
    game_still_going = False
    return True, board[0]
  elif (board[2] == board[4] == board[6] != "-"):
    game_still_going = False
    return True, board[2]

  return False, board[0]


def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
    return True
  return False


def flip_player():
  global current_player
  current_player = "O" if current_player == "X" else "X"


def handle_turn(player):
  flag = False
  position = input("Choose a position from 1 to 9 ")
  while not flag:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    if board[position] == "-":
      flag = True
    else:
      print("position in board already occupied ,choose another position")

  board[position] = player
  display_board()


play_game()
