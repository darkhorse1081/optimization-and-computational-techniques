from pprint import pprint
n_rows_ = 6
n_columns_ = 7

def init_field(rows=n_rows_, columns=n_columns_): # test commit
    for i in rows:
        for j in columns:
            pass     


def drop_token(field, col, player, symbol={True: 'x', False: 'o'}):
    pass
        
def game_is_won(field, void='.'):
    pass


def play(field, tokens):
    pass


if __name__ == "__main__":
    field, tokens = init_field()
    pprint(field)
    winner = play(field, tokens)
    print(f"Player {winner} wins the game. Congratulations!")







