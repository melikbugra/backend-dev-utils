from fastapi.testclient import TestClient
from assertpy import assert_that

from backend_dev_utils.fastapi_helpers.fastapi_app import FastAPIApp
from backend_dev_utils.fastapi_helpers.fastapi_route import FastAPIRoute
from backend_dev_utils.fastapi_helpers.fastapi_router import FastAPIRouter


def test_app_initialization(client: TestClient):
    response = client.get("/")
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).is_equal_to({"Test App": "0.1.0"})


def test_openapi(client: TestClient):
    response = client.get("/openapi.json")
    assert_that(response.status_code).is_equal_to(200)


def test_docs(client: TestClient):
    response = client.get("/docs")
    assert_that(response.status_code).is_equal_to(200)


def test_add_route():
    fastapi_route = FastAPIRoute(
        path="/test", endpoint=lambda: {"test": "test"}, methods=["GET"]
    )
    fastapi_route2 = FastAPIRoute(
        path="/test2", endpoint=lambda: {"test2": "test2"}, methods=["GET"]
    )
    fastapi_app = FastAPIApp(routes=[fastapi_route])
    fastapi_app.add_route(fastapi_route2)

    client = TestClient(fastapi_app.app)
    response = client.get("/test")
    response2 = client.get("/test2")

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).is_equal_to({"test": "test"})
    assert_that(response2.status_code).is_equal_to(200)
    assert_that(response2.json()).is_equal_to({"test2": "test2"})
    assert_that(fastapi_app.routes).contains(fastapi_route)
    assert_that(fastapi_app.routes).contains(fastapi_route2)


def test_add_router():
    fastapi_route = FastAPIRoute(
        path="/test", endpoint=lambda: {"test": "test"}, methods=["GET"]
    )
    fastapi_router = FastAPIRouter(routes=[fastapi_route])
    fastapi_app = FastAPIApp(routers=[fastapi_router])

    client = TestClient(fastapi_app.app)
    response = client.get("/api/v1/test")

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).is_equal_to({"test": "test"})
    assert_that(fastapi_app.routers).contains(fastapi_router)
