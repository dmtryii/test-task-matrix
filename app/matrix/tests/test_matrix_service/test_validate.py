import pytest

from ...exceptions.matrix_exception import MatrixFormatException
from ...services.matrix_service import _validate


def test_valid_matrix():
    matrix = """
        +---+---+---+
        | 1 | 2 | 3 |
        +---+---+---+
        | 4 | 5 | 6 |
        +---+---+---+
        | 7 | 8 | 9 |
        +---+---+---+
    """
    expected_result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = _validate(matrix)
    assert result == expected_result


def test_invalid_matrix():
    matrix = """
        +---+---+---+
        | 1 | a | 3 |
        +---+---+---+
        | 4 | 5 | 6 |
        +---+---+---+
        | 7 | 8 | 9 |
        +---+---+---+
    """
    with pytest.raises(MatrixFormatException):
        _validate(matrix)
