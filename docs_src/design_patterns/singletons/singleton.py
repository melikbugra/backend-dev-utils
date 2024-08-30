from backend_dev_utils import SingletonBase


class MyClass(SingletonBase):
    def __init__(self, value):
        self.value = value


obj1 = MyClass(10)
obj2 = MyClass(20)

print(obj1.value)  # Output: 10
print(obj2.value)  # Output: 10
print(obj1 is obj2)  # Output: True
