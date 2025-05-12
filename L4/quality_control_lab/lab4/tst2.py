# tests/test_init_field.py
# field initialisation testing
import pytest
from connect_four import game_is_won

def vertical():
    field = init_field()
    # default Connect-4 is 6 rows × 7 cols
    assert len(field) == 6
    assert all(len(row) == 7 for row in field)
    assert all(cell is None for row in field for cell in row)

def horizontal():
    field = init_field(rows=4, cols=4)
    assert len(field) == 4
    assert all(len(row) == 4 for row in field)

def NE():
    with pytest.raises(ValueError):
        init_field(rows=0, cols=7)
    with pytest.raises(TypeError):
        init_field(rows="six", cols=7)

def NW():
    with pytest.raises(ValueError):
        init_field(rows=0, cols=7)
    with pytest.raises(TypeError):
        init_field(rows="six", cols=7)