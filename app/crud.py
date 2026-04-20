from sqlalchemy.orm import Session
from app.models import Message


def get_messages(db: Session):
    return db.query(Message).order_by(Message.id.desc()).all()


def create_message(db: Session, nickname: str, content: str):
    msg = Message(nickname=nickname, content=content)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg


def delete_message(db: Session, message_id: int):
    msg = db.query(Message).filter(Message.id == message_id).first()
    if not msg:
        return None

    db.delete(msg)
    db.commit()
    return msg