import pytest
from gol import Cell


@pytest.fixture
def live_cell():
    """returns a live cell with no neighbours"""
    return Cell(alive=True)


def test_given_a_live_cell_with_fewer_than_two_neighbours_when_tick_is_called_dies(live_cell):
    live_cell.living_neighbours = 1
    assert live_cell.will_i_live() is False


def test_given_a_live_cell_with_greater_than_three_neighbours_when_tick_is_called_dies(live_cell):
    live_cell.living_neighbours = 4
    assert live_cell.will_i_live() is False


def test_given_a_live_cell_with_two_or_three_neighbours_when_tick_is_called_remains_alive(live_cell):
    live_cell.living_neighbours = 3
    assert live_cell.will_i_live() is True
    live_cell.living_neighbours = 2
    assert live_cell.will_i_live() is True



