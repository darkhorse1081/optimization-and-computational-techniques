from pprint import pprint
n_rows_ = 6
n_columns_ = 7

def init_field(rows=n_rows_, columns=n_columns_):
    
    field = [['.' for y in range(columns)] for x in range(rows)]
    tokens = {True: 'x', False: 'o'}
    return field, tokens

def drop_token(field, col, player, symbol={True: 'x', False: 'o'}):

    global n_rows_

    for i in field[range(n_rows_)][col]:
        if field[i+1][col] != '.':
            field[i][col] = symbol.get(player)
            
        
def game_is_won(field, void='.'):

    # returns bool
    global n_rows_, n_columns_

    r = n_rows_
    c = n_columns_

    for i in range(r): #vertical
        for j in range(c):
            if field[r][c] != void and field[r][c] == field[r+1][c] == field[r+2][c] == field[r+3][c]:
                return True

    for i in range(n_rows_): #horiz
        for j in range(n_columns_):
            if field[r][c] != void and field[r][c] == field[r][c+1] == field[r][c+2] == field[r][c+3]:
                return True

    for i in range(n_rows_): #NE
        for j in range(n_columns_):
            if field[r][c] != void and field[r][c] == field[r-1][c+1] == field[r-2][c+2] == field[r-3][c+3]:
                return True

    for i in range(n_rows_): #NW
        for j in range(n_columns_):
            if field[r][c] != void and field[r][c] == field[r-1][c-1] == field[r-1][c-1] == field[r-1][c-1]:
                return True

    return False

def play(field, tokens):

    while(not game_is_won(field, void='.')):
          pass


if __name__ == "__main__":
    field, tokens = init_field()
    pprint(field)
    winner = play(field, tokens)
    print(f"Player {winner} wins the game. Congratulations!")







