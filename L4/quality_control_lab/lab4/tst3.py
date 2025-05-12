import pytest
from connect_four import init_field, drop_token

def test_drop_token_valid():
    field, _ = init_field(rows=3, columns=3)
    drop_token(field, 0, True)
    assert field[0][0] == 'x'
    drop_token(field, 0, False)
    assert field[0][1] == 'o'

def test_drop_token_full_column():
    field, _ = init_field(rows=1, columns=1)
    drop_token(field, 0, True)
    with pytest.raises(ValueError):
        drop_token(field, 0, False)

def test_drop_token_invalid_column():
    field, _ = init_field()
    with pytest.raises(ValueError):
        drop_token(field, -1, True)
    with pytest.raises(ValueError):
        drop_token(field, 7, True)