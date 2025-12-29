from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    DEBUG: bool = False

    NOVELS_DIR: Path = Path("novels")

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file_encoding="utf-8",
        env_file=".env",
    )

    def ensure_dirs(self):
        self.NOVELS_DIR.mkdir(exist_ok=True)


settings = Settings()
