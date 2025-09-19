from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    BOT_TOKEN: str = Field(..., description="Telegram Bot API token")
    DATABASE_URL: str = Field("sqlite+aiosqlite:///./catalog.db")
    # URL заглушки для товаров без фото
    PLACEHOLDER_IMAGE: str = Field(
        "https://avatars.mds.yandex.net/i?id=e88ee212919876d176895e7fa2bcb4a2f8f48d7d-10115068-images-thumbs&n=13",
    )

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
