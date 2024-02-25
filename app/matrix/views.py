from ninja import NinjaAPI

from .exceptions.matrix_exception import MatrixInvalidException, MatrixFormatException, MatrixTraverseException, \
    RequestException
from .services import matrix_service

api = NinjaAPI()


@api.post('/')
async def start(request, api_url: str):
    result = await matrix_service.get_matrix(api_url)
    return {'result': result}


@api.exception_handler(RequestException)
def matrix_invalid_exception_handler(request, exc):
    return api.create_response(
        request,
        {"message": exc.message},
        status=400,
    )


@api.exception_handler(MatrixInvalidException)
def matrix_invalid_exception_handler(request, exc):
    return api.create_response(
        request,
        {"message": exc.message},
        status=400,
    )


@api.exception_handler(MatrixFormatException)
def matrix_format_exception_handler(request, exc):
    return api.create_response(
        request,
        {"message": exc.message},
        status=400,
    )


@api.exception_handler(MatrixTraverseException)
def matrix_traverse_exception_handler(request, exc):
    return api.create_response(
        request,
        {"message": exc.message},
        status=500,
    )
