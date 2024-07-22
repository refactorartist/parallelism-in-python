def generate_url(total_urls: int) -> list[str]:
    """
    Generate a list of URLs with a specified length.

    Args:
        total_urls (int): The number of URLs to generate.

    Returns:
        list[str]: A list of URLs.

    """
    return ["https://httpbin.org/delay/1" for _ in range(total_urls)]
