from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse

from webnovel_reader.services.library import LibraryService
from webnovel_reader.web.templates import templates

router = APIRouter()


def get_library(request: Request) -> LibraryService:
    return request.app.state.library


@router.get("/", response_class=HTMLResponse)
def index(request: Request, lib: Annotated[LibraryService, Depends(get_library)]):
    books = lib.get_all_books()
    books_data = []
    for b in books:
        books_data.append({"book": b})

    return templates.TemplateResponse(
        request, "index.html", {"library_items": books_data}
    )
