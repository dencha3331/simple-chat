from fastapi import WebSocket
from pydantic import ValidationError

from core.schemas import websockets as ws_schemas


class ChatWebSocketManager:
    def __init__(self):
        self.connections: list[WebSocket] = []
        self.message_id = 1

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)
        try:
            await websocket.close()
        except RuntimeError:
            pass

    async def broadcast(self, data: dict):
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

        self.message_id += 1

        for connection in self.connections:
            await connection.send_json(response.model_dump())
