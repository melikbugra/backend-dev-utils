from fastapi import APIRouter, Depends, Response
from sqlmodel import Session
from sqlmodel import SQLModel
import requests
import json


class FastAPIRoute:
    def __init__(
        self,
        router: APIRouter,
        path: str,
        endpoint: callable,
        methods: list[str],
        response_model: SQLModel = None,
        name: str = None,
        input_schema: SQLModel = None,
        input_params: dict = None,
    ):
        self.router = router
        self.path = path
        self.endpoint = endpoint
        self.methods = methods
        self.response_model = response_model
        self.name = name
        self.input_schema = input_schema
        self.input_params = input_params

        self._add_to_router()

    def _add_to_router(self):
        self.router.add_api_route(
            path=self.path,
            endpoint=self.endpoint,
            methods=self.methods,
            response_model=self.response_model,
            name=self.name,
        )
