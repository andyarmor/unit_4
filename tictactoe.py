board = [['','',''], ['','',''], ['', '', '']]
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
            print('------')
            row_count +=1
        else:
            print(row_string)
 
def make_move(name, symbol):
    valid_move = False
    while not valid_move:
        print(f"{name}, where would you like your marker?")
        player_column = int(input(" Enter a column 1-3: "))
        player_row = int(input(" Enter a row 1-3: "))
        if board[player_row -1][player_column-1] == '':
            board[player_row -1][player_column-1] = symbol
            valid_move = True
        if not valid_move:
            print("Not a valid move, pick somewhere else")

def end_game(board):

    game_winner = ''
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            game_winner = board[i][0]
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            game_winner = board[0][0]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        game_winner = board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        game_winner = board[0][2]
    return game_winner


def reset_board():
    global board
    board = [['','',''], ['','',''], ['', '', '']]
    print_board()

def checkTied(board):
    
    pass


    

    

while Playing:

    print("The current gameboard is: ")
    print_board()

    make_move(player_1, player_1_symbol)
    print("The current gameboard is: ")
    print_board()
    winner = end_game(board)
    if winner != '':
        print(f"{winner} has won the game! ")
        break

    gameTied = checkTied(board)

    make_move(player_2, player_2_symbol)
    print("The current gameboard is: ")
    print_board()
    winner = end_game(board) 
    if winner != '':
        print(f"{winner} has won the game! ")
        break

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

