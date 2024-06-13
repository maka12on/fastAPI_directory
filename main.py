from mangum import Mangum
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError

from routers import example_router
from exceptions.handler import ExampleMiddleware

app = FastAPI()
app.add_middleware(ExampleMiddleware)

# デフォルトのバリデーションエラーハンドラーを上書き
@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request: Request, exc: RequestValidationError):
    raise exc

app.include_router(example_router.router)

handler = Mangum(app)
