from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from webnovel_reader.web.templates import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request, "index.html")
