from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from webnovel_reader.services.library import LibraryService
from webnovel_reader.web.templates import templates

router = APIRouter()


def get_library(request: Request) -> LibraryService:
    return request.app.state.library


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request, "index.html")
