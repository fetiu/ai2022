import random
 
def select_letter():
   let = ""
   auto_let = ""
   while (let != "x" and let != "o"):
       let = input("Select X or O: ").replace(" ", "").strip().lower()
       if let == "x":
           auto_let = "o"
       else:
           auto_let = "x"
   return let, auto_let
 
 
def clean_board():
 
   brd = [" " for x in range(10)]
   return brd
 
 
def is_board_full(board):
   return board.count(" ") == 0
 
 
def insert_letter(board, letter, pos):
   board[pos] = letter
 
 
def computer_move(board, letter):
   computer_letter = letter
   possible_moves = []
   available_corners = []
   available_edges = []
   available_center = []
   position = -1
 
   for i in range(1, len(board)):
       if board[i] == " ":
           possible_moves.append(i)
 
   for let in ["x", "o"]:
       for i in possible_moves:
           board_copy = board[:]
           board_copy[i] = let
           if is_winner(board_copy, let):
               position = i
 
   if position == -1:
       for i in range(len(board)):
 
           if board[i] == " ":
               if i in [1, 3, 7, 9]:
                   available_corners.append(i)
               if i is 5:
                   available_center.append(i)
               if i in [2, 4, 6, 8]:
                   available_edges.append(i)
       # check corners first
       if len(available_corners) > 0:
           print("it comes here")
           # select a random position in the corners
           position = random.choice(available_corners)
       # then check the availability of the center
       elif len(available_center) > 0:
           # select the center as the position
           position = available_center[0]
       # lastly, check the availability of the edges
       elif len(available_edges) > 0:
           # select a random position in the edges
           position = random.choice(available_edges)
   # fill the position with the letter
   board[position] = computer_letter
 
 
def draw_board(board):
   board[0] = -1
   print("   |   |   ")
   print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
   print("   |   |   ")
   print("-"*11)
   print("   |   |   ")
   print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
   print("   |   |   ")
   print("-"*11)
   print("   |   |   ")
   print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
   print("   |   |   ")
   print("-"*11)
   return board
 
 
def is_winner(board, letter):
   return (board[1] == letter and board[2] == letter and board[3] == letter) or \
       (board[4] == letter and board[5] == letter and board[6] == letter) or \
       (board[7] == letter and board[8] == letter and board[9] == letter) or \
       (board[1] == letter and board[4] == letter and board[7] == letter) or \
       (board[2] == letter and board[5] == letter and board[8] == letter) or \
       (board[3] == letter and board[6] == letter and board[9] == letter) or \
       (board[1] == letter and board[5] == letter and board[9] == letter) or \
       (board[3] == letter and board[5] == letter and board[7] == letter)
 
 
def repeat_game():
 
   repeat = input("Play again? Press y for yes and n for no: ")
   while repeat != "n" and repeat != "y":
       repeat = input("PLEASE, press y for yes and n for no: ")
   return repeat
 
 
def play_game():
 
   letter, auto_letter = select_letter()
 
   board = clean_board()
   board = draw_board(board)
 
   while is_board_full(board) == False:
       try:
           position = int(
               input("Select a position (1-9) to place an "+letter+" : "))
 
       except:
           position = int(
               input("PLEASE enter position using only NUMBERS from 1-9: "))
 
       if position not in range(1, 10):
           position = int(
               input("Please, choose another position to place an "+letter+" from 1 to 9 :"))
 
       if board[position] != " ":
           position = int(
               input("Please, choose an empty position to place an "+letter+" from 1 to 9: "))
 
       insert_letter(board, letter, position)
       computer_move(board, auto_letter)
 
       board = draw_board(board)
 
       if is_winner(board, letter):
           print("Congratulations! You Won.")
           return repeat_game()
       elif is_winner(board, auto_letter):
           print("Hard Luck! Computer won")
           return repeat_game()
 
   if is_board_full(board):
       print("Tie Game :)")
       return repeat_game()
 
 
print("Welcome to Tic Tac Toe.")
repeat = "y"
while (repeat == "y"):
   repeat = play_game()