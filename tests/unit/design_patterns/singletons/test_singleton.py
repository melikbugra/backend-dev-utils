import pytest
from assertpy import assert_that

from backend_dev_utils.design_patterns.singletons.singleton.singleton_base import (
    SingletonBase,
)


def test_singleton():
    class TestClass(SingletonBase):
        def __init__(self, value: int) -> None:
            self.value = value

    obj1 = TestClass(10)
    obj2 = TestClass(20)

    assert_that(obj1.value).is_equal_to(10)
    assert_that(obj2.value).is_not_equal_to(20)
    assert_that(obj2.value).is_equal_to(10)
    assert_that(obj1).is_equal_to(obj2)
