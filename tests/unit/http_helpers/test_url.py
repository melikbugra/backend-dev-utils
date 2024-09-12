import pytest
from assertpy import assert_that

from backend_dev_utils.http_helpers.url import URL
from backend_dev_utils.http_helpers.exceptions import InvalidURLError


def test_init_url():
    url = URL("http://www.example.com")

    assert_that(url).is_instance_of(URL)
    assert_that(url.url_string).is_equal_to("http://www.example.com")
    assert_that(url.scheme).is_equal_to("http")
    assert_that(url.netloc).is_equal_to("www.example.com")
    assert_that(url.path).is_equal_to("")
    assert_that(url.query).is_equal_to("")
    assert_that(url.fragment).is_equal_to("")


def test_init_invalid_url():
    with pytest.raises(InvalidURLError):
        URL("www.example.com")


def test_with_scheme():
    url = URL("http://www.example.com")
    url2 = url.with_scheme("https")

    assert_that(url).is_instance_of(URL)
    assert_that(url.url_string).is_equal_to("https://www.example.com")
    assert_that(url.scheme).is_equal_to("https")
    assert_that(url.netloc).is_equal_to("www.example.com")
    assert_that(url.path).is_equal_to("")
    assert_that(url.query).is_equal_to("")
    assert_that(url.fragment).is_equal_to("")
    assert_that(url2).is_instance_of(URL)
    assert_that(str(url2)).is_equal_to("https://www.example.com")


def test_str():
    url = URL("http://www.example.com")

    assert_that(str(url)).is_equal_to("http://www.example.com")


def test_is_valid_url():
    url = URL("http://www.example.com")

    assert_that(url._is_valid_url()).is_true()

    with pytest.raises(InvalidURLError):
        URL("www.example.com")


def test_properties():
    url = URL("http://www.example.com")

    assert_that(url.scheme).is_equal_to("http")
    assert_that(url.netloc).is_equal_to("www.example.com")
    assert_that(url.path).is_equal_to("")
    assert_that(url.query).is_equal_to("")
    assert_that(url.fragment).is_equal_to("")


def test_properties_with_path_query_fragment():
    url = URL(
        "http://www.example.com/path/to/resource?param1=value1&param2=value2#section1"
    )

    assert_that(url.scheme).is_equal_to("http")
    assert_that(url.netloc).is_equal_to("www.example.com")
    assert_that(url.path).is_equal_to("/path/to/resource")
    assert_that(url.query).is_equal_to("param1=value1&param2=value2")
    assert_that(url.fragment).is_equal_to("section1")


def test_with_netloc():
    url = URL("http://www.example.com")
    url2 = url.with_netloc("www.example.org")

    assert_that(url).is_instance_of(URL)
    assert_that(url.url_string).is_equal_to("http://www.example.org")
    assert_that(url.scheme).is_equal_to("http")
    assert_that(url.netloc).is_equal_to("www.example.org")
    assert_that(url.path).is_equal_to("")
    assert_that(url.query).is_equal_to("")
    assert_that(url.fragment).is_equal_to("")
    assert_that(url2).is_instance_of(URL)
    assert_that(str(url2)).is_equal_to("http://www.example.org")


def test_with_path():
    url = URL("http://www.example.com")
    url2 = url.with_path("/new/path")

    assert_that(url).is_instance_of(URL)
    assert_that(url.url_string).is_equal_to("http://www.example.com/new/path")
    assert_that(url.scheme).is_equal_to("http")
    assert_that(url.netloc).is_equal_to("www.example.com")
    assert_that(url.path).is_equal_to("/new/path")
    assert_that(url.query).is_equal_to("")
    assert_that(url.fragment).is_equal_to("")
    assert_that(url2).is_instance_of(URL)
    assert_that(str(url2)).is_equal_to("http://www.example.com/new/path")


def test_with_fragment():
    url = URL("http://www.example.com")
    url2 = url.with_fragment("section1")

    assert_that(url).is_instance_of(URL)
    assert_that(url.url_string).is_equal_to("http://www.example.com#section1")
    assert_that(url.scheme).is_equal_to("http")
    assert_that(url.netloc).is_equal_to("www.example.com")
    assert_that(url.path).is_equal_to("")
    assert_that(url.query).is_equal_to("")
    assert_that(url.fragment).is_equal_to("section1")
    assert_that(url2).is_instance_of(URL)
    assert_that(str(url2)).is_equal_to("http://www.example.com#section1")


def test_with_query_param():
    url = URL("http://www.example.com")
    url2 = url.with_query_param("param1", "value1")

    assert_that(url).is_instance_of(URL)
    assert_that(url.url_string).is_equal_to("http://www.example.com?param1=value1")
    assert_that(url.scheme).is_equal_to("http")
    assert_that(url.netloc).is_equal_to("www.example.com")
    assert_that(url.path).is_equal_to("")
    assert_that(url.query).is_equal_to("param1=value1")
    assert_that(url.fragment).is_equal_to("")
    assert_that(url2).is_instance_of(URL)
    assert_that(str(url2)).is_equal_to("http://www.example.com?param1=value1")


def test_with_query_param_with_existing_query():
    url = URL("http://www.example.com?param1=value1")
    url2 = url.with_query_param("param2", "value2")

    assert_that(url).is_instance_of(URL)
    assert_that(url.url_string).is_equal_to(
        "http://www.example.com?param1=value1&param2=value2"
    )
    assert_that(url.scheme).is_equal_to("http")
    assert_that(url.netloc).is_equal_to("www.example.com")
    assert_that(url.path).is_equal_to("")
    assert_that(url.query).is_equal_to("param1=value1&param2=value2")
    assert_that(url.fragment).is_equal_to("")
    assert_that(url2).is_instance_of(URL)
    assert_that(str(url2)).is_equal_to(
        "http://www.example.com?param1=value1&param2=value2"
    )


def test_delete_query_param():
    url = URL("http://www.example.com?param1=value1&param2=value2")
    url2 = url.delete_query_param("param1")

    assert_that(url).is_instance_of(URL)
    assert_that(url.url_string).is_equal_to("http://www.example.com?param2=value2")
    assert_that(url.scheme).is_equal_to("http")
    assert_that(url.netloc).is_equal_to("www.example.com")
    assert_that(url.path).is_equal_to("")
    assert_that(url.query).is_equal_to("param2=value2")
    assert_that(url.fragment).is_equal_to("")
    assert_that(url2).is_instance_of(URL)
    assert_that(str(url2)).is_equal_to("http://www.example.com?param2=value2")


def test_get_query_params():
    url = URL("http://www.example.com?param1=value1&param2=value2")
    query_params = url.get_query_params()

    assert_that(query_params).is_equal_to({"param1": ["value1"], "param2": ["value2"]})


def test_get_query_params_with_no_query():
    url = URL("http://www.example.com")
    query_params = url.get_query_params()

    assert_that(query_params).is_equal_to({})


def test_get_query_params_with_no_query_params():
    url = URL("http://www.example.com?")
    query_params = url.get_query_params()

    assert_that(query_params).is_equal_to({})
