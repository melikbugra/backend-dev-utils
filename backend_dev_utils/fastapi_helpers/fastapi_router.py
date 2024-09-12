from fastapi import APIRouter

from backend_dev_utils.fastapi_helpers.fastapi_route import FastAPIRoute


class FastAPIRouter:
    def __init__(
        self,
        routes: list[FastAPIRoute] = [],
        prefix: str = "/api/v1",
        tags: list[str] = ["api-router"],
    ):
        self.router = APIRouter(prefix=prefix, tags=tags)
        self.routes: list = []

        for route in routes:
            self.add_route(route)

    def add_route(self, fastapi_route: FastAPIRoute):
        self.router.add_api_route(
            path=fastapi_route.path,
            endpoint=fastapi_route.endpoint,
            methods=fastapi_route.methods,
            response_model=fastapi_route.response_model,
            name=fastapi_route.name,
        )
        self.routes.append(fastapi_route)
