import pytest
from unittest.mock import AsyncMock
from fastapi import WebSocket
from core.chat_websocket_manager import ChatWebSocketManager
from core.schemas.websockets import ChatWSResponseSchema, ChatWSErrorSchema


@pytest.mark.asyncio
class TestWebSocketManagerEndpoint:
    async def test_connect(self):
        manager = ChatWebSocketManager()
        websocket = AsyncMock(spec=WebSocket)

        await manager.connect(websocket)

        assert websocket.accept.called
        assert websocket in manager.connections

    async def test_disconnect(self):
        manager = ChatWebSocketManager()
        websocket = AsyncMock(spec=WebSocket)

        await manager.connect(websocket)
        await manager.disconnect(websocket)

        assert websocket not in manager.connections
        assert websocket.close.called

    async def test_broadcast_valid_message(self):
        manager = ChatWebSocketManager()
        websocket1 = AsyncMock(spec=WebSocket)
        websocket2 = AsyncMock(spec=WebSocket)

        await manager.connect(websocket1)
        await manager.connect(websocket2)

        message_data = {"message": "Hello, WebSocket!"}
        expected_response = ChatWSResponseSchema(number=1, message="Hello, WebSocket!")

        await manager.broadcast(message_data)

        websocket1.send_json.assert_called_with(expected_response.model_dump())
        websocket2.send_json.assert_called_with(expected_response.model_dump())

    async def test_broadcast_invalid_message(self):
        manager = ChatWebSocketManager()
        websocket = AsyncMock(spec=WebSocket)

        await manager.connect(websocket)

        invalid_data = {"invalid_field": "This is wrong"}
        expected_error_response = ChatWSErrorSchema(number=1, message="Ошибка обработки данных")

        await manager.broadcast(invalid_data)

        websocket.send_json.assert_called_with(expected_error_response.model_dump())
