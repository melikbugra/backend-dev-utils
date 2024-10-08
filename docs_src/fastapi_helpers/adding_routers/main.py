from backend_dev_utils import FastAPIApp, FastAPIRouter, FastAPIRoute


def hello_endpoint(name: str):
    return {"message": f"Hello {name}"}


hello_route = FastAPIRoute(path="/hello", endpoint=hello_endpoint, methods=["GET"])

my_router = FastAPIRouter(prefix="/api/v1", tags=["my-router"])
my_router.add_route(hello_route)

fastapi_app = FastAPIApp(
    routers=[my_router],
    title="Hello API",
    description="An API to say hello.",
    version="0.0.1",
    include_default_router=False,
)

app = fastapi_app.app
