from assertpy import assert_that
from fastapi import APIRouter

from backend_dev_utils.fastapi_helpers.fastapi_route import FastAPIRoute


def test_fastapi_route_init():
    path = "/test"
    endpoint = lambda: {"message": "Hello, World!"}
    methods = ["GET"]
    response_model = None
    name = "test"

    test_route = FastAPIRoute(
        path=path,
        endpoint=endpoint,
        methods=methods,
        response_model=response_model,
        name=name,
    )

    assert_that(test_route.path).is_equal_to(path)
    assert_that(test_route.endpoint).is_equal_to(endpoint)
    assert_that(test_route.methods).is_equal_to(methods)
    assert_that(test_route.response_model).is_equal_to(response_model)
    assert_that(test_route.name).is_equal_to(name)
