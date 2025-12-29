import uvicorn

from webnovel_reader.config import settings
from webnovel_reader.web.app import create_app

app = create_app()


def run() -> None:
    uvicorn.run(
        "webnovel_reader.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
