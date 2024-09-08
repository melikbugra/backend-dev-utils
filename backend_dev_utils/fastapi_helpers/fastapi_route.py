from sqlmodel import SQLModel

from backend_dev_utils.fastapi_helpers.fastapi_router import FastAPIRouter
from backend_dev_utils.fastapi_helpers.fastapi_app import FastAPIApp


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

    def add_to_router(self, fastapi_router: FastAPIRouter):
        fastapi_router.router.add_api_route(
            path=self.path,
            endpoint=self.endpoint,
            methods=self.methods,
            response_model=self.response_model,
            name=self.name,
        )

    def add_to_app(self, fastapi_app: FastAPIApp):
        fastapi_app.app.add_api_route(
            path=self.path,
            endpoint=self.endpoint,
            methods=self.methods,
            response_model=self.response_model,
            name=self.name,
        )
