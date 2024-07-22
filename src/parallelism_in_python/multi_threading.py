import os
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from loguru import logger

from parallelism_in_python.utils.timeit import timeit
from parallelism_in_python.utils.urls import generate_url


@timeit
def download_url(url: str) -> requests.Response:
    """
    Downloads the content of the specified URL.

    Args:
        url (str): The URL to download.

    Returns:
        requests.Response: The response object containing the downloaded content.
    """
    try:
        return requests.get(url)
    except Exception:
        ...


@timeit
def download_all_urls(urls: list[str]) -> list[requests.Response]:
    """
    Downloads multiple URLs concurrently using multi-threading.

    Args:
        urls (list[str]): A list of URLs to download.

    Returns:
        list[requests.Response]: A list of responses obtained from downloading the URLs.
    """
    responses = []

    total_workers = os.cpu_count() * 2
    logger.info(f"Total workers: {total_workers}")

    with ThreadPoolExecutor(max_workers=total_workers) as executor:
        futures = [executor.submit(download_url, url) for url in urls]
        responses = [future.result() for future in as_completed(futures)]

    return responses


@timeit
def main() -> None:
    """
    Main function that downloads multiple URLs concurrently using multi-threading.

    This function generates a list of URLs, downloads them concurrently using multiple threads,
    and logs the progress using a logger.

    Returns:
        None
    """
    urls = generate_url(128)
    logger.info("Downloading all urls")
    download_all_urls(urls)
    logger.info("Completed downloading all urls")


if __name__ == "__main__":
    main()
