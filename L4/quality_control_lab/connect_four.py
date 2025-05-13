from pprint import pprint

n_rows_ = 6
n_columns_ = 7

def init_field(rows=n_rows_, columns=n_columns_):
    if rows <= 0 or columns <= 0:
        raise ValueError("Rows and columns must be positive integers.")
    tokens = [0] * columns
    field = []
    for _ in range(columns):
        field.append(['.'] * rows)
    return field, tokens

def drop_token(field, col, player, symbol=None):
    if symbol is None:
        symbol = {True: 'x', False: 'o'}
    if col < 0 or col >= len(field):
        raise ValueError(f"Column {col} is invalid.")
    column = field[col]
    for row in range(len(column)):
        if column[row] == '.':
            column[row] = symbol[player]
            break
    else:
        raise ValueError(f"Column {col} is full.")
    # Display the field correctly
    rows_display = []
    for r in range(len(column)):
        current_row = [field[c][r] for c in range(len(field))]
        rows_display.append(current_row)
    rows_display.reverse()
    pprint(rows_display)

def game_is_won(field, void='.'):
    has_won = False
    N_cols = len(field)
    N_rows_in_col = len(field[0]) if N_cols > 0 else 0
    # Check horizontal, vertical, and diagonals
    for col in range(N_cols):
        for row in range(N_rows_in_col):
            if field[col][row] == void:
                continue
            # Horizontal check (four consecutive columns in the same row)
            if col <= N_cols - 4:
                if all(field[col + i][row] == field[col][row] for i in range(4)):
                    has_won = True
                    break
            # Vertical check (four consecutive rows in the same column)
            if row <= N_rows_in_col - 4:
                if all(field[col][row + i] == field[col][row] for i in range(4)):
                    has_won = True
                    break
            # Diagonal bottom-left to top-right
            if col <= N_cols - 4 and row <= N_rows_in_col - 4:
                if all(field[col + i][row + i] == field[col][row] for i in range(4)):
                    has_won = True
                    break
            # Diagonal top-left to bottom-right
            if col <= N_cols - 4 and row >= 3:
                if all(field[col + i][row - i] == field[col][row] for i in range(4)):
                    has_won = True
                    break
        if has_won:
            break
    # Check for draw (all columns full)
    if not has_won:
        all_full = True
        for col in field:
            if '.' in col:
                all_full = False
                break
        if all_full:
            return 'nobody'
    return has_won

def play(field, tokens):
    is_player_1 = True
    players = {True: 1, False: 2}
    while True:
        result = game_is_won(field)
        if result:
            break
        correct_input = False
        player = players[is_player_1]
        while not correct_input:
            try:
                col = int(input(f"Player {player}, choose column [0-{len(tokens)-1}]: "))
                if 0 <= col < len(tokens):
                    if tokens[col] < len(field[col]):
                        drop_token(field, col, is_player_1)
                        tokens[col] += 1
                        is_player_1 = not is_player_1
                        correct_input = True
                    else:
                        print("Column full. Try another.")
                else:
                    print(f"Column must be 0-{len(tokens)-1}.")
            except ValueError:
                print("Invalid input. Enter a column number.")
    if result == 'nobody':
        print("Game over. It's a draw!")
        return None
    else:
        winner = 2 if is_player_1 else 1
        print(f"Player {winner} wins!")
        return winner

if __name__ == "__main__":
    field, tokens = init_field()
    play(field, tokens)