import aiohttp

from ..exceptions.matrix_exception import RequestException


async def get_matrix(url: str) -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()
    except aiohttp.ClientResponseError as e:
        raise RequestException(f"Client response error: {e}") from e
    except aiohttp.ClientError as e:
        raise RequestException(f"Client error: {e}") from e
    except aiohttp.ServerError as e:
        raise RequestException(f"Server error: {e}") from e
    except Exception as e:
        raise RequestException(f"An error occurred: {e}") from e
