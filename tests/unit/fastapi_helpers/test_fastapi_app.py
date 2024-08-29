from fastapi.testclient import TestClient
from assertpy import assert_that


def test_app_initialization(client: TestClient):
    response = client.get("/")
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).is_equal_to({"message": "Hello World!"})


def test_openapi(client: TestClient):
    response = client.get("/openapi.json")
    assert_that(response.status_code).is_equal_to(200)


def test_docs(client: TestClient):
    response = client.get("/docs")
    assert_that(response.status_code).is_equal_to(200)
