from pprint import pprint
n_rows_ = 6
n_columns_ = 7
username1 = True
active_player = username1
username2 = False

def init_field(rows=n_rows_, columns=n_columns_):
    
    field = [['.' for y in range(columns)] for x in range(rows)]
    tokens = {True: 'x', False: 'o'}
    return field, tokens

def drop_token(field, col, player, symbol={True: 'x', False: 'o'}):

    global n_rows_

    for i in range(n_rows_-1,-1,-1):
        if field[i][col] == '.' and i == n_rows_-1:
            field[i][col] = symbol.get(player)
            break
        elif field[i][col] != '.' and field[i-1][col] == '.':
            field[i-1][col] = symbol.get(player)
            break
     
def game_is_won(field, void='.'):

    # returns bool
    global n_rows_, n_columns_

    for r in range(n_rows_): #vertical
        for c in range(n_columns_):
            if (r-3 >= n_rows_-n_rows_):
                if field[r][c] != void and field[r][c] == field[r-1][c] == field[r-2][c] == field[r-3][c] :
                    return True

    for r in range(n_rows_): #horiz
        for c in range(n_columns_):
            if c+3 < n_columns_:
                if field[r][c] != void and field[r][c] == field[r][c+1] == field[r][c+2] == field[r][c+3]:
                    return True

    for r in range(n_rows_): #NE
        for c in range(n_columns_):
            if (r-3 >= n_rows_-n_rows_) and (c+3 < n_columns_):
                if (field[r][c] != void and field[r][c] == field[r-1][c+1] == field[r-2][c+2] == field[r-3][c+3] 
                and r-3 < n_rows_ and c+3 < n_columns_):
                    return True

    for r in range(n_rows_): #NW
        for c in range(n_columns_):
            if (r-3 >= n_rows_-n_rows_) and (c-3 >= n_columns_-n_columns_):
                if (field[r][c] != void and field[r][c] == field[r-1][c-1] == field[r-1][c-1] == field[r-1][c-1]
                    and c-3 < n_columns_):
                    return True

    return False

def switch_player():
    global active_player
    if active_player == username1:
        active_player = username2
    else:
        active_player = username1

def play(field, tokens):

    global n_columns_
    username1 = input("Please enter your name, player 1: ")
    username2 = input("Please enter your name, player 2: ")
    player = {username1:True, username2:False}

    active_player = username1
    while(not game_is_won(field, void='.')):

        col = int(input(f"Player {active_player}, please enter your column between 0 to 6: "))
        while((col < 0) or (col >= n_columns_ )):
            col = int(input(f"Player {active_player}, please try again entering between 0 to 6: "))
        drop_token(field,col,player.get(active_player),tokens)
        pprint(field)
        switch_player()

    switch_player()
    winner = active_player
    return winner 

if __name__ == "__main__":
    field, tokens = init_field()
    pprint(field)
    winner = play(field, tokens)
    print(f"Player {winner} wins the game. Congratulations!")







