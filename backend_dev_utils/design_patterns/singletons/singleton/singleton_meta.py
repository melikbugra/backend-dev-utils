from backend_dev_utils.design_patterns.singletons.exceptions import (
    SingletonInstanceNotFoundError,
)


class SingletonMeta(type):
    """
    A metaclass that creates a Singleton base class when used as a metaclass.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def reset_instance(cls):
        """
        Reset the singleton instance.
        Raise SingletonInstanceNotFoundError if the instance does not exist.
        """
        if cls in cls._instances:
            del cls._instances[cls]
        else:
            raise SingletonInstanceNotFoundError(cls.__name__)
