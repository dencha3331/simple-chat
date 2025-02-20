from fastapi import WebSocket
from pydantic import ValidationError
from websockets import ConnectionClosed

from core.schemas import websockets as ws_schemas


class ChatWebSocketManager:
    def __init__(self, websocket: WebSocket):
        self.connection: WebSocket = websocket
        self.message_id = 1

    async def connect(self):
        await self.connection.accept()

    async def disconnect(self):
        try:
            await self.connection.close()
        except RuntimeError:
            print("Сокет-соединение уже закрыто.")

    async def send_message_to_chat(self, data: dict):
        try:
            message_data = ws_schemas.ChatWSRequestSchema.model_validate(data)
            response = ws_schemas.ChatWSResponseSchema(
                number=self.message_id,
                message=message_data.message
            )
        except ValidationError:
            response = ws_schemas.ChatWSErrorSchema(
                number=self.message_id,
                message="Ошибка обработки данных"
            )

        try:
            self.message_id += 1
            await self.connection.send_json(response.model_dump())
        except ConnectionClosed:
            print("Сокет-соединение прервано")
