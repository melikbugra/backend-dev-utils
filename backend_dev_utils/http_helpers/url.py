import re
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode, ParseResult


class URLValidatorHandler:
    def __init__(self, url: str):
        self.url = url
        self.parsed_url = urlparse(url)

    def is_valid_url(self) -> bool:
        """Validates the URL format using regex."""
        regex = re.compile(
            r"^(https?|ftp):\/\/"
            r'(?:(?:[a-zA-Z0-9$-_@.&+!*"(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'
            r"(?::\d+)?"
            r'(?:\/[a-zA-Z0-9$-_@.&+!*"(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))*\/?'
            r'(?:\?[a-zA-Z0-9$-_@.&+!*"(),]|(?:%[0-9a-fA-F][0-9a-fA-F])|[=])*'
            r'(?:#[a-zA-Z0-9$-_@.&+!*"(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))*$'
        )
        return re.match(regex, self.url) is not None

    def get_scheme(self) -> str:
        """Returns the scheme of the URL (e.g., http, https)."""
        return self.parsed_url.scheme

    def get_netloc(self) -> str:
        """Returns the network location (domain) of the URL."""
        return self.parsed_url.netloc

    def get_path(self) -> str:
        """Returns the path of the URL."""
        return self.parsed_url.path

    def get_query_params(self) -> dict:
        """Returns the query parameters as a dictionary."""
        return parse_qs(self.parsed_url.query)

    def get_fragment(self) -> str:
        """Returns the fragment (anchor) of the URL."""
        return self.parsed_url.fragment

    def with_scheme(self, scheme: str) -> str:
        """Returns a new URL with the updated scheme."""
        updated_url = self.parsed_url._replace(scheme=scheme)
        return urlunparse(updated_url)

    def with_netloc(self, netloc: str) -> str:
        """Returns a new URL with the updated network location (domain)."""
        updated_url = self.parsed_url._replace(netloc=netloc)
        return urlunparse(updated_url)

    def with_path(self, path: str) -> str:
        """Returns a new URL with the updated path."""
        updated_url = self.parsed_url._replace(path=path)
        return urlunparse(updated_url)

    def with_query_param(self, key: str, value: str) -> str:
        """Returns a new URL with an updated query parameter."""
        query_params = self.get_query_params()
        query_params[key] = [value]
        new_query_string = urlencode(query_params, doseq=True)
        updated_url = self.parsed_url._replace(query=new_query_string)
        return urlunparse(updated_url)

    def with_fragment(self, fragment: str) -> str:
        """Returns a new URL with the updated fragment."""
        updated_url = self.parsed_url._replace(fragment=fragment)
        return urlunparse(updated_url)

    def to_string(self) -> str:
        """Returns the complete URL as a string."""
        return self.url
