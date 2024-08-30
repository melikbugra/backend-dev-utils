from backend_dev_utils import NamedSingletonBase


class TestClass(NamedSingletonBase):
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value


obj1 = TestClass("instance1", 10)
obj2 = TestClass("instance1", 20)
obj3 = TestClass("instance2", 30)

print(obj1.name, obj1.value)  # Output: instance1 10
print(obj2.name, obj2.value)  # Output: instance1 10
print(obj3.name, obj3.value)  # Output: instance2 30
print(obj1 is obj2)  # Output: True
print(obj1 is obj3)  # Output: False
