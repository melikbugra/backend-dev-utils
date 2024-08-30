from backend_dev_utils.design_patterns.singletons.named_singleton.named_singleton_meta import (
    NamedSingletonMeta,
)


class NamedSingletonBase(metaclass=NamedSingletonMeta):
    """
    Base class to be inherited by any class that should be a named singleton.
    """

    def __init__(self, name: str) -> None:
        self.name = name
