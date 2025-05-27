from connect_four import init_field, drop_token, game_is_won

def test_horizontal_win():
    field, _ = init_field(rows=6, columns=7)
    for col in range(4):
        drop_token(field, col, True)
    assert game_is_won(field) == True

def test_vertical_win():
    field, _ = init_field()
    for _ in range(4):
        drop_token(field, 0, True)
    assert game_is_won(field) == True

def test_diagonal_win():
    field, _ = init_field()
    for i in range(4):
        for _ in range(i):
            drop_token(field, i, False)
        drop_token(field, i, True)
    assert game_is_won(field) == True

def test_draw():
    field, _ = init_field(rows=1, columns=1)
    drop_token(field, 0, True)
    assert game_is_won(field) == 'nobody'

