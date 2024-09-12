import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend_dev_utils.fastapi_helpers.fastapi_router import FastAPIRouter
from backend_dev_utils.fastapi_helpers.fastapi_app import FastAPIApp
from backend_dev_utils.fastapi_helpers.fastapi_route import FastAPIRoute


@pytest.fixture
def fastapi_app():
    routers = [FastAPIRouter(prefix="/test", tags=["test-router"])]
    title = "Test App"
    description = "This is a test app"
    version = "0.1.0"
    openapi_url = "/openapi.json"
    docs_url = "/docs"
    root_path = ""
    include_default_router = True

    fastapi_app = FastAPIApp(
        routers=routers,
        title=title,
        description=description,
        version=version,
        openapi_url=openapi_url,
        docs_url=docs_url,
        root_path=root_path,
        include_default_router=include_default_router,
    )

    return fastapi_app


@pytest.fixture
def client(fastapi_app: FastAPIApp):
    return TestClient(fastapi_app.app)


@pytest.fixture
def test_router():
    return FastAPIRouter(prefix="/test", tags=["test-router"])


@pytest.fixture
def test_route():
    path = "/test"
    endpoint = lambda: {"message": "Hello, World!"}
    methods = ["GET"]
    response_model = None
    name = "test"

    return FastAPIRoute(
        path=path,
        endpoint=endpoint,
        methods=methods,
        response_model=response_model,
        name=name,
    )
