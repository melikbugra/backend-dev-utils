import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend_dev_utils.fastapi_helpers.fastapi_router import FastAPIRouter
from backend_dev_utils.fastapi_helpers.fastapi_app import FastAPIApp


@pytest.fixture
def app():
    routers = [FastAPIRouter(prefix="/test", tags=["test-router"])]
    title = "Test App"
    description = "This is a test app"
    version = "0.1.0"
    openapi_url = "/openapi.json"
    docs_url = "/docs"
    root_path = ""
    include_base_router = True

    app = FastAPIApp(
        routers=routers,
        title=title,
        description=description,
        version=version,
        openapi_url=openapi_url,
        docs_url=docs_url,
        root_path=root_path,
        include_base_router=include_base_router,
    )

    return app


@pytest.fixture
def client(app: FastAPI):
    return TestClient(app)


@pytest.fixture
def test_router():
    return FastAPIRouter(prefix="/test", tags=["test-router"])
