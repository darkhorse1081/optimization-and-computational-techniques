"""
Textual interface for playing Connect Four with two players. """
from pprint import pprint
n_rows_ = 6
n_columns_ = 7

def init_field(rows=n_rows_, columns=n_columns_): # test commit
    """
    Intialize field
    :param rows: number of rows :param columns: number of columns :return: list of lists
    """

def drop_token(field, col, player, symbol={True: 'x', False: 'o'}): 
    """
    Modify field with player's choice to drop a token into a specific column
    :param field: Two-dimensional object
    :param col: Column to drop token to
    :param player: Player, whose token is dropped
    :param symbol: dictionary mapping player to token symbol. True refers to player 1,
    False to player 2 (not player 1). :return: None
    """
        
def game_is_won(field, void='.'): 
    """
    Test if field indicates that one of the players has won the game.
    :param field: Double indexed object :return: bool
    """


def play(field, tokens): 
    """
    Play connect four starting with an intialised field and a corresponding list of ,→ token numbers per column.
    :param field: Object with two indexable dimensions
    :param tokens: List of token numbers per column
    :return: Winner of the game 
    """


if __name__ == "__main__":
    field, tokens = init_field()
    pprint(field)
    winner = play(field, tokens)
    print(f"Player {winner} wins the game. Congratulations!")







