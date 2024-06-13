from fastapi import FastAPI, Response, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.middleware.base import BaseHTTPMiddleware

from exceptions.custom_exception import CustomException


class ExampleMiddleware(BaseHTTPMiddleware):
    # async def response_exception_middleware(self, request: Request, call_next) -> Response:
    async def dispatch(self, request: Request, call_next) -> Response:
        '''
        カスタム例外をスローすると、ミドルウェアが発火する。
        ミドルウェアがリクエストの処理チェーン全体を監視し、例外をキャッチして処理

        Args:
            request: HTTPリクエストオブジェクト
            call_next: 次のミドルウェアまたはリクエストハンドラを呼び出すための関数

        Returns:
            JSONResponse: 例外が発生した場合のエラーレスポンス、または通常のレスポンス
        '''
        try:
            response = await call_next(request)
        except CustomException as exc:
            return JSONResponse(
                status_code=exc.status_code,
                content={"result": "failure","message" : exc.message},
            )
        except RequestValidationError as exc:
            return JSONResponse(
                status_code=403,
                content={"message": "Request validation error"}
            )
        except Exception as exc:
            # 予期しないエラーの場合
            return JSONResponse(
                status_code=500,
                content={"result": "failure", "message": "A system error has occurred"}
            )
        return response
