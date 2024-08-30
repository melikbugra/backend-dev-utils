from assertpy import assert_that
from fastapi import APIRouter

from backend_dev_utils.fastapi_helpers.fastapi_route import FastAPIRoute


def test_fastapi_route_init(test_router):
    path = "/test"
    endpoint = lambda: {"message": "Hello, World!"}
    methods = ["GET"]
    response_model = None
    name = "test"

    test_route = FastAPIRoute(
        router=test_router,
        path=path,
        endpoint=endpoint,
        methods=methods,
        response_model=response_model,
        name=name,
    )

    assert_that(test_route.router).is_equal_to(test_router)


def test_add_to_router(test_router: APIRouter):
    path = "/test"
    endpoint = lambda: {"message": "Hello, World!"}
    methods = ["GET"]
    response_model = None
    name = "test"

    test_route = FastAPIRoute(
        router=test_router,
        path=path,
        endpoint=endpoint,
        methods=methods,
        response_model=response_model,
        name=name,
    )

    assert_that(test_route.router.routes).is_length(1)
    assert_that(test_route.router.routes[0].path).is_equal_to(
        f"{test_router.prefix}{path}"
    )
    assert_that(test_route.router.routes[0].methods).is_equal_to(set(methods))
    assert_that(test_route.router.routes[0].name).is_equal_to(name)
    assert_that(test_route.router.routes[0].response_model).is_equal_to(response_model)
    assert_that(test_route.router.routes[0].endpoint).is_equal_to(endpoint)
    assert_that(test_route.router.routes[0].dependencies).is_length(0)
