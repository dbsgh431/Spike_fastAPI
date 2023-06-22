from fastapi import APIRouter, Body, HTTPException, status
from models.event import Event
from typing import List

event_router = APIRouter(
    tags=["Events"]
)

events = []

@event_router.get("/", response_model=List[Event])
async def retreive_all_events() -> List[Event]:
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id : int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="해당 id의 이벤트가 존재하지 않습니다."
    )

@event_router.post("/new")
async def create_event(body: Event=Body(...)) -> dict:
    events.append(body)
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