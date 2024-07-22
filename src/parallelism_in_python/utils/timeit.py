import time
from functools import wraps
from typing import Any, Awaitable, Callable

from loguru import logger


def async_timeit(function: Callable[..., Awaitable[Any]]) -> Callable[..., Awaitable[Any]]:
    """
    Decorator that measures the execution time of an asynchronous function.

    Args:
        function (Callable[..., Awaitable[Any]]): The asynchronous function to be timed.

    Returns:
        Callable[..., Awaitable[Any]]: The wrapped asynchronous function.

    """
    @wraps(function)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        start: float = time.time()
        result: Any = await function(*args, **kwargs)
        end: float = time.time()
        logger.info(f"Function {function.__name__} {args} {kwargs} took {end - start} seconds")
        return result
    return wrapper


def timeit(function: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that measures the execution time of a function.

    Args:
        function (Callable[..., Any]): The function to be timed.

    Returns:
        Callable[..., Any]: The wrapped function.

    """
    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start: float = time.time()
        result: Any = function(*args, **kwargs)
        end: float = time.time()
        logger.info(f"Function {function.__name__} {args} {kwargs} took {end - start} seconds")
        return result
    return wrapper
