from sqlmodel import SQLModel


class FastAPIRoute:
    def __init__(
        self,
        path: str,
        endpoint: callable,
        methods: list[str],
        response_model: SQLModel = None,
        name: str = None,
    ):
        self.path = path
        self.endpoint = endpoint
        self.methods = methods
        self.response_model = response_model
        self.name = name
