from os.path import realpath

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.settings import settings
from websocket.routes import router as websockets_router
from web.routes import router as web_router

app = FastAPI()

app.mount(
    '/static',
    StaticFiles(directory=realpath(f'{realpath(__file__)}/../static')),
    name='static')

app.include_router(web_router)
app.include_router(websockets_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
