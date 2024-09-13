from backend_dev_utils import FastAPIApp, FastAPIRouter, FastAPIRoute


def hello_endpoint(name: str):
    return {"message": f"Hello {name}"}


hello_route = FastAPIRoute(path="/hello", endpoint=hello_endpoint, methods=["GET"])

fastapi_app = FastAPIApp(
    routes=[hello_route],
    title="Hello API",
    description="An API to say hello.",
    version="0.0.1",
    include_default_router=False,
)

app = fastapi_app.app
