from pydantic import BaseModel
from typing import List

class ResponseItem(BaseModel):
    '''
    ResponseItem

    Parameters:
    -------
    result: str
    effectList: str
    '''
    result: str
    id: str
