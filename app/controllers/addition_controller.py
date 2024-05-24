from fastapi import APIRouter, HTTPException
from app.models.addition_model import AdditionRequest, AdditionResponse
from app.utils.logger import logger
from multiprocessing import Pool
from datetime import datetime

router = APIRouter()


def add_list(nums):
    return sum(nums)


@router.post("/api/add", response_model=AdditionResponse)
async def add_numbers(request: AdditionRequest):
    try:
        started_at = datetime.now()

        with Pool() as pool:
            result = pool.map(add_list, request.payload)

        completed_at = datetime.now()

        return AdditionResponse(
            batchid=request.batchid,
            response=result,
            status="complete",
            started_at=started_at,
            completed_at=completed_at
        )
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An internal server error occurred")
