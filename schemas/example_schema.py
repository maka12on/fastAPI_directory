from pydantic import BaseModel
from typing import List

class ResponseItem(BaseModel):
    '''
    route "/effect/list" レスポンス内容

    Parameters:
    -------
    result: str
    effectList: List[EffectItem]
    '''
    result: str
    id: str
