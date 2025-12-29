from fastapi import FastAPI

from webnovel_reader.web.routes import router


def create_app() -> FastAPI:
    app = FastAPI(title="Webnovel Reader")

    app.include_router(router)

    return app
