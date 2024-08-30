from fastapi import APIRouter
from sqlmodel import SQLModel


class FastAPIRoute:
    def __init__(
        self,
        router: APIRouter,
        path: str,
        endpoint: callable,
        methods: list[str],
        response_model: SQLModel = None,
        name: str = None,
    ):
        self.router = router
        self.path = path
        self.endpoint = endpoint
        self.methods = methods
        self.response_model = response_model
        self.name = name

        self._add_to_router()

    def _add_to_router(self):
        self.router.add_api_route(
            path=self.path,
            endpoint=self.endpoint,
            methods=self.methods,
            response_model=self.response_model,
            name=self.name,
        )
