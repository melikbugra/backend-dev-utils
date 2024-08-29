class InvalidURLError(Exception):
    def __init__(self, url):
        message = f"Invalid URL: {url}"
        super().__init__(message)
