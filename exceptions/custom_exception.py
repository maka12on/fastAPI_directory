from typing import Any
from fastapi import HTTPException, status

class CustomException(Exception):
    """
    HTTPExceptionを継承して、新しいカスタム例外クラスを定義
    default_status_code: デフォルトのステータスコードを400（Bad Request）に設定。
    
    """

    default_status_code = status.HTTP_400_BAD_REQUEST
    default_error_msg   = "A system error has occurred"

    def __init__(
        self,
        error: Any,
        status_code: int    = default_status_code,
        error_msg: str      = default_error_msg,
        headers: dict[str, Any] | None = None,
    ) -> None:
        self.headers = headers
        try:
            error_obj = error()
        except Exception:
            error_obj = error

        try:
            self.message = error_obj.text.format(error_obj.param)
        except Exception:
            self.message = error_obj.text

        try:
            self.status_code = error_obj.status_code
        except Exception:
            self.status_code = status_code
        
        if hasattr(error_obj, 'error_log'):
            print(f"error_code : {str(error_obj)} 詳細: {error_obj.error_log}")

        self.detail = {"error_code": str(error_obj), "error_msg": self.message}
