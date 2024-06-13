from fastapi import APIRouter

from schemas.example_schema import ResponseItem
from models import example_model

router = APIRouter()

@router.get("/example/get", status_code=200, response_model=ResponseItem)
# GetProductResponseの型を返す宣言
async def example()-> ResponseItem:
    """
    データを返す
    
    Returns
    -------
    ResponseItem
    """
    try:
        item = example_model()
        return ResponseItem(result="success", id=item['id'])
    except Exception as e:
        raise e
