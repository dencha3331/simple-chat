import pytest
from unittest.mock import AsyncMock
from fastapi import WebSocket
from core.chat_websocket_manager import ChatWebSocketManager
from core.schemas.websockets import ChatWSResponseSchema, ChatWSErrorSchema


@pytest.mark.asyncio
class TestWebSocketManagerEndpoint:
    async def test_connect(self):
        websocket = AsyncMock(spec=WebSocket)
        manager = ChatWebSocketManager(websocket)

        await manager.connect()

        assert websocket.accept.called
        assert websocket == manager.connection

    async def test_disconnect(self):
        websocket = AsyncMock(spec=WebSocket)
        manager = ChatWebSocketManager(websocket)

        await manager.connect()
        await manager.disconnect()

        assert websocket not in manager.connection
        assert websocket.close.called

    async def test_broadcast_valid_message(self):
        websocket = AsyncMock(spec=WebSocket)
        manager = ChatWebSocketManager(websocket)

        await manager.connect()

        message_data = {"message": "Hello, WebSocket!"}
        expected_response = ChatWSResponseSchema(number=1, message="Hello, WebSocket!")

        await manager.send_message_to_chat(message_data)

        websocket.send_json.assert_called_with(expected_response.model_dump())

    async def test_broadcast_invalid_message(self):
        websocket = AsyncMock(spec=WebSocket)
        manager = ChatWebSocketManager(websocket)

        await manager.connect()

        invalid_data = {"invalid_field": "This is wrong"}
        expected_error_response = ChatWSErrorSchema(number=1, message="Ошибка обработки данных")

        await manager.send_message_to_chat(invalid_data)

        websocket.send_json.assert_called_with(expected_error_response.model_dump())
