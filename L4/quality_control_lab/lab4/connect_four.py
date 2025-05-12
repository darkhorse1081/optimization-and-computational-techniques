"""
Textual interface for playing Connect Four with two players.
"""
from pprint import pprint

n_rows_ = 6
n_columns_ = 7

def init_field(rows=n_rows_, columns=n_columns_):
    """
    Intialize field

    :param rows: number of rows
    :param columns: number of columns
    :return: list of lists
    """
    tokens = [0] * columns
    field = list()
    for i in range(columns):
        field.append(['.'] * rows)
    return field, tokens

def drop_token(field, col, player, symbol={True: 'x', False: 'o'}):
    """
    Modify field with player's choice to drop a token into a specific column

    :param field: Two-dimensional object
    :param col: Column to drop token to
    :param player: Player, whose token is dropped
    :param symbol: dictionary mapping player to token symbol. True refers to player 1, False to player 2 (not player 1).
    :return: None
    """

    field.reverse()
    for row in field:
        if row[col] == '.':
            row[col] = symbol.get(player)
            break
    field.reverse()
    pprint(field)

def game_is_won(field, void='.'):
    """
    Test if field indicates that one of the players has won the game.

    :param field: Double indexed object
    :return: bool
    """
    has_won = False
    field.reverse()
    N_rows = len(field)
    N_columns = len(field[0])
    for i in range(N_rows):
        for j in range(N_columns):
            if field[i][j] != void:
                # horizontal
                if j <= n_columns_ - 5 and field[i][j] == field[i][j+1] == field[i][j+2] == field[i][j+3]:
                    has_won = True
                    break
                # vertical
                if i <= n_rows_ - 5 and field[i][j] == field[i+1][j] == field[i+2][j] == field[i+3][j]:
                    has_won = True
                    break
                # diagonal bottom left to top right
                if (j <= n_columns_ - 5 and i <= n_rows_ - 5 and
                        field[i][j] == field[i+1][j+1] == field[i+2][j+2] == field[i+3][j+3]):
                    has_won = True
                    break
            # diagonal top left to bottom right
            if (j <= n_columns_ - 5 and i <= n_rows_ - 5 and field[i+3][j] != void and
                    field[i+3][j] == field[i + 2][j + 1] == field[i + 1][j + 2] == field[i][j + 3]):
                has_won = True
                break
    field.reverse()
    if sum([field[N_rows - 1][j] != void for j in range(N_columns)]) == N_columns:  # trivial draw, all columns full
        has_won = 'nobody'
    return has_won

def play(field, tokens):
    """
    Play connect four starting with an intialised field and a corresponding list of token numbers per column.

    :param field: Object with two indexable dimensions
    :param tokens: List of token numbers per row
    :return: Winner of the game
    """
    is_player_1 = True
    players = {True: 1,
               False: 2}
    while not game_is_won(field):
        correct_input = False
        player = players[is_player_1]
        while not correct_input:
            col = int(input(f"Make your move player {player}. Select your column [0-6]: "))

            if col >= 0 and col < len(tokens):
                if tokens[col] < len(field):
                    drop_token(field, col, is_player_1)
                    tokens[col] += 1
                    is_player_1 = not is_player_1
                    correct_input = True
                else:
                    print(f"Column {col} is already full. Try again.")
            else:
                print(f"The column number needs to be between 0 and {n_columns_-1}. Try again.")
    if is_player_1:
        winner = 2
    else:
        winner = 1
    return winner

if __name__ == "__main__":
    field, tokens = init_field()
    pprint(field)
    winner = play(field, tokens)
    print(f"Player {winner} wins the game. Congratulations!")