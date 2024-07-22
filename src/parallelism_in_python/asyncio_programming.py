import asyncio
from typing import Awaitable

import httpx
from loguru import logger

from parallelism_in_python.utils.timeit import async_timeit
from parallelism_in_python.utils.urls import generate_url


@async_timeit
async def download_url(url: str) -> httpx.Response:
    """
    Downloads the content of the given URL asynchronously using httpx.AsyncClient.

    Args:
        url (str): The URL to download.

    Returns:
        Any: The response object containing the downloaded content.

    Raises:
        Exception: If an error occurs during the download.
    """
    async with httpx.AsyncClient() as client:
        try:
            return await client.get(url)
        except Exception:
            ...


@async_timeit
async def download_all_urls(urls: list[str]) -> list[Awaitable[httpx.Response]]:
    """
    Downloads all the URLs asynchronously using asyncio.

    Args:
        urls (list[str]): A list of URLs to download.

    Returns:
        list[Awaitable[httpx.Response]]: A list of HTTPX Response objects.
    """
    return await asyncio.gather(*map(download_url, urls))


def main() -> None:
    """
    Entry point of the program.

    Downloads all the URLs generated and logs the progress.
    """
    @async_timeit
    async def _main() -> None:
        urls = generate_url(128)
        logger.info("Downloading all urls")
        await download_all_urls(urls)
        logger.info("Completed downloading all urls")

    asyncio.run(_main())


if __name__ == "__main__":
    asyncio.run(main())
