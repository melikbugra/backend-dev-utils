from fastapi import APIRouter


class FastAPIRouter:
    def __init__(self, prefix: str = "", tags: list[str] = ["base-router"]):
        self.router = APIRouter(prefix=prefix, tags=tags)
