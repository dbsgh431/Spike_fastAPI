from fastapi import APIRouter, Body, HTTPException, status, Request, Depends
from models.event import Event, EventUpdate
from database.connection import get_session
from sqlmodel import select
from typing import List

event_router = APIRouter(
    tags=["Events"]
)

events = []

@event_router.get("/", response_model=List[Event])
async def retreive_all_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id : int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return event
   
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="해당 id의 이벤트가 존재하지 않습니다."
    )

@event_router.post("/new")
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    
    return{
        "message" : "이벤트 생성 성공"
    }

@event_router.delete("/{id}")
async def delete_event(id : int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message" : "이벤트 삭제 완료"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="이벤트가 존재하지 않습니다."
    )

@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message" : "모든 이벤트 삭제 완료"
    }

@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id:int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        
        session.add(event)
        session.commit()
        session.refresh(event)
        
        return event
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
