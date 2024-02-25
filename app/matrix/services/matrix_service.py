import json
from typing import List, Optional

from ..exceptions.matrix_exception import MatrixInvalidException, MatrixFormatException, MatrixTraverseException
from ..helpers import data_fetcher
from ..models import Matrix


async def _validate(matrix: str) -> List[List[int]]:
    try:
        lines = matrix.strip().split('\n')
        result_matrix = []
        for line in lines[1:-1:2]:
            row = [int(cell.strip()) for cell in line.strip().split('|')[1:-1]]
            result_matrix.append(row)
        return result_matrix
    except (ValueError, IndexError, TypeError) as e:
        raise MatrixFormatException(e)


async def _traverse_counterclockwise(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []

    result = []
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
        for j in range(top, bottom + 1):
            result.append(matrix[j][left])
        left += 1

        for i in range(left, right + 1):
            result.append(matrix[bottom][i])
        bottom -= 1

        if left <= right:
            for j in range(bottom, top - 1, -1):
                result.append(matrix[j][right])
            right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[top][i])
            top += 1

    return result


async def _save_matrix(matrix: List[List[int]]) -> None:
    matrix_data_json = json.dumps(matrix)
    current_matrix = Matrix(rows=len(matrix),
                            columns=len(matrix[0]),
                            data=matrix_data_json)
    await current_matrix.asave()


async def get_matrix(url: str) -> Optional[List[int]]:
    matrix = await data_fetcher.get_matrix(url)

    if not matrix:
        raise MatrixFormatException("Matrix not received")

    valid_matrix = await _validate(matrix)

    if not valid_matrix:
        raise MatrixInvalidException("Invalid matrix")

    await _save_matrix(valid_matrix)

    traverse_matrix = await _traverse_counterclockwise(valid_matrix)

    if not traverse_matrix:
        raise MatrixTraverseException("Impossible to make a counter-clockwise detour")

    return traverse_matrix
