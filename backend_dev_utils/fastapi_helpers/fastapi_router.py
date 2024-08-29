from fastapi import APIRouter, Depends, Response
from sqlmodel import Session
from sqlmodel import SQLModel

from backend_dev_utils.fastapi_helpers.fastapi_route import FastAPIRoute


class FastAPIRouter:
    def __new__(cls, prefix: str = "", tags: list[str] = ["base-router"]):
        instance = super().__new__(cls)
        init_result = instance._init_router(prefix=prefix, tags=tags)

        return init_result

    def _init_router(self, prefix: str, tags: list[str]):
        self.router = APIRouter(prefix=prefix, tags=tags)

        return self.router
