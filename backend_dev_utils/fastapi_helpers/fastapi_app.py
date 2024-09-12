from fastapi import FastAPI, APIRouter

from backend_dev_utils.fastapi_helpers.fastapi_router import FastAPIRouter
from backend_dev_utils.fastapi_helpers.fastapi_route import FastAPIRoute


class FastAPIApp:
    def __init__(
        self,
        routers: list[FastAPIRouter] = [],
        routes: list[FastAPIRoute] = [],
        title: str = "FastAPI App",
        description: str = "",
        version: str = "0.0.1",
        openapi_url: str = "/openapi.json",
        docs_url: str = "/docs",
        root_path: str = "",
        include_default_router: bool = True,
    ):
        self.app = FastAPI(
            title=title,
            description=description,
            version=version,
            openapi_url=openapi_url,
            docs_url=docs_url,
            root_path=root_path,
        )

        self.routers: list = []
        self.routes: list = []

        if include_default_router:
            self._add_default_router()

        for router in routers:
            self.add_router(router)

        for route in routes:
            self.add_route(route)

    def _add_default_router(self):
        route = FastAPIRoute(
            path="/",
            endpoint=lambda: {f"{self.app.title}": f"{self.app.version}"},
            methods=["GET"],
            response_model=None,
            name="root",
        )
        default_router = FastAPIRouter(
            routes=[route], tags=["default-router"], prefix=""
        )
        self.add_router(default_router)

    def add_route(self, fastapi_route: FastAPIRoute):
        self.app.add_api_route(
            path=fastapi_route.path,
            endpoint=fastapi_route.endpoint,
            methods=fastapi_route.methods,
            response_model=fastapi_route.response_model,
            name=fastapi_route.name,
        )
        self.routes.append(fastapi_route)

    def add_router(self, fastapi_router: FastAPIRouter):
        self.app.include_router(fastapi_router.router)
        self.routers.append(fastapi_router)
