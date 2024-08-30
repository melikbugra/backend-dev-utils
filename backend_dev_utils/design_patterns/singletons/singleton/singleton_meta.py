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
