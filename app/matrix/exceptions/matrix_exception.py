

class MatrixInvalidException(Exception):
    def __init__(self, message):
        super().__init__(message)


class MatrixFormatException(Exception):
    def __init__(self, message):
        super().__init__(message)


class MatrixTraverseException(Exception):
    def __init__(self, message):
        super().__init__(message)


class RequestException(Exception):
    def __init__(self, message):
        super().__init__(message)
