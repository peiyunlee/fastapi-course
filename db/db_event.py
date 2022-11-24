from db.models import DbEventInfo
from router.schemas.eventSchema import EventResponseSchema
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from typing import List


def create_event(num_terminals: int, db: Session) -> EventResponseSchema:

    new_event = DbEventInfo(
        num_terminals=num_terminals
    )

    db.add(new_event)
    db.commit()

    return {
        'event_id': new_event.event_id,
        'num_terminals': new_event.num_terminals,
    }


def get_all_event_infos(db: Session) -> List[EventResponseSchema]:

    events = db.query(DbEventInfo).all()

    if not events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'找不到事件資料')

    return events