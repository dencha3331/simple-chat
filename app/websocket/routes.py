from fastapi import APIRouter, WebSocket
from starlette.websockets import WebSocketDisconnect

from core.chat_websocket_manager import ChatWebSocketManager

router = APIRouter(
    tags=["Websocket"],
)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    ws_manager = ChatWebSocketManager(websocket)
    await ws_manager.connect()

    try:
        while True:

            data = await websocket.receive_json()
            await ws_manager.send_message_to_chat(data)

    except WebSocketDisconnect:
        await ws_manager.disconnect()
    except Exception as e:
        print(f"Error: {e!r}")
        await ws_manager.disconnect()

