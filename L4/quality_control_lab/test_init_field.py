import pytest
from connect_four import init_field

def test_init_field_default():
    field, tokens = init_field()
    assert len(field) == 7
    assert all(len(col) == 6 for col in field)
    assert all(cell == '.' for col in field for cell in col)
    assert len(tokens) == 7
    assert all(t == 0 for t in tokens)

def test_init_field_custom():
    field, tokens = init_field(rows=3, columns=4)
    assert len(field) == 4
    assert all(len(col) == 3 for col in field)
    assert len(tokens) == 4

def test_init_field_invalid():
    with pytest.raises(ValueError):
        init_field(rows=-1, columns=5)
    with pytest.raises(ValueError):
        init_field(rows=5, columns=0)