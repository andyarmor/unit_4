def print_board():
    print()
    board = [[1,2,3], [4,5,6], [7,8,9]]
    row_count = 1
    for row in board:
        row_string = ""
        for i in range(0,3):
            if i < 2:
                row_string += str(row[i]) + " |"
            else:
                row_string +=str(row[i])
        if row_count < 4: 
            print(row_string)
            print('--------')
            row_count +=1
        else:
            print(row_count)
        
turn = 1
player_symbol = ""
print_board()
