from fastapi import APIRouter
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request

router = APIRouter(
    tags=["Web"],
)


templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def get_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

