from pprint import pprint
n_rows_ = 6
n_columns_ = 7

def init_field(rows=n_rows_, columns=n_columns_):
    
    field = [['.' for y in range(columns)] for x in range(rows)]
    return field

def drop_token(field, col, player, symbol={True: 'x', False: 'o'}):

    global n_rows_

    if player == True:
        field[n_rows_-1][col] = symbol.get(player)
    else:
        field[n_rows_-1][col] = symbol.get(player)
        
def game_is_won(field, void='.'):

    # returns bool
    global n_rows_, n_columns_

    result = False

    # result = [[True for y in range(n_columns_) if condition...] for x in range(n_rows_)]

    for i in range(n_rows_):
        for j in range(n_columns_):
            if # condition:
            result = True
            break
        if result == True
        break

    for i in range(n_rows_):
        for j in range(n_columns_):
            if # condition:
            result = True
            break
        if result == True
        break

    for i in range(n_rows_):
        for j in range(n_columns_):
            if # condition:
            result = True
            break
        if result == True
        break

    for i in range(n_rows_):
        for j in range(n_columns_):
            if # condition:
            result = True
            break
        if result == True
        break

    return result

    pass


def play(field, tokens):

    while(not game_is_won):
          
    pass


if __name__ == "__main__":
    field, tokens = init_field()
    pprint(field)
    winner = play(field, tokens)
    print(f"Player {winner} wins the game. Congratulations!")







