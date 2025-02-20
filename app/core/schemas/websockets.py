from pydantic import BaseModel


class ChatWSRequestSchema(BaseModel):
    message: str


class ChatWSResponseSchema(BaseModel):
    number: int
    message: str


class ChatWSErrorSchema(BaseModel):
    number: int
    message: str
