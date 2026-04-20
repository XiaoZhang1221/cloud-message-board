from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/messages", tags=["messages"])


@router.get("/")
def get_messages(db: Session = Depends(get_db)):
    messages = crud.get_messages(db)
    return messages


@router.post("/")
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    new_message = crud.create_message(
        db=db,
        nickname=message.nickname,
        content=message.content
    )
    return new_message


@router.delete("/{message_id}")
def delete_message(message_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_message(db, message_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="留言不存在")
    return {"message": "删除成功"}