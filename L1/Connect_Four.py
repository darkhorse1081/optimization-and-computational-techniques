from pprint import pprint
n_rows_ = 6
n_columns_ = 7

def init_field(rows=n_rows_, columns=n_columns_):

    field = [['.' for y in range(columns)] for x in range(rows)]
    return field



def drop_token(field, col, player, symbol={True: 'x', False: 'o'}):
    pass
        
def game_is_won(field, void='.'):
    pass


def play(field, tokens):
    pass


if __name__ == "__main__":
    # field, tokens = init_field()
    field= init_field()
    pprint(field)
    winner = play(field, tokens)
    print(f"Player {winner} wins the game. Congratulations!")







