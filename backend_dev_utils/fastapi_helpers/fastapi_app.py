from fastapi import FastAPI, APIRouter

from backend_dev_utils.fastapi_helpers.fastapi_router import FastAPIRouter
from backend_dev_utils.fastapi_helpers.fastapi_route import FastAPIRoute


class FastAPIApp:
    def __new__(
        cls,
        routers: list[APIRouter] = [],
        title: str = "FastAPI App",
        description: str = "",
        version: str = "0.0.1",
        openapi_url: str = "/openapi.json",
        docs_url: str = "/docs",
        root_path: str = "",
        include_default_router: bool = False,
    ):
        instance = super().__new__(cls)
        init_result = instance._init_app(
            routers=routers,
            title=title,
            description=description,
            version=version,
            openapi_url=openapi_url,
            docs_url=docs_url,
            root_path=root_path,
            include_default_router=include_default_router,
        )

        return init_result

    def _init_app(
        self,
        routers: list[APIRouter],
        title: str,
        description: str,
        version: str,
        openapi_url: str,
        docs_url: str,
        root_path: str,
        include_default_router: bool,
    ):
        self.app = FastAPI(
            title=title,
            description=description,
            version=version,
            openapi_url=openapi_url,
            docs_url=docs_url,
            root_path=root_path,
        )

        if include_default_router:
            self._add_default_router()

        for router in routers:
            self.app.include_router(router)

        return self.app

    def _add_default_router(self):
        default_router = FastAPIRouter(tags=["default-router"])
        FastAPIRoute(
            router=default_router,
            path="/",
            endpoint=lambda: {"message": "Hello World!"},
            methods=["GET"],
            response_model=None,
            name="hello-world",
        )
        self.app.include_router(default_router)
        return self.app
