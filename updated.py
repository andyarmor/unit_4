board = [[' ',' ',' '], [' ',' ',' '], [' ', ' ', ' ']]
player_1 = input("Player 1, what is your name? ")
player_2 = input("Player 2, what is your name? ")
player_1_symbol = 'X'
player_2_symbol = 'O'
gamecount = 0
player_symbol = ""
winner = ''
gameTied = False
Playing = True

def print_board():
    print()
    row_count = 1
    for row in board:
        
        row_string = ""
        for i in range(0,3):
            if i < 2:
                row_string += str(row[i]) + " |"
            else:
                row_string +=str(row[i])
        if row_count < 3: 
            print(row_string)
            print('--------')
            row_count +=1
        else:
            print(row_string)
 
def make_move(name, symbol):
    valid_move = False
    while not valid_move:
        print(f"{name}, where would you like your marker?")
        player_column = int(input(" Enter a column 1-3: "))
        player_row = int(input(" Enter a row 1-3: "))
        if board[player_row -1][player_column-1] == ' ':
            board[player_row -1][player_column-1] = symbol
            valid_move = True
        if not valid_move:
            print("Not a valid move, pick somewhere else")

def player_winner(pl_symbol):
    if pl_symbol == 'X':
        print(f"Congrats {player_1}!")
    else:
        print(f"Congrats {player_2}!")

def end_game(board):

    #horizontal win
    global playing
    for row in board:
        if row[0] == row[1] == row[2]:
            player_winner(row[0])
            playing = False
    #vertical win
    if board[0][0] == board[1][0] == board[2][0]:
        player_winner(row[0])
        playing =False
    elif board[0][1] == board[1][1] == board[2][1]:
        player_winner(row[0])
        playing = False
    elif board[0][2] == board[1][2] == board[2][2]:
        player_winner(row[0])
        playing = False
    #diagonal win
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        player_winner(row[0])
        playing = False

    #full board for tie?

def reset_board():
    global board
    board = [[' ',' ',' '], [' ',' ',' '], [' ', ' ', ' ']]
    print_board()

def checkTied(board):
    
    pass


    

    

while Playing:

    print("The current gameboard is: ")
    print_board()

    make_move(player_1, player_1_symbol)
    print("The current gameboard is: ")
    print_board()

    gameTied = checkTied(board)

    make_move(player_2, player_2_symbol)
    print("The current gameboard is: ")
    print_board()

    gameTied = checkTied(board)

    

while True:
    user_input = input("Would you like to play again? (y/n)")
    if user_input == 'y':
        print("Playing again...")
        reset_board()
        break
    elif user_input == 'n':
        print("See you later")
        playing = False
        break