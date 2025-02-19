import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.mark.asyncio
class TestWebSocketEndpoint:

    @pytest.fixture
    def client(self):
        return TestClient(app)

    async def test_websocket_connection(self, client):
        with client.websocket_connect("/ws") as websocket:
            assert websocket  # Подключение прошло успешно

    async def test_websocket_send_receive(self, client):
        with client.websocket_connect("/ws") as websocket:
            test_message = {"message": "Hello, WebSocket!"}

            websocket.send_json(test_message)
            response = websocket.receive_json()

            assert response["number"] == 1
            assert response["message"] == "Hello, WebSocket!"

    async def test_websocket_invalid_message(self, client):
        with client.websocket_connect("/ws") as websocket:
            invalid_message = {"invalid_field": "Wrong data"}

            websocket.send_json(invalid_message)
            response = websocket.receive_json()

            assert response["number"] == 1
            assert response["message"] == "Ошибка обработки данных"

    async def test_websocket_disconnection(self, client):
        with client.websocket_connect("/ws") as websocket:
            websocket.close()
