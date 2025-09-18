from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    BOT_TOKEN: str = Field(..., description="Telegram Bot API token")
    DATABASE_URL: str = Field("sqlite+aiosqlite:///./catalog.db")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()