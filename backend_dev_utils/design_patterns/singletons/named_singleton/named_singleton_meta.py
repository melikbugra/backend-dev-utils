class NamedSingletonMeta(type):
    """
    A metaclass that creates a named Singleton base class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        name = kwargs.get("name")
        if name is None and len(args) > 0:
            name = args[0]

        if name is None:
            raise ValueError("A 'name' argument is required.")

        if (cls, name) not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[(cls, name)] = instance
        return cls._instances[(cls, name)]
