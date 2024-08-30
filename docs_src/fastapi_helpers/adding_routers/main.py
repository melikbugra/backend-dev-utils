from backend_dev_utils import FastAPIApp, FastAPIRouter, FastAPIRoute


def hello_endpoint(name: str):
    return {"message": f"Hello {name}"}


my_router = FastAPIRouter(prefix="/api/v1", tags=["my-router"])

hello_route = FastAPIRoute(
    router=my_router, path="/hello", endpoint=hello_endpoint, methods=["GET"]
)

app = FastAPIApp(
    routers=[my_router],
    title="Hello API",
    description="An API to say hello.",
    version="0.0.1",
    include_base_router=False,
)
