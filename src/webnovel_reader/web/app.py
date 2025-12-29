from contextlib import asynccontextmanager

from fastapi import FastAPI

from webnovel_reader.config import settings
from webnovel_reader.services.library import LibraryService
from webnovel_reader.web.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings.ensure_dirs()

    library = LibraryService(settings.NOVELS_DIR)

    app.state.library = library

    yield


def create_app() -> FastAPI:
    app = FastAPI(title="Webnovel Reader", lifespan=lifespan)

    app.include_router(router)

    return app
