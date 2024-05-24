from pydantic import BaseModel, Field
from typing import List


class AdditionRequest(BaseModel):
    batchid: str = Field(..., example="id0101")
    payload: List[List[int]] = Field(..., example=[[1, 2], [3, 4]])


class AdditionResponse(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: str
    completed_at: str
