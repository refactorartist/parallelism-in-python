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
    Downloads the content of multiple URLs sequentially and returns a list of responses.

    Args:
        urls (list[str]): A list of URLs to download.

    Returns:
        list[requests.Response]: A list of responses obtained from downloading the URLs.
    """
    responses: list[requests.Response] = []
    for site in urls:
        response = download_url(site)
        responses.append(response)

    return responses


@timeit
def main() -> None:
    """
    Main function that downloads a list of URLs sequentially.

    This function generates a list of URLs, downloads them one by one,
    and logs the progress.

    Returns:
        None
    """
    urls: list[str] = generate_url(10)
    logger.info("Downloading all urls")
    download_all_urls(urls)
    logger.info("Completed downloading all urls")


if __name__ == "__main__":
    main()
