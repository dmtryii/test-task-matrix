from app.matrix.services.matrix_service import _traverse_counterclockwise


def test_traverse_counterclockwise_regular_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected_result = [1, 4, 7, 8, 9, 6, 3, 2, 5]
    result = _traverse_counterclockwise(matrix)
    assert result == expected_result


def test_traverse_counterclockwise_empty_matrix():
    matrix = []
    result = _traverse_counterclockwise(matrix)
    assert result == []


def test_traverse_counterclockwise_single_row_matrix():
    matrix = [[1, 2, 3, 4]]
    expected_result = [1, 2, 3, 4]
    result = _traverse_counterclockwise(matrix)
    assert result == expected_result


def test_traverse_counterclockwise_single_column_matrix():
    matrix = [[1], [2], [3], [4]]
    expected_result = [1, 2, 3, 4]
    result = _traverse_counterclockwise(matrix)
    assert result == expected_result
