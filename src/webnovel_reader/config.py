from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    DEBUG: bool = False

    NOVELS_DIR: Path = Path("novels")

    def ensure_dirs(self):
        self.NOVELS_DIR.mkdir(exist_ok=True)


settings = Settings()
