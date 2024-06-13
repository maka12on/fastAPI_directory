from typing import Any
from fastapi import status


class BaseMessage:
    """メッセージクラスのベース"""

    text: str
    # status_code: int = status.HTTP_400_BAD_REQUEST
    status_code: int = status.HTTP_400_BAD_REQUEST

    def __init__(self, param: Any | None = None) -> None:
        self.param = param

    def __str__(self) -> str:
        return self.__class__.__name__


class ErrorMessage:
    """エラーメッセージクラス.

    Notes
    -----
        BaseMessagを継承することで
        Class呼び出し時にClass名がエラーコードになり、.textでエラーメッセージも取得できるため
        エラーコードと、メッセージの管理が直感的に行える。

        fastAPIステータスコード:https://fastapi.tiangolo.com/reference/status/

    """
    # 共通
    class CUSTOM_ERROR_EXAMPLE_ADD_MESSAGE(BaseMessage):
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        text = "システムエラーが発生しました"

        def __init__(self, error_log: str = None,) -> None:
            self.error_log = error_log

    class CUSTOM_ERROR_EXAMPLE(BaseMessage):
        status_code = 501
        text = "システムエラーが発生しました。"
