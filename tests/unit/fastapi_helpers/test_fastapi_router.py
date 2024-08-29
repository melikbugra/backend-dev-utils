from assertpy import assert_that
from fastapi import APIRouter
from backend_dev_utils.fastapi_helpers.fastapi_router import FastAPIRouter


def test_fastapi_router_with_prefix():
    prefix = "/api"
    router = FastAPIRouter(prefix=prefix)
    assert_that(router.prefix).is_equal_to(prefix)


def test_fastapi_router_with_tags():
    tags = ["users", "admin"]
    router = FastAPIRouter(tags=tags)
    assert_that(router.tags).is_equal_to(tags)


def test_fastapi_router_with_default_tags():
    router = FastAPIRouter()
    assert_that(router.tags).is_equal_to(["base-router"])
    assert_that(router.tags).is_length(1)


def test_fastapi_router_instantiation():
    router = FastAPIRouter()
    assert_that(router).is_instance_of(APIRouter)


def test_fastapi_router_init_router():
    prefix = "/api"
    tags = ["users", "admin"]
    router = FastAPIRouter(prefix, tags)
    assert_that(router).is_instance_of(APIRouter)
    assert_that(router.prefix).is_equal_to(prefix)
    assert_that(router.tags).is_equal_to(tags)