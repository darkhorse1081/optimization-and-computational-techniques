from pprint import pprint
n_rows_ = 6
n_columns_ = 7

def init_field(rows=n_rows_, columns=n_columns_):
    
    field = [['.' for y in range(columns)] for x in range(rows)]
    tokens = {True: 'x', False: 'o'}
    return field, tokens

def drop_token(field, col, player, symbol={True: 'x', False: 'o'}):

    for i in range(n_rows_-1,-1,-1):
        if field[i][col] == '.' and i == n_rows_-1:
            field[i][col] = symbol.get(player)
            break
        elif field[i][col] != '.' and field[i-1][col] == '.':
            field[i-1][col] = symbol.get(player)
            break

def game_is_won(field, void='.'):

    for r in range(n_rows_-4, n_rows_): #vertical
        for c in range(n_columns_):
            if field[r][c] != void and field[r][c] == field[r-1][c] == field[r-2][c] == field[r-3][c] :
                return True

    for r in range(n_rows_): #horiz
        for c in range(n_columns_-3):
            if field[r][c] != void and field[r][c] == field[r][c+1] == field[r][c+2] == field[r][c+3]:
                return True

    for r in range(n_rows_-3,n_rows_): #NE
        for c in range(n_columns_-3):
            if field[r][c] != void and field[r][c] == field[r-1][c+1] == field[r-2][c+2] == field[r-3][c+3]:
                return True

    for r in range(n_rows_-3,n_rows_): #NW
        for c in range(n_columns_-4,n_columns_):
            if field[r][c] != void and field[r][c] == field[r-1][c-1] == field[r-2][c-2] == field[r-3][c-3]:
                return True

    return False

def play(field, tokens):

    username1 = input("Please enter your name, player 1: ")
    username2 = input("Please enter your name, player 2: ")

    while(username2 == username1):
         username2 = input("please pick a different name for player 2: ")

    player = {username1:True, username2:False}

    active_player = username1
    while(not game_is_won(field, void='.')):

        col = int(input(f"Player {active_player}, please enter your column between 0 to 6: "))
        while((col < 0) or (col >= n_columns_ ) or (field[0][col] != '.')):
            col = int(input(f"Player {active_player}, please try again entering between 0 to 6 or column that has not been filled: "))

        drop_token(field,col,player.get(active_player),tokens)
        pprint(field)

        sys_clock = 0
        for i in range(n_columns_):
            if field[0][i] == '.':
                sys_clock += 1

        if(not game_is_won(field, void='.')) and (sys_clock == 0): # indicates game has been drawn
            winner = 'null'
            break

        if active_player == username1:
            active_player = username2
        else:
            active_player = username1

    if active_player == username1:
        active_player = username2
    else:
        active_player = username1

    winner = active_player
    return winner 

if __name__ == "__main__":
    field, tokens = init_field()
    pprint(field)
    winner = play(field, tokens)
    print(f"Player {winner} wins the game. Congratulations!")







