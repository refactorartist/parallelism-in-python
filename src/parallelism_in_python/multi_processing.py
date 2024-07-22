import multiprocessing

import requests
from loguru import logger

from parallelism_in_python.utils.timeit import timeit
from parallelism_in_python.utils.urls import generate_url


@timeit
def download_url(url: str) -> requests.Response:
    """
    Downloads the content of the given URL.

    Args:
        url (str): The URL to download.

    Returns:
        requests.Response: The response object containing the downloaded content.
    """
    return requests.get(url)


@timeit
def download_all_urls(urls: list[str]) -> list[requests.Response]:
    """
    Downloads the content of multiple URLs concurrently using multiprocessing.

    Args:
        urls (list[str]): A list of URLs to download.

    Returns:
        list[requests.Response]: A list of responses obtained from downloading the URLs.
    """
    responses = []

    total_workers = multiprocessing.cpu_count()
    logger.info(f"Total workers: {total_workers}")

    with multiprocessing.Pool(total_workers) as pool:
        responses = pool.map(download_url, urls)

    return responses


@timeit
def main() -> None:
    """
    Entry point of the program.

    This function generates a list of URLs, downloads the content of each URL,
    and logs the progress.
    """
    urls = generate_url(128)
    logger.info("Downloading all urls")
    download_all_urls(urls)
    logger.info("Completed downloading all urls")


if __name__ == "__main__":
    main()
