from pydantic import BaseModel, ConfigDict


class MessageCreate(BaseModel):
    nickname: str
    content: str


class MessageResponse(BaseModel):
    id: int
    nickname: str
    content: str
    created_at: str | None = None

    model_config = ConfigDict(from_attributes=True)