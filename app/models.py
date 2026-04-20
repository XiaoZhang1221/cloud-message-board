from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from app.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))