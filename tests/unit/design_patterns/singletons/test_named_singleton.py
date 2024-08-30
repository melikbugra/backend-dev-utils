import pytest
from assertpy import assert_that

from backend_dev_utils.design_patterns.singletons.named_singleton.named_singleton_base import (
    NamedSingletonBase,
)


def test_named_singleton():
    class TestClass(NamedSingletonBase):
        def __init__(self, name: str, value: int) -> None:
            self.name = name
            self.value = value

    obj1 = TestClass(name="instance1", value=10)
    obj2 = TestClass(name="instance1", value=20)
    obj3 = TestClass(name="instance2", value=30)

    print(obj1.name, obj1.value)  # Output: instance1 10
    print(obj2.name, obj2.value)  # Output: instance1 10
    print(obj3.name, obj3.value)  # Output: instance2 30
    print(obj1 is obj2)  # Output: True
    print(obj1 is obj3)  # Output: False

    assert_that(obj1.name).is_equal_to("instance1")
    assert_that(obj1.value).is_equal_to(10)
    assert_that(obj2.name).is_equal_to("instance1")
    assert_that(obj2.value).is_not_equal_to(20)
    assert_that(obj2.value).is_equal_to(10)
    assert_that(obj1).is_equal_to(obj2)
    assert_that(obj2).is_not_equal_to(obj3)


def test_named_singleton_base_init():
    class TestClass(NamedSingletonBase):
        def __init__(self, name: str) -> None:
            super().__init__(name=name)

    obj = TestClass(name="instance")

    assert_that(obj.name).is_equal_to("instance")


def test_named_singleton_meta():
    class TestClass(NamedSingletonBase):
        def __init__(self, name: str) -> None:
            super().__init__(name=name)

    with pytest.raises(ValueError):
        obj = TestClass()

    obj2 = TestClass(name="instance")

    assert_that(obj2.name).is_equal_to("instance")


def test_named_singleton_meta_name_is_first_positional_argument():
    class TestClass(NamedSingletonBase):
        def __init__(self, name: str, value: int) -> None:
            self.name = name
            self.value = value

    obj = TestClass("instance", value=10)

    assert_that(obj.name).is_equal_to("instance")
    assert_that(obj.value).is_equal_to(10)
