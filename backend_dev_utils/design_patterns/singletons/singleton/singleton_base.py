from backend_dev_utils.design_patterns.singletons.singleton.singleton_meta import (
    SingletonMeta,
)


class SingletonBase(metaclass=SingletonMeta):
    """
    Base class to be inherited by any class that should be a singleton.
    """

    pass
