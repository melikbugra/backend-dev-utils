import re
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

from backend_dev_utils.http_helpers.exceptions import InvalidURLError


class URL:
    def __init__(self, url: str):
        self.url_string = url
        if not self._is_valid_url():
            raise InvalidURLError(url)
        else:
            self.parsed_url = urlparse(url)

    def __str__(self) -> str:
        return self.url_string

    def _is_valid_url(self) -> bool:
        """Validates the URL format using regex."""
        regex = re.compile(
            r"^(https?|ftp):\/\/"  # protocol
            r"(?:(?:[a-zA-Z0-9-._~%!$&\'()*+,;=]+@)?"  # user:password (optional)
            r"(?:[a-zA-Z0-9-._~%]+|\[[a-fA-F0-9:.]+\])"  # domain or IP
            r"(?::\d{2,5})?)"  # port (optional)
            r"(?:\/[a-zA-Z0-9-._~%!$&\'()*+,;=:@/]*)*"  # path
            r"(?:\?[a-zA-Z0-9-._~%!$&\'()*+,;=:@/?]*)?"  # query string (optional)
            r"(?:#[a-zA-Z0-9-._~%!$&\'()*+,;=:@/?]*)?$"  # fragment identifier (optional)
        )
        return re.match(regex, self.url_string) is not None

    @property
    def scheme(self):
        """Scheme of the URL (e.g. https)."""
        return self.parsed_url.scheme

    @property
    def netloc(self):
        """Network location of the URL (e.g. www.example.com)."""
        return self.parsed_url.netloc

    @property
    def path(self):
        """Path of the URL (e.g. /path/to/resource)."""
        return self.parsed_url.path

    @property
    def query(self):
        """Query of the URL (e.g. ?query_param=value)."""
        return self.parsed_url.query

    @property
    def fragment(self):
        """Fragment of the URL (e.g. #section1)."""
        return self.parsed_url.fragment

    def get_query_params(self) -> dict:
        """Returns the query parameters as a dictionary."""
        return parse_qs(self.parsed_url.query)

    def with_scheme(self, scheme: str) -> None:
        """Updates the scheme of the URL."""
        self.parsed_url = self.parsed_url._replace(scheme=scheme)
        self.url_string = urlunparse(self.parsed_url)

    def with_netloc(self, netloc: str) -> None:
        """Updates the network location (domain) of the URL."""
        self.parsed_url = self.parsed_url._replace(netloc=netloc)
        self.url_string = urlunparse(self.parsed_url)

    def with_path(self, path: str) -> None:
        """Updates the path of the URL."""
        self.parsed_url = self.parsed_url._replace(path=path)
        self.url_string = urlunparse(self.parsed_url)

    def with_query_param(self, key: str, value: str) -> None:
        """Updates or adds a specific query parameter in the URL."""
        query_params = self.get_query_params()
        query_params[key] = [value]
        new_query_string = urlencode(query_params, doseq=True)
        self.parsed_url = self.parsed_url._replace(query=new_query_string)
        self.url_string = urlunparse(self.parsed_url)

    def delete_query_param(self, key: str) -> None:
        """Deletes a specific query parameter from the URL."""
        query_params = self.get_query_params()
        if key in query_params:
            del query_params[key]
        new_query_string = urlencode(query_params, doseq=True)
        self.parsed_url = self.parsed_url._replace(query=new_query_string)
        self.url_string = urlunparse(self.parsed_url)

    def with_fragment(self, fragment: str) -> None:
        """Updates the fragment (anchor) of the URL."""
        self.parsed_url = self.parsed_url._replace(fragment=fragment)
        self.url_string = urlunparse(self.parsed_url)
