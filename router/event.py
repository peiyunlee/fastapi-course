from typing import List
from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from db import db_event
from db.database import get_db
from .schemas.eventSchema import EventResponseSchema
from .schemas.httpErrorSchema import HTTPError


router = APIRouter(
    prefix='/api/v1/event',
    tags=['Event']
)


@router.post('/', responses={
    200: {
        "model": EventResponseSchema,
        "description": "Successful Response",
    }
})
async def create_event_document(
    num_terminals = Form(...),
    db: Session = Depends(get_db),
):
    
    response = db_event.create_event(num_terminals=num_terminals,db=db)

    return response


@router.get('/all', response_model=List[EventResponseSchema], responses={
    200: {
        "model": List[EventResponseSchema],
        "description": "Successful Response",
    },
    404: {
        "model": HTTPError,
        "description": "Data not found",
        "content": {
            "application/json": {
                "example": {"detail": "找不到事件"},
            }
        },
    }
})
async def get_all_event_infos(db: Session = Depends(get_db)):
    response = db_event.get_all_event_infos(db=db)
    
    return response