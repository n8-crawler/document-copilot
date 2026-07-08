from functools import lru_cache

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Supabase
    SUPABASE_URL: AnyHttpUrl
    SUPABASE_ANON_KEY: str
    SUPABASE_SERVICE_ROLE_KEY: str

    # Database
    DATABASE_URL: str

    # Hugging Face
    EMBEDDING_MODEL: str
    EMBEDDING_DIMENSIONS: int

    #llm model config
    LLM_PROVIDER: str
    LLM_MODEL: str
    OLLAMA_BASE_URL: str

    # CORS
    ALLOWED_ORIGINS: str

    #jwt config
    JWT_SECRET_KEY: str
    ALGORITHM: str

    model_config = SettingsConfigDict(
        env_file="/Users/ranjan/Projects/document-copilot/backend/.env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    @property
    def allowed_origins(self) -> list[str]:
        """Convert comma-separated origins into a list."""
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()