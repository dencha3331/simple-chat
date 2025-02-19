from pydantic import BaseModel, Field


class ChatWSRequestSchema(BaseModel):
    message: str = Field()


class ChatWSResponseSchema(BaseModel):
    number: int = Field()
    message: str = Field()


class ChatWSErrorSchema(BaseModel):
    number: int = Field()
    message: str = Field()
