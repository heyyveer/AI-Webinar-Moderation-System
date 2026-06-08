from fastapi import APIRouter
from pydantic import BaseModel

from process_message import process_message

router = APIRouter()

class MessageRequest(BaseModel):
    message: str


@router.post("/analyze")
def analyze_message(request: MessageRequest):

    result = process_message(
        request.message
    )

    return result