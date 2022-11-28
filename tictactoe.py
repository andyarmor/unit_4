board = [[' ',' ',' '], [' ',' ',' '], [' ', ' ', ' ']]
player_1 = input("Player 1, what is your name? ")
player_1_symbol = 'X'
player_2 = input("Player 2, what is your name? ")
player_2_symbol = 'O'
gamecount = 0
player_symbol = ""
winner = ""

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

def check_tied(board):

    pass
        
def make_move(board, name, symbol):
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



def check_winner(board):

    winner = ''

    #check the rows and collumns for win
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            winner = board[i][0]
        elif board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            winner = board[0][i]
        
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        winner = board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board [2][0]:
        winner = board[0][2]
    return winner

    

while True:
    print("The current gameboard is: ")
    print_board()

    make_move(board, player_1, player_1_symbol)

    make_move(board, player_2, player_2_symbol)

    winner = check_winner(board)