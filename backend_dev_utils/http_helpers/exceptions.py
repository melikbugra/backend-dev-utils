class InvalidURLError(Exception):
    def __init__(self, url):
        self.message = f"Invalid URL: {url}"
        super().__init__(self.message)
