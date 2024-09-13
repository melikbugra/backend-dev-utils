HTTP Helpers module contains helper functions for making http, requests, url validations etc. Its name contains "HTTP" but it might contain helper functions for other protocols. I named it like this because http seems cool in a module name :smile:.


### URL

First, the class validates the URL at intialization.

<!-- termynal: {"prompt_literal_start": ["$", ">>>"], title: python} -->

```python
>>> from backend_dev_utils import URL
>>> url = URL("http://////example.com")
backend_dev_utils.http_helpers.exceptions.InvalidURLError: Invalid URL: http://////example.com
```

Then you can change its scheme, netloc, path, params and fragment:

<!-- termynal: {"prompt_literal_start": ["$", ">>>"], title: python} -->

```python
>>> from backend_dev_utils import URL
>>> url = URL("http://www.example.com")
>>> url.with_scheme("https")
https://www.example.com
>>> url.with_netloc("example2.net")
https://example2.net
>>> url.with_path("/hello/world")
https://example2.net/hello/world
>>> url.with_query_param(key="hello", value="world")
https://example2.net/hello/world?hello=world
>>> url.delete_query_param("hello")
https://example2.net/hello/world
>>> url.with_fragment("hello")
https://example2.net/hello/world#hello
```

