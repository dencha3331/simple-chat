from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.settings import settings
from websocket.routes import router as websockets_router

app = FastAPI()

app.include_router(websockets_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
